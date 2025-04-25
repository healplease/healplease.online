import Typography from "@mui/material/Typography";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";

const App = () => {
  return (
    <Card>
      <CardContent>
        <Typography variant="h1" component="div">
          healplease.online
        </Typography>
        <Typography variant="body1" color="text.secondary">
          You have nowhere to go?
        </Typography>
      </CardContent>
    </Card>
  );
};

export default App;