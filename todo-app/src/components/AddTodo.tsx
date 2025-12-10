import { useState, type FormEvent } from 'react';

interface AddTodoProps {
  onAdd: (text: string) => void;
}

export function AddTodo({ onAdd }: AddTodoProps) {
  const [text, setText] = useState('');

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    if (text.trim()) {
      onAdd(text.trim());
      setText('');
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{ display: 'flex', gap: '0.5rem', marginBottom: '1rem' }}
    >
      <input
        type="text"
        value={text}
        onChange={e => setText(e.target.value)}
        placeholder="What needs to be done?"
        style={{
          flex: 1,
          padding: '0.5rem',
          border: '1px solid #ddd',
          borderRadius: '4px',
        }}
        aria-label="New todo text"
      />
      <button
        type="submit"
        style={{
          padding: '0.5rem 1rem',
          backgroundColor: '#4CAF50',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          cursor: 'pointer',
        }}
      >
        Add
      </button>
    </form>
  );
}
