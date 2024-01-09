import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';
import MenuItem from '@mui/material/MenuItem';
import AppoinmentsList from './AppoinmentsList';


const currencies = [
  {
    value: 'USD',
    label: '$',
  },
  {
    value: 'EUR',
    label: '€',
  },
  {
    value: 'BTC',
    label: '฿',
  },
  {
    value: 'JPY',
    label: '¥',
  },
];

const AppointmentsForm = () => {
  return (
    <Grid   sx={{ marginBottom: 3 }} >
    <Card spacing={{ xs: 2, md: 3 }} sx={{ minWidth: 10, textAlign: 'center' }}>
      <CardContent>
        <Grid container spacing={2}>
          <Grid item xs={12} sm={6} md={3}>
            <TextField 
              id="truck" 
              label="truck" 
              variant="outlined" 
              fullWidth />
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
          <TextField
                id="standard-select-currency"
                select
                label="Truck"
                defaultValue="EUR"
                fullWidth
                >
                {currencies.map((option) => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
            </TextField>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
          <TextField
                id="standard-select-currency"
                select
                label="Truck"
                defaultValue="EUR"
                fullWidth
                >
                {currencies.map((option) => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
            </TextField>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
          <TextField
                id="standard-select-currency"
                select
                label="Truck"
                defaultValue="EUR"
                fullWidth
                >
                {currencies.map((option) => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
            </TextField>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
          <TextField
                id="standard-select-currency"
                select
                label="Truck"
                defaultValue="EUR"
                fullWidth
                >
                {currencies.map((option) => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
            </TextField>
          </Grid>
        </Grid>
      </CardContent>

      <CardActions sx={{ justifyContent: 'flex-end' }}>
        <Button size="small">Modify</Button>
        <Button size="small">Submit</Button>
      </CardActions>
    </Card>
    </Grid>
  );
};

export default AppointmentsForm;

