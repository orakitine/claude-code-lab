import { useState } from 'react';
import './App.css';
import type { Todo } from './types';
import { AddTodo } from './components/AddTodo';
import { TodoList } from './components/TodoList';

function App() {
  const [todos, setTodos] = useState<Todo[]>([]);

  const handleAddTodo = (text: string) => {
    const newTodo: Todo = {
      id: crypto.randomUUID(),
      text,
      completed: false,
      createdAt: new Date(),
    };
    setTodos(prev => [...prev, newTodo]);
  };

  const handleToggleTodo = (id: string) => {
    setTodos(prev =>
      prev.map(todo =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      )
    );
  };

  const handleDeleteTodo = (id: string) => {
    setTodos(prev => prev.filter(todo => todo.id !== id));
  };

  const completedCount = todos.filter(t => t.completed).length;
  const totalCount = todos.length;

  return (
    <div style={{ maxWidth: '600px', margin: '2rem auto', padding: '1rem' }}>
      <h1 style={{ textAlign: 'center', marginBottom: '2rem' }}>Todo App</h1>
      <AddTodo onAdd={handleAddTodo} />
      <div style={{ marginBottom: '1rem', color: '#666', fontSize: '0.9rem' }}>
        {completedCount} of {totalCount} completed
      </div>
      <TodoList
        todos={todos}
        onToggle={handleToggleTodo}
        onDelete={handleDeleteTodo}
      />
    </div>
  );
}

export default App;
