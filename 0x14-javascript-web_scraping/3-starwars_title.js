#!/usr/bin/node

const request = require('request')
let url = 'https://swapi.co/api/films/'
const MovieId = process.argv.slice(2)

request(url, MovieId[0], function(err, response, body) {
  if (err) {
    console.log(err);
  } else {
      console.log(JSON.parse(body).title);
  } 
});
