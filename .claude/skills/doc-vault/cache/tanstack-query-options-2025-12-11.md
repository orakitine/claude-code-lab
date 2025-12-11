---
url: https://tanstack.com/query/latest/docs/framework/react/guides/query-options
fetched: 2025-12-11
title: Query Options - TanStack Query
description: Query configuration helper for sharing queryKey and queryFn with type safety
---

# Query Options

## Overview

The `queryOptions` helper provides a way to share `queryKey` and `queryFn` between multiple locations while keeping them co-located. At runtime, it simply returns the input, but offers significant advantages when using TypeScript.

## Purpose

This helper enables you to:
- Define all query configuration in a single place
- Maintain type inference and type safety across your application
- Share query definitions between hooks and utility functions

## Basic Usage

```typescript
import { queryOptions } from '@tanstack/react-query'

function groupOptions(id: number) {
  return queryOptions({
    queryKey: ['groups', id],
    queryFn: () => fetchGroups(id),
    staleTime: 5 * 1000,
  })
}
```

## Implementation Examples

Once defined, `queryOptions` can be used across various TanStack Query APIs:

```typescript
// In hooks
useQuery(groupOptions(1))
useSuspenseQuery(groupOptions(5))

// In batch queries
useQueries({
  queries: [groupOptions(1), groupOptions(2)],
})

// With QueryClient methods
queryClient.prefetchQuery(groupOptions(23))
queryClient.setQueryData(groupOptions(42).queryKey, newGroups)
```

## Overriding Options

You can override specific options at the component level while maintaining type safety. A common pattern involves adding per-component `select` functions:

```typescript
const query = useQuery({
  ...groupOptions(1),
  select: (data) => data.groupName,
})
```

Type inference automatically adjusts so `query.data` reflects the `select` function's return type.

## For Infinite Queries

A dedicated `infiniteQueryOptions` helper exists for infinite query configurations, following the same pattern as `queryOptions`.
