---
url: https://tanstack.com/query/latest/docs/framework/react/guides/optimistic-updates
fetched: 2025-12-11
title: Optimistic Updates - TanStack Query
description: Two strategies for optimistically updating UI before mutations complete - via UI or cache manipulation
---

# Optimistic Updates

React Query provides two strategies for optimistically updating your UI before a mutation completes: direct UI updates using mutation variables, or cache manipulation via the `onMutate` handler.

## Via the UI

This simpler approach doesn't interact with the cache directly. Access the mutation's `variables` to display a temporary item while the request is pending:

```tsx
const addTodoMutation = useMutation({
  mutationFn: (newTodo: string) => axios.post('/api/data', { text: newTodo }),
  onSettled: () => queryClient.invalidateQueries({ queryKey: ['todos'] }),
})

const { isPending, variables, mutate, isError } = addTodoMutation
```

Render a temporary list item with reduced opacity during the pending state:

```tsx
<ul>
  {todoQuery.items.map((todo) => (
    <li key={todo.id}>{todo.text}</li>
  ))}
  {isPending && <li style={{ opacity: 0.5 }}>{variables}</li>}
</ul>
```

When the mutation completes successfully, the item automatically becomes a normal list item. If it fails, the temporary item disappears—though you can retain it by checking `isError` and offering a retry button.

### Cross-Component Access

For mutations in different components, use `useMutationState` with a `mutationKey`:

```tsx
const { mutate } = useMutation({
  mutationFn: (newTodo: string) => axios.post('/api/data', { text: newTodo }),
  mutationKey: ['addTodo'],
})

// Access elsewhere
const variables = useMutationState<string>({
  filters: { mutationKey: ['addTodo'], status: 'pending' },
  select: (mutation) => mutation.state.variables,
})
```

Variables return as an array since multiple mutations may run concurrently.

## Via the Cache

For more complex scenarios, use `onMutate` to directly update cached data and implement rollback logic on failure.

### Updating a List

```tsx
useMutation({
  mutationFn: updateTodo,
  onMutate: async (newTodo) => {
    await queryClient.cancelQueries({ queryKey: ['todos'] })
    const previousTodos = queryClient.getQueryData(['todos'])
    queryClient.setQueryData(['todos'], (old) => [...old, newTodo])
    return { previousTodos }
  },
  onError: (err, newTodo, onMutateResult) => {
    queryClient.setQueryData(['todos'], onMutateResult.previousTodos)
  },
  onSettled: () =>
    queryClient.invalidateQueries({ queryKey: ['todos'] }),
})
```

### Updating a Single Item

```tsx
useMutation({
  mutationFn: updateTodo,
  onMutate: async (newTodo) => {
    await queryClient.cancelQueries({ queryKey: ['todos', newTodo.id] })
    const previousTodo = queryClient.getQueryData(['todos', newTodo.id])
    queryClient.setQueryData(['todos', newTodo.id], newTodo)
    return { previousTodo, newTodo }
  },
  onError: (err, newTodo, onMutateResult) => {
    queryClient.setQueryData(
      ['todos', onMutateResult.newTodo.id],
      onMutateResult.previousTodo,
    )
  },
  onSettled: () =>
    queryClient.invalidateQueries({ queryKey: ['todos'] }),
})
```

## When to Use Each

Use UI-based updates when the optimistic result appears in only one location—less code, no rollback handling needed. Use cache updates when multiple screen locations need awareness of the change; the cache automatically propagates updates everywhere.
