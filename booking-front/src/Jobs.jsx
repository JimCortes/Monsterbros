// Functional Component
import BasicCard from './BasicCard';
import Grid from '@mui/material/Grid';
import EnhancedTable from './Tables';
import AppoinmentsForm from './Appoinments';
import AppoinmentsList from './AppoinmentsList';
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const apiEndpoint = import.meta.env.VITE_APPOINTMENTS_API_ENDPOINT;
console.log(apiEndpoint)

const Jobs = () => {
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

  const formatDate = (dateString) => {
    try {
      const date = new Date(dateString);
      
      const options = {
        weekday: 'long', // Use 'long' for the day of the week
        day: 'numeric',
        month: 'long', // Use 'long' for the month name
        year: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
      };
  
      const dateFormatter = new Intl.DateTimeFormat('en-CA', options);
      const formattedDate = dateFormatter.format(date);
  
      return formattedDate;;
    } catch (error) {
      return 'Invalid Date';
    }
  };
 



  return (
    <>
    <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}  sx={{ marginBottom: 3 }}>
      {appoinments.map((appoinment) => (
        <Grid item xs={12} sm={6} md={4} key={appoinment.appointment_id}>
          <BasicCard
            customer={appoinment.customer}
            truck={appoinment.truck}
            appointment_time={formatDate(appoinment.appointment_time)}
            status={appoinment.status}
          />
      
        </Grid>
      ))}
         
    </Grid>
    <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}sx={{ overflowX: 'auto' }}>
        <Grid item xs={12} sm={6} md={12}>
        </Grid>
    </Grid>
    </>
  );
};

export default Jobs;