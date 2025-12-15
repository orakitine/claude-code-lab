import { Check, X } from 'lucide-react';
import type { Todo } from '../types';

interface TodoItemProps {
  todo: Todo;
  onToggle: (id: string) => void;
  onDelete: (id: string) => void;
}

export function TodoItem({ todo, onToggle, onDelete }: TodoItemProps) {
  return (
    <div
      className="flex items-center gap-3 px-4 py-3 border-b border-gray-200 dark:border-gray-700
                 hover:bg-gray-50 dark:hover:bg-gray-700/50 transition-colors group"
    >
      <button
        onClick={() => onToggle(todo.id)}
        className={`flex-shrink-0 w-5 h-5 rounded border-2 flex items-center justify-center
                   transition-all ${
                     todo.completed
                       ? 'bg-primary border-primary'
                       : 'border-gray-300 dark:border-gray-600 hover:border-primary'
                   }`}
        aria-label={`Toggle ${todo.text}`}
      >
        {todo.completed && <Check size={14} className="text-white" />}
      </button>
      <span
        className={`flex-1 transition-all ${
          todo.completed
            ? 'line-through text-gray-400 dark:text-gray-500'
            : 'text-gray-900 dark:text-gray-100'
        }`}
      >
        {todo.text}
      </span>
      <button
        onClick={() => onDelete(todo.id)}
        className="flex-shrink-0 p-1.5 text-red-500 hover:bg-red-50 dark:hover:bg-red-900/20
                   rounded-lg transition-colors opacity-0 group-hover:opacity-100
                   focus:opacity-100 focus:outline-none focus:ring-2 focus:ring-red-500"
        aria-label={`Delete ${todo.text}`}
      >
        <X size={18} />
      </button>
    </div>
  );
}
