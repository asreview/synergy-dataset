import React from 'react';
import ReactDOM from 'react-dom';
import { makeStyles } from '@material-ui/core/styles';

import {Button, Box, Container} from '@material-ui/core/';
import Typography from '@material-ui/core/Typography';

import StepperUpload from './StepperUpload'

const useStyles = makeStyles({
  title: {
    margin: "40px 0px 40px 0px",
  },
  description: {
    display: "block",
    margin: "0px 0px 14px 0px",
  },
});

function App() {
  const classes = useStyles();

  return (
    <Box>
      <Container maxWidth="md">
        <Typography variant="h4" className={classes.title}>Add dataset to Open Dataset on Study Selection (ODSS)</Typography>
        <Typography variant="p" className={classes.description}>This step-by-step instruction helps you to add a dataset to the Open Dataset on Study Selection (ODSS). The instructions help you to upload your dataset to a repository of choice and upload the metadata to the ODSS repository.</Typography>
        <Typography variant="p" className={classes.description}>Running into problems or question during the step-by-step instructions? Try to continue with the next step. In the end, the ODSS team can help you via Github to resolve your issues.</Typography>
        <Typography variant="p" className={classes.description}>Contact the team via asreview@uu.nl</Typography>

        <StepperUpload/>
      </Container>
    </Box>
  );
}

export default App
