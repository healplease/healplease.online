import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import { Provider as StoreProvider } from "react-redux";
import { RouterProvider } from "react-router";
import { ThemeProvider } from "@mui/material/styles";

import CSSBaseline from "@mui/material/CssBaseline";

import { store } from "@/app/store";
import { router } from "@/app/router";
import { theme } from "@/app/theme";

import "./globals.css";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <CSSBaseline />
    <StoreProvider store={store}>
      <ThemeProvider theme={theme}>
        <RouterProvider router={router} />
      </ThemeProvider>
    </StoreProvider>
  </StrictMode>,
);
