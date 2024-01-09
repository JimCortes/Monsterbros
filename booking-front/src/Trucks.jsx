import BasicCard from './BasicCard';
import Grid from '@mui/material/Grid';
import React, { useState, useEffect } from 'react';
import axios from 'axios';


const TruckList = () => {
  const [trucks, setTrucks] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/trucks/');
        setTrucks(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  console.log(trucks)



  return (
    <>
      <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }} sx={{ marginBottom: 3 }}>
        {trucks.map((trucks) => (
          <Grid item xs={12} sm={6} md={4} key={trucks.id}>
            <BasicCard 
            name={trucks.name}
            model={trucks.model}
            year={trucks.year}
            registrationNumber={trucks.registration_number}
              />
          </Grid>
        ))}
      </Grid>
    </>
  );
};

export default TruckList;
