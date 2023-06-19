import React from "react";
import ReactDOM from "react-dom/client";
import { RouterProvider } from "react-router-dom";
import {
  QueryClient,
  QueryClientProvider,
} from "react-query";
import './styles.css';

import { router } from "./pages";
import Layout from "./components/Layout";

// TODO: connect state manager and get csrf token

const queryClient = new QueryClient()

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <Layout>
        <RouterProvider router={router} />
      </Layout>
    </QueryClientProvider>
  </React.StrictMode>
);
