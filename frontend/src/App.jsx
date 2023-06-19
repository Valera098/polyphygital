import { useState } from "react";
import { RouterProvider } from "react-router-dom";

import { router } from "./pages";
import Layout from "./components/Layout";
import { UserContext } from "./contexts";

import './styles.css';

export default function App() {
  const [user, setUser] = useState(null);

  return (
    <UserContext.Provider value={{
      user,
      setUser
    }}>
      <Layout>
        <RouterProvider router={router} />
      </Layout>
    </UserContext.Provider>
  );
}