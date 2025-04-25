import { createBrowserRouter } from "react-router";

import App from "./app/page";
import AppLayout from "./app/layout";

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
