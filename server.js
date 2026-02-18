const express = require('express');
const mongoose =require('mongoose');
const ejs = require('ejs');

//express app
const server = express();

server.use(express.json());

//connect to mongoDb
const dbURI ='mongodb+srv://<username>:<pwd>@nodeapp.dsgroh1.mongodb.net/';
mongoose.connect(dbURI)
.then((result) => 
// listen for requests only when connected to our database
    server.listen(7273))
.catch((err) => console.log(err));

server.set('view engine','ejs');



server.get('/',(req,res)=>{
    console.log('request made');
    res.render('index');

})

server.get('/search',(req,res)=>{
    const query = req.query;
    const ques= query.question;
    const arr= [
        {
            title:"knvbed",
            url:"vfd",
            statement:"vdfhjvberhb"

        }
    ]
    res.json(arr);
})

server.get('/result',(req,res)=>{
    res.render('result');
})

server.use((req,res)=>{
    res.status(404).render('404');
})