// ThemeProvider.js
import { createTheme, ThemeProvider as MuiThemeProvider } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#D62B38', // Red
    },
    secondary: {
      main: '#A4C53F', // Green
    },
    background: {
      default: '#ffffff', // Background
    },
  },
});

function ThemeProvider({ children }) {
  return <MuiThemeProvider theme={theme}>{children}</MuiThemeProvider>;
}

export default ThemeProvider;
