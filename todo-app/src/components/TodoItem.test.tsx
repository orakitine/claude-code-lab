import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi } from 'vitest';
import { TodoItem } from './TodoItem';
import type { Todo } from '../types';

describe('TodoItem', () => {
  const mockTodo: Todo = {
    id: '1',
    text: 'Test todo',
    completed: false,
    createdAt: new Date(),
  };

  it('renders todo text', () => {
    const onToggle = vi.fn();
    const onDelete = vi.fn();

    render(
      <TodoItem todo={mockTodo} onToggle={onToggle} onDelete={onDelete} />
    );

    expect(screen.getByText('Test todo')).toBeInTheDocument();
  });

  it('calls onToggle when checkbox is clicked', async () => {
    const user = userEvent.setup();
    const onToggle = vi.fn();
    const onDelete = vi.fn();

    render(
      <TodoItem todo={mockTodo} onToggle={onToggle} onDelete={onDelete} />
    );

    const checkbox = screen.getByRole('checkbox');
    await user.click(checkbox);

    expect(onToggle).toHaveBeenCalledWith('1');
  });

  it('calls onDelete when delete button is clicked', async () => {
    const user = userEvent.setup();
    const onToggle = vi.fn();
    const onDelete = vi.fn();

    render(
      <TodoItem todo={mockTodo} onToggle={onToggle} onDelete={onDelete} />
    );

    const deleteButton = screen.getByRole('button', { name: /delete/i });
    await user.click(deleteButton);

    expect(onDelete).toHaveBeenCalledWith('1');
  });

  it('shows completed styling when todo is completed', () => {
    const completedTodo: Todo = { ...mockTodo, completed: true };
    const onToggle = vi.fn();
    const onDelete = vi.fn();

    render(
      <TodoItem todo={completedTodo} onToggle={onToggle} onDelete={onDelete} />
    );

    const text = screen.getByText('Test todo');
    expect(text).toHaveStyle({ textDecoration: 'line-through' });
  });
});
