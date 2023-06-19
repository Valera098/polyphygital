import { createBrowserRouter } from "react-router-dom";
import Home from "./Home";
import ErrorPage from "./ErrorPage";
import News from "./News";
import Post from "./News/Post";
import Forum from "./Forum";
import Thread from "./Forum/Thread";
import NewThread from "./Forum/NewThread";
import news from "../api/news";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Home />,
    errorElement: <ErrorPage />,
  },
  {
    path: "/news",
    element: <News />,
    loader: () => {
      return news.getAll();
    },
    children: [
      {
        path: ":postUniqueName",
        element: <Post />,
      },
    ]
  },
  {
    path: "/forum",
    element: <Forum />,
    children: [
      {
        path: ":threadUniqueName",
        element: <Thread />,
      },
      {
        path: "new-thread",
        element: <NewThread />,
      },
    ]
  },
]);
