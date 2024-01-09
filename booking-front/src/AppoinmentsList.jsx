import BasicCard from './BasicCard';
import Grid from '@mui/material/Grid';
import React, { useState, useEffect } from 'react';
import axios from 'axios';


const AppoinmentsList = () => {
    const [appoinments, setAppoinments] = useState([]);
  
    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/appointments/');
          setAppoinments(response.data);
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };
  
      fetchData();
    }, []);
  
  
      
     console.log(appoinments)
    return (
      <>
        <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }} sx={{ marginBottom: 3 }}>
          {appoinments.map((appoinment) => (
            <Grid item xs={12} sm={6} md={4} key={appoinment.id}>
              <BasicCard 
              appointment_time={appoinment.appointment_time}
              truck={appoinment.truck}
              customer={appoinment.customer}
              status={appoinment.status}
                />
            </Grid>
          ))}
        </Grid>
        
      </>
    );
  
  };
  
export default AppoinmentsList;