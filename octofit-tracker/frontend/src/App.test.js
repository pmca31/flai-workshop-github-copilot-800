import { render, screen } from '@testing-library/react';
import App from './App';

test('renders OctoFit Tracker welcome heading', () => {
  render(<App />);
  const headingElement = screen.getByText(/Welcome to OctoFit Tracker/i);
  expect(headingElement).toBeInTheDocument();
});

test('renders OctoFit Tracker navbar', () => {
  render(<App />);
  const navbar = screen.getByRole('navigation');
  expect(navbar).toBeInTheDocument();
  expect(navbar).toHaveTextContent('OctoFit Tracker');
});
