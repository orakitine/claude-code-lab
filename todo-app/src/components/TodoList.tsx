import type { Todo } from '../types';
import { TodoItem } from './TodoItem';

interface TodoListProps {
  todos: Todo[];
  onToggle: (id: string) => void;
  onDelete: (id: string) => void;
}

export function TodoList({ todos, onToggle, onDelete }: TodoListProps) {
  if (todos.length === 0) {
    return (
      <div style={{ textAlign: 'center', padding: '2rem', color: '#999' }}>
        No todos yet. Add one above!
      </div>
    );
  }

  return (
    <div style={{ border: '1px solid #ddd', borderRadius: '4px' }}>
      {todos.map(todo => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onToggle={onToggle}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}
