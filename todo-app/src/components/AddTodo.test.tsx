import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi } from 'vitest';
import { AddTodo } from './AddTodo';

describe('AddTodo', () => {
  it('renders input and add button', () => {
    const onAdd = vi.fn();
    render(<AddTodo onAdd={onAdd} />);

    expect(
      screen.getByPlaceholderText(/what needs to be done/i)
    ).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /add/i })).toBeInTheDocument();
  });

  it('calls onAdd with trimmed text when form is submitted', async () => {
    const user = userEvent.setup();
    const onAdd = vi.fn();
    render(<AddTodo onAdd={onAdd} />);

    const input = screen.getByPlaceholderText(/what needs to be done/i);
    await user.type(input, '  New todo  ');
    await user.click(screen.getByRole('button', { name: /add/i }));

    expect(onAdd).toHaveBeenCalledWith('New todo');
  });

  it('clears input after submission', async () => {
    const user = userEvent.setup();
    const onAdd = vi.fn();
    render(<AddTodo onAdd={onAdd} />);

    const input = screen.getByPlaceholderText(
      /what needs to be done/i
    ) as HTMLInputElement;
    await user.type(input, 'New todo');
    await user.click(screen.getByRole('button', { name: /add/i }));

    expect(input.value).toBe('');
  });

  it('does not call onAdd when text is empty or whitespace', async () => {
    const user = userEvent.setup();
    const onAdd = vi.fn();
    render(<AddTodo onAdd={onAdd} />);

    const input = screen.getByPlaceholderText(/what needs to be done/i);
    await user.type(input, '   ');
    await user.click(screen.getByRole('button', { name: /add/i }));

    expect(onAdd).not.toHaveBeenCalled();
  });
});
