const express=require('express');
const app= express();
const cors=require('cors');
const { request, response } = require('express');
require('dotenv').config();

const dbService =require('./dbService');

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({extended: false}))

//create
app.post('/insert',(request,response) =>{
    console.log(request.body);

})

//read
app.get('/getAll', (request,response)=>{
    const db= dbService.getDbServiceInstance();

    const result =db.getAllData()

    result
    .then(data => response.json({data : data}))
    .catch(err=> console.log(err));
    
    });


//update

//delete

app.listen(5000, ()=> console.log('app is running'))