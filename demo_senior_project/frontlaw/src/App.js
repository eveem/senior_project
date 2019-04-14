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
      rows: []
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
    fetch(url).then(repos => {
      this.setState({
        result: repos
      })
      console.log(repos)
    })
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
        <div style={{display:"flex", flexDirection:"row"}}>
          <div style={{width:"50%", marginTop:"10px", paddingRight:"20px"}}>
            <TextField
              id="outlined-multiline-static"
              label="Please enter text you want to analyze"
              multiline
              rows="18"
              margin="normal"
              variant="outlined"
              fullWidth
            />
            <div style={{justifyContent:"space-between", display:"flex"}}>
              <Button variant="outlined" style={{width:"48%"}}>
                Analyze
              </Button>
              <Button variant="outlined" color="secondary" style={{width:"48%"}}>
                Clear
              </Button>
            </div>
          </div>
          <div style={{width:"50%", marginTop:"26px"}}>
          <MaterialTable
            columns={[
              { title: 'Code', field: 'code' },
              { title: 'Description', field: 'description' },
            ]}
            data={[
              { code: '288', description: 'เมื่อประมวลกฎหมาย อาญาได้ใช้บังคับแล้ว บทบัญญัติแห่งกฎหมายใดอ้างถึงกฎหมายลักษณะอาญา หรืออ้างถึงบทบัญญัติแห่ง กฎหมายลักษณะอาญา ให้ถือว่าบทบัญญัติแห่งกฎหมายนั้นอ้างถึงประมวลกฎหมายอาญา หรือบทบัญญัติ แห่งประมวลกฎหมายอาญาในบทมาตราที่มีนัยเช่นเดียวกัน แล้วแต่กรณี'},
              { code: '288', description: 'เมื่อประมวลกฎหมาย อาญาได้ใช้บังคับแล้ว บทบัญญัติแห่งกฎหมายใดอ้างถึงกฎหมายลักษณะอาญา หรืออ้างถึงบทบัญญัติแห่ง กฎหมายลักษณะอาญา ให้ถือว่าบทบัญญัติแห่งกฎหมายนั้นอ้างถึงประมวลกฎหมายอาญา หรือบทบัญญัติ แห่งประมวลกฎหมายอาญาในบทมาตราที่มีนัยเช่นเดียวกัน แล้วแต่กรณี'},
              { code: '1', description: 'พระราชบัญญัตินี้เรียกว่า "พระราชบัญญัติ ให้ใช้ประมวลกฎหมายอาญา พ.ศ. 2499"'},
              { code: '288', description: 'เมื่อประมวลกฎหมาย อาญาได้ใช้บังคับแล้ว บทบัญญัติแห่งกฎหมายใดอ้างถึงกฎหมายลักษณะอาญา หรืออ้างถึงบทบัญญัติแห่ง กฎหมายลักษณะอาญา ให้ถือว่าบทบัญญัติแห่งกฎหมายนั้นอ้างถึงประมวลกฎหมายอาญา หรือบทบัญญัติ แห่งประมวลกฎหมายอาญาในบทมาตราที่มีนัยเช่นเดียวกัน แล้วแต่กรณี'},
              { code: '288', description: 'เมื่อประมวลกฎหมาย อาญาได้ใช้บังคับแล้ว บทบัญญัติแห่งกฎหมายใดอ้างถึงกฎหมายลักษณะอาญา หรืออ้างถึงบทบัญญัติแห่ง กฎหมายลักษณะอาญา ให้ถือว่าบทบัญญัติแห่งกฎหมายนั้นอ้างถึงประมวลกฎหมายอาญา หรือบทบัญญัติ แห่งประมวลกฎหมายอาญาในบทมาตราที่มีนัยเช่นเดียวกัน แล้วแต่กรณี'},
              { code: '1', description: 'พระราชบัญญัตินี้เรียกว่า "พระราชบัญญัติ ให้ใช้ประมวลกฎหมายอาญา พ.ศ. 2499"'},
              { code: '288', description: 'เมื่อประมวลกฎหมาย อาญาได้ใช้บังคับแล้ว บทบัญญัติแห่งกฎหมายใดอ้างถึงกฎหมายลักษณะอาญา หรืออ้างถึงบทบัญญัติแห่ง กฎหมายลักษณะอาญา ให้ถือว่าบทบัญญัติแห่งกฎหมายนั้นอ้างถึงประมวลกฎหมายอาญา หรือบทบัญญัติ แห่งประมวลกฎหมายอาญาในบทมาตราที่มีนัยเช่นเดียวกัน แล้วแต่กรณี'},
              { code: '288', description: 'เมื่อประมวลกฎหมาย อาญาได้ใช้บังคับแล้ว บทบัญญัติแห่งกฎหมายใดอ้างถึงกฎหมายลักษณะอาญา หรืออ้างถึงบทบัญญัติแห่ง กฎหมายลักษณะอาญา ให้ถือว่าบทบัญญัติแห่งกฎหมายนั้นอ้างถึงประมวลกฎหมายอาญา หรือบทบัญญัติ แห่งประมวลกฎหมายอาญาในบทมาตราที่มีนัยเช่นเดียวกัน แล้วแต่กรณี'},
              { code: '1', description: 'พระราชบัญญัตินี้เรียกว่า "พระราชบัญญัติ ให้ใช้ประมวลกฎหมายอาญา พ.ศ. 2499"'},
              { code: '288', description: 'เมื่อประมวลกฎหมาย อาญาได้ใช้บังคับแล้ว บทบัญญัติแห่งกฎหมายใดอ้างถึงกฎหมายลักษณะอาญา หรืออ้างถึงบทบัญญัติแห่ง กฎหมายลักษณะอาญา ให้ถือว่าบทบัญญัติแห่งกฎหมายนั้นอ้างถึงประมวลกฎหมายอาญา หรือบทบัญญัติ แห่งประมวลกฎหมายอาญาในบทมาตราที่มีนัยเช่นเดียวกัน แล้วแต่กรณี'},
              { code: '288', description: 'เมื่อประมวลกฎหมาย อาญาได้ใช้บังคับแล้ว บทบัญญัติแห่งกฎหมายใดอ้างถึงกฎหมายลักษณะอาญา หรืออ้างถึงบทบัญญัติแห่ง กฎหมายลักษณะอาญา ให้ถือว่าบทบัญญัติแห่งกฎหมายนั้นอ้างถึงประมวลกฎหมายอาญา หรือบทบัญญัติ แห่งประมวลกฎหมายอาญาในบทมาตราที่มีนัยเช่นเดียวกัน แล้วแต่กรณี'},
              { code: '1', description: 'พระราชบัญญัตินี้เรียกว่า "พระราชบัญญัติ ให้ใช้ประมวลกฎหมายอาญา พ.ศ. 2499"'},
              { code: '288', description: 'เมื่อประมวลกฎหมาย อาญาได้ใช้บังคับแล้ว บทบัญญัติแห่งกฎหมายใดอ้างถึงกฎหมายลักษณะอาญา หรืออ้างถึงบทบัญญัติแห่ง กฎหมายลักษณะอาญา ให้ถือว่าบทบัญญัติแห่งกฎหมายนั้นอ้างถึงประมวลกฎหมายอาญา หรือบทบัญญัติ แห่งประมวลกฎหมายอาญาในบทมาตราที่มีนัยเช่นเดียวกัน แล้วแต่กรณี'},
              { code: '288', description: 'เมื่อประมวลกฎหมาย อาญาได้ใช้บังคับแล้ว บทบัญญัติแห่งกฎหมายใดอ้างถึงกฎหมายลักษณะอาญา หรืออ้างถึงบทบัญญัติแห่ง กฎหมายลักษณะอาญา ให้ถือว่าบทบัญญัติแห่งกฎหมายนั้นอ้างถึงประมวลกฎหมายอาญา หรือบทบัญญัติ แห่งประมวลกฎหมายอาญาในบทมาตราที่มีนัยเช่นเดียวกัน แล้วแต่กรณี'},
              { code: '1', description: 'พระราชบัญญัตินี้เรียกว่า "พระราชบัญญัติ ให้ใช้ประมวลกฎหมายอาญา พ.ศ. 2499"'},
            ]}
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
