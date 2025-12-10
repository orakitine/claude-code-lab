import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect } from 'vitest';
import App from './App';

describe('App', () => {
  it('renders the todo app title', () => {
    render(<App />);
    expect(screen.getByText('Todo App')).toBeInTheDocument();
  });

  it('shows empty state when no todos', () => {
    render(<App />);
    expect(screen.getByText(/no todos yet/i)).toBeInTheDocument();
  });

  it('adds a new todo when submitted', async () => {
    const user = userEvent.setup();
    render(<App />);

    const input = screen.getByPlaceholderText(/what needs to be done/i);
    const addButton = screen.getByRole('button', { name: /add/i });

    await user.type(input, 'Test todo item');
    await user.click(addButton);

    expect(screen.getByText('Test todo item')).toBeInTheDocument();
    expect(screen.getByText('0 of 1 completed')).toBeInTheDocument();
  });

  it('toggles todo completion', async () => {
    const user = userEvent.setup();
    render(<App />);

    // Add a todo
    const input = screen.getByPlaceholderText(/what needs to be done/i);
    await user.type(input, 'Test todo');
    await user.click(screen.getByRole('button', { name: /add/i }));

    // Toggle it
    const checkbox = screen.getByRole('checkbox', {
      name: /toggle test todo/i,
    });
    await user.click(checkbox);

    expect(checkbox).toBeChecked();
    expect(screen.getByText('1 of 1 completed')).toBeInTheDocument();
  });

  it('deletes a todo', async () => {
    const user = userEvent.setup();
    render(<App />);

    // Add a todo
    const input = screen.getByPlaceholderText(/what needs to be done/i);
    await user.type(input, 'Todo to delete');
    await user.click(screen.getByRole('button', { name: /add/i }));

    expect(screen.getByText('Todo to delete')).toBeInTheDocument();

    // Delete it
    const deleteButton = screen.getByRole('button', {
      name: /delete todo to delete/i,
    });
    await user.click(deleteButton);

    expect(screen.queryByText('Todo to delete')).not.toBeInTheDocument();
    expect(screen.getByText(/no todos yet/i)).toBeInTheDocument();
  });
});
