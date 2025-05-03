import { useState, useEffect } from "react";

import Typography from "@mui/material/Typography";
import { Box } from "@mui/material";

import "./page.css";

const App = () => {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        minHeight: "100vh",
      }}
    >
      <Typography variant="h1" component="h1" gutterBottom color="white" fontWeight={500} fontSize={120} letterSpacing={12}>
        HEALPLEASE
      </Typography>
      <Typography variant="h3" component="h3" gutterBottom color="white" fontWeight={300} fontSize={40} letterSpacing={3}>
        Social links will be here
      </Typography>
    </Box>
  );
};

export default App;