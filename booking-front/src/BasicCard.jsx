// BasicCard.js
import Divider from '@mui/material/Divider';
import React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Collapse from '@mui/material/Collapse';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { styled } from '@mui/material/styles';
import IconButton from '@mui/material/IconButton';
import { useTheme } from '@mui/system';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import EmailIcon from '@mui/icons-material/Email';
import TodayIcon from '@mui/icons-material/Today';
import PersonIcon from '@mui/icons-material/Person';
import NotesIcon from '@mui/icons-material/Notes';

const ExpandMore = styled((props) => {
  const { expand, ...other } = props;
  return <IconButton {...other} />;
})(({ theme, expand }) => ({
  transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
  marginLeft: 'auto',
  transition: theme.transitions.create('transform', {
    duration: theme.transitions.duration.shortest,
  }),
}));



const BasicCard = ({ truck, customer, appointment_time, status, phone, email, address, notes }) => {
  const theme = useTheme();

  
  const [expanded, setExpanded] = React.useState(false);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };
 
  return (
    <Card sx={{ minWidth: 275, textAlign: 'center', 
              display: 'flex',flexDirection: 'column' }}>
      <CardContent sx={{ display: 'flex', flexDirection: 'column'}}>
      <Typography variant="h6" component="div" 
                  sx={{ 
                        mb: 2, 
                        textAlign: 'left', 
                        }}> 
                           
                        <TodayIcon sx={{color: theme.palette.secondary.main}}/> {appointment_time} 
        </Typography>
        <Typography  variant="h6" component="div" 
                     sx={{ 
                        textAlign: 'left', 

                     }}>
        <PersonIcon sx={{color: theme.palette.secondary.main}}/>{customer}
        </Typography>
        <Typography  variant="body" component="div" 
                     sx={{mb: 0, 
                        textAlign: 'left',

                     }}>
          <EmailIcon sx={{color: theme.palette.secondary.main}}/> {email}
        </Typography>
        <Typography  variant="body" component="div" 
                     sx={{mb: 1, 
                        textAlign: 'left', 

                     }}>
         <LocationOnIcon sx={{color: theme.palette.secondary.main}}/> {address}
        </Typography>
        <Typography variant="body" component="div" sx={{textAlign: 'left' }}>
          <NotesIcon sx={{ color: theme.palette.secondary.main }} />
          {notes.length > 0 && (
        <div>
          {notes[notes.length - 1].user} : {notes[notes.length - 1].notes}
        </div>
  )}
        </Typography>

    
      </CardContent>
      <CardActions  component="div" 
                    sx={{  alignSelf: 'flex-end', marginTop: 'auto' }}>
         <Button variant="outlined" size="small"
             sx={{ marginRight: 1 }}>
              call
            </Button>
          <Button variant="outlined" size="small"
             sx={{ marginRight: 0 }}>
              map
          </Button>
    
        <ExpandMore
          expand={expanded}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
        >
          <ExpandMoreIcon />
        </ExpandMore>
      </CardActions>
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent>
        <Typography variant="body" component="div" sx={{textAlign: 'left' }}>
          <NotesIcon sx={{ color: theme.palette.secondary.main }} />
            {notes.map((note, index) => (
              <div key={index}>
                {note.user} : {note.notes}
              </div>
            ))}
        </Typography>
          <Typography paragraph>Method:</Typography>
          <Typography paragraph>
            Heat 1/2 cup of the broth in a pot until simmering, add saffron and set
            aside for 10 minutes.
          </Typography>
          <Typography paragraph>
            Heat oil in a (14- to 16-inch) paella pan or a large, deep skillet over
            medium-high heat. Add chicken, shrimp and chorizo, and cook, stirring
            occasionally until lightly browned, 6 to 8 minutes. Transfer shrimp to a
            large plate and set aside, leaving chicken and chorizo in the pan. Add
            pimentón, bay leaves, garlic, tomatoes, onion, salt and pepper, and cook,
            stirring often until thickened and fragrant, about 10 minutes. Add
            saffron broth and remaining 4 1/2 cups chicken broth; bring to a boil.
          </Typography>
          <Typography paragraph>
            Add rice and stir very gently to distribute. Top with artichokes and
            peppers, and cook without stirring, until most of the liquid is absorbed,
            15 to 18 minutes. Reduce heat to medium-low, add reserved shrimp and
            mussels, tucking them down into the rice, and cook again without
            stirring, until mussels have opened and rice is just tender, 5 to 7
            minutes more. (Discard any mussels that don&apos;t open.)
          </Typography>
          <Typography>
            Set aside off of the heat to let rest for 10 minutes, and then serve.
          </Typography>
          <ExpandMore
          expand={expanded}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
        >
          <ExpandMoreIcon />
        </ExpandMore>
        </CardContent>
      </Collapse>
    </Card>
  );
};

export default BasicCard;
