import { useState, type FormEvent } from 'react';
import { Plus } from 'lucide-react';

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
    <form onSubmit={handleSubmit} className="flex gap-2 mb-4">
      <input
        type="text"
        value={text}
        onChange={e => setText(e.target.value)}
        placeholder="What needs to be done?"
        className="flex-1 px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg
                   bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100
                   focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent
                   transition-all"
        aria-label="New todo text"
      />
      <button
        type="submit"
        className="flex items-center gap-2 px-4 py-2 bg-primary hover:bg-primary-dark
                   text-white rounded-lg font-medium transition-colors
                   focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2"
      >
        <Plus size={20} />
        <span className="hidden sm:inline">Add</span>
      </button>
    </form>
  );
}
