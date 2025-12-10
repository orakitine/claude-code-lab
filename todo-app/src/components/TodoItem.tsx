import type { Todo } from '../types';

interface TodoItemProps {
  todo: Todo;
  onToggle: (id: string) => void;
  onDelete: (id: string) => void;
}

export function TodoItem({ todo, onToggle, onDelete }: TodoItemProps) {
  return (
    <div
      style={{
        display: 'flex',
        alignItems: 'center',
        padding: '0.5rem',
        borderBottom: '1px solid #ddd',
      }}
    >
      <input
        type="checkbox"
        checked={todo.completed}
        onChange={() => onToggle(todo.id)}
        style={{ marginRight: '0.5rem' }}
        aria-label={`Toggle ${todo.text}`}
      />
      <span
        style={{
          flex: 1,
          textDecoration: todo.completed ? 'line-through' : 'none',
          color: todo.completed ? '#999' : '#333',
        }}
      >
        {todo.text}
      </span>
      <button
        onClick={() => onDelete(todo.id)}
        style={{
          padding: '0.25rem 0.5rem',
          backgroundColor: '#ff4444',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          cursor: 'pointer',
        }}
        aria-label={`Delete ${todo.text}`}
      >
        Delete
      </button>
    </div>
  );
}
