import React, { Component } from 'react';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import MaterialTable from 'material-table'
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      text: '',
      result: '',
      data: []
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({text: event.target.value});
    console.log(this.state.text);
  }

  handleSubmit(event) {
    let url = 'http://0.0.0.0:5000?text=' + this.state.text         
    fetch(url).then(response => response.json()).then((repos) => {
      this.setState({
        data: repos.law,
      });
      console.log(this.state.data)
    });
  }
  
  render() {
    return (
      <div className="App">
        <Typography variant="h4">
          Legal texts analysis for identifying suspect’s violated law sections
        </Typography>
        <Typography variant="h6">
          By using Natural Language Processing technique
        </Typography>
        <hr></hr>
        <div style={{display:"flex", flexDirection:"row"}}>
          <div style={{width:"50%", paddingRight:"20px"}}>
            <TextField
              id="outlined-multiline-static"
              label="Please enter text you want to analyze"
              multiline
              rows="18"
              margin="normal"
              variant="outlined"
              fullWidth
              onChange={this.handleChange}
            />
            <div style={{justifyContent:"space-around", display:"flex"}}>
              <Button variant="outlined" color="primary" style={{width:"100%"}} onClick={this.handleSubmit}>
                Analyze
              </Button>
              {/* <Button variant="outlined" color="secondary" style={{width:"48%"}} onClick={this.clearData}>
                Clear
              </Button> */}
            </div>
          </div>
          <div style={{width:"50%", marginTop:"16px"}}>
          <MaterialTable
            columns={[
              { title: 'Code', field: 'code' },
              { title: 'Description', field: 'desc' },
              { title: 'SimScore', field: 'score', type: 'numeric' },
            ]}
            data={this.state.data}
            title="Body Scroll Example"
            options={{
              paging: true,
              maxBodyHeight: 364,
              toolbar: false,
              pageSize: 10
            }}
          />
          </div>
        </div>
      </div>
    );
  }
}

export default App;
