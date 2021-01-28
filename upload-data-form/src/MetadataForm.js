import React from 'react';
import TextField from '@material-ui/core/TextField';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(theme => ({
  root: {
    '& .MuiTextField-root': {
      margin: theme.spacing(1),
      width: '100%',
    },
  },
  form: {
    width: '100%',
  }
}));

export default function MetadataForm() {
  const classes = useStyles();
  const [license, setLicense] = React.useState("ccby");

  const handleChange = (event) => {
    setLicense(event.target.value);
  };

  return (
    <form className={classes.root} noValidate autoComplete="off">
      <div>
        <Typography variant="h5">About the journal publication</Typography>
        <TextField required id="metadata-title" label="Title"/>
        <TextField required id="metadata-reference" label="DOI URL"/>
        <TextField required id="metadata-authors" label="Authors (; separated)"/>
        <TextField required id="metadata-year" label="Year"/>
        <TextField required id="metadata-topic" label="Topic"/>

        <Typography variant="h5">About the dataset</Typography>
        <TextField required id="metadata-link" label="URL (preferably a DOI)"/>
        <TextField required id="metadata-url" label="URL to file"/>
        <FormControl className={classes.formControl}>
          <InputLabel id="metadata-license">License</InputLabel>
          <Select
            labelId="metadata-license"
            id="metadata-license-select"
            value={license}
            onChange={setLicense}
          >
            <MenuItem value={"cc0"}>CC0</MenuItem>
            <MenuItem value={"ccby"}>CC-BY Attribution 4.0 International</MenuItem>
            <MenuItem value={"other"}>Other/don't know</MenuItem>
          </Select>
        </FormControl>
      </div>
    </form>
  );
}
