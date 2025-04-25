import { createBrowserRouter } from "react-router";

import App from "../pages/index/page";
import AppLayout from "../pages/index/layout";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <AppLayout />,
    children: [
      {
        path: "/",
        element: <App />,
      },
    ],
  },
]);
