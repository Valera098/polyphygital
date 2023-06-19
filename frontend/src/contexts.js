import { createContext } from 'react';

// TODO: connect state manager and get csrf token
export const UserContext = createContext({
  csrf_token: null,
});