import { Outlet } from "react-router";

import Box from "@mui/material/Box";

import bg1920 from "@/assets/img/bg1920.png";

const AppLayout = () => {
  return (
    // outside should be darkened
    <Box 
      sx={{
        display: "flex",
        flexDirection: "column",
        minHeight: "100vh",
        backgroundImage: `url(${bg1920})`,
        backgroundSize: "cover",
      }}
    >
      <Outlet />
    </Box>
  );
};

export default AppLayout;