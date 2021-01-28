import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Box from '@material-ui/core/Box';
import Stepper from '@material-ui/core/Stepper';
import Step from '@material-ui/core/Step';
import StepLabel from '@material-ui/core/StepLabel';
import StepContent from '@material-ui/core/StepContent';
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';

import { Github } from '@icons-pack/react-simple-icons';
import YouTube from 'react-youtube';

import TableExample from './TableExample'
import MetadataForm from './MetadataForm'

const useStyles = makeStyles((theme) => ({
  root: {
    width: '100%',
  },
  button: {
    marginTop: theme.spacing(1),
    marginRight: theme.spacing(1),
  },
  actionsContainer: {
    marginBottom: theme.spacing(2),
  },
  resetContainer: {
    padding: theme.spacing(3),
  },
  github: {
    textAlign: "center",
  },
  githubIcon: {
    display: "block",
    margin: "0 auto",
    padding: '24px',
  },

}));

export default function StepperUpload() {
  const classes = useStyles();
  const [activeStep, setActiveStep] = React.useState(0);

  const VideoSettings = {
    height: '390',
    width: '640',
    playerVars: {
      autoplay: 1,
    },
  };

  const handleNext = () => {
    setActiveStep((prevActiveStep) => prevActiveStep + 1);
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleReset = () => {
    setActiveStep(0);
  };

  const videoReady = (event) => {
    event.target.pauseVideo();
  }

  return (
    <div className={classes.root}>
      <Stepper activeStep={activeStep} orientation="vertical">

        {/* Create Github account */}
        <Step key={'Create Github account'}>
          <StepLabel>{'Create Github account'}</StepLabel>
          <StepContent>
            <Typography>We use Github to host, process, and upload datasets. Create an account if you do not have one already.</Typography>

              <Box className={classes.github}>
                <Github
                  title="Create Github account"
                  color="#000000"
                  size={128}
                  className={classes.githubIcon}
                />
                <Button
                  variant="outlined"
                  target="_blank"
                  href="https://github.com/join/"
                >
                  Create Github account
                </Button>
              </Box>

            <div className={classes.actionsContainer}>
              <div>
                <Button
                  disabled={activeStep === 0}
                  onClick={handleBack}
                  className={classes.button}
                >
                  Back
                </Button>
                <Button
                  variant="contained"
                  color="primary"
                  onClick={handleNext}
                  className={classes.button}
                >
                  {activeStep === 4 ? 'Finish' : 'Next'}
                </Button>
              </div>
            </div>
          </StepContent>
        </Step>

        {/* Format dataset */}
        <Step key={'Format your dataset'}>
          <StepLabel>{'Format your dataset'}</StepLabel>
          <StepContent>
            <Typography>Your dataset needs to be formatted in a specific way. Preferrably, a CSV file with columns 'title', 'abstract', 'label_included'</Typography>
            <TableExample/>
            <div className={classes.actionsContainer}>
              <div>
                <Button
                  disabled={activeStep === 0}
                  onClick={handleBack}
                  className={classes.button}
                >
                  Back
                </Button>
                <Button
                  variant="contained"
                  color="primary"
                  onClick={handleNext}
                  className={classes.button}
                >
                  {activeStep === 4 ? 'Finish' : 'Next'}
                </Button>
              </div>
            </div>
          </StepContent>
        </Step>

        {/* Upload dataset */}
        <Step key={'Upload your dataset'}>
          <StepLabel>{'Upload your dataset'}</StepLabel>
          <StepContent>
            <Typography>Upload your data to Zenodo or OSF.</Typography>

            <div className={classes.actionsContainer}>
              <div>
                <Button
                  disabled={activeStep === 0}
                  onClick={handleBack}
                  className={classes.button}
                >
                  Back
                </Button>
                <Button
                  variant="contained"
                  color="primary"
                  onClick={handleNext}
                  className={classes.button}
                >
                  {activeStep === 4 ? 'Finish' : 'Next'}
                </Button>
              </div>
            </div>
          </StepContent>
        </Step>

        {/* Add metadata */}
        <Step key={'Add information on the study'}>
          <StepLabel>{'Add information on the study'}</StepLabel>
          <StepContent>
            <MetadataForm/>
            <div className={classes.actionsContainer}>
              <div>
                <Button
                  disabled={activeStep === 0}
                  onClick={handleBack}
                  className={classes.button}
                >
                  Back
                </Button>
                <Button
                  variant="contained"
                  color="primary"
                  onClick={handleNext}
                  className={classes.button}
                >
                  {activeStep === 4 ? 'Finish' : 'Next'}
                </Button>
              </div>
            </div>
          </StepContent>
        </Step>

        {/* Upload */}
        <Step key={'Upload metadata to Github'}>
          <StepLabel>{'Upload metadata to Github'}</StepLabel>
          <StepContent>
            <Typography>Upload the downloaded file to Github. </Typography>
            <Button
              variant="outlined"
              target="_blank"
              href="https://github.com/asreview/systematic-review-datasets/upload/master/datasets"
            >
              Upload file to Github
            </Button>
            <YouTube videoId="2g811Eo7K8U" opts={VideoSettings} onReady={videoReady} />
            <div className={classes.actionsContainer}>
              <div>
                <Button
                  disabled={activeStep === 0}
                  onClick={handleBack}
                  className={classes.button}
                >
                  Back
                </Button>
                <Button
                  variant="contained"
                  color="primary"
                  onClick={handleNext}
                  className={classes.button}
                >
                  {activeStep === 4 ? 'Finish' : 'Next'}
                </Button>
              </div>
            </div>
          </StepContent>
        </Step>

      </Stepper>
      {activeStep === 4 && (
        <Paper square elevation={0} className={classes.resetContainer}>
          <Typography>All steps completed - you&apos;re finished</Typography>
          <Button onClick={handleReset} className={classes.button}>
            Reset
          </Button>
        </Paper>
      )}
    </div>
  );
}
