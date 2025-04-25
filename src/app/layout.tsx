import { Outlet } from "react-router";

import Container from "@mui/material/Container";
import Box from "@mui/material/Box";


const AppLayout = () => {
  return (
    // outside should be darkened
    <Box 
      sx={{
        display: "flex",
        flexDirection: "column",
        minHeight: "100vh",
        backgroundColor: (theme) => theme.palette.background.default,
      }}
    >
      <Container maxWidth="lg" sx={{ padding: 2 }}>
        <Outlet />
      </Container>
    </Box>
  );
};

export default AppLayout;