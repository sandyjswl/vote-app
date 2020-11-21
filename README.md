# vote-app
Sample CRUD service used to build demo docker images and kuberneted deployments

This is a sample crud service which i'm using to learn docker and kubernetes. 
There are 4 endpoints 


  1. /check -> returns a string `Checking In if everything is fine`
  2. /register -> POST mapping, to regsiter a new candidate. takes as input a dictionary with one key `name`. EG: {"name":"sandeep"}
  3. /candidates -> GET mapping, returns a list of registered candidated
  4. /vote/{candidate_name} -> votes for `candidate_name`
  5. /winner -> retruns the candidate with most votes
  
  
 This is automatically built as a docker image. To download the docker image 
 ```
 docker pull sandyjswl/vote-app:latest
 ```
 
 When building docker image you have to provide two environment variables REDIS_HOST and REDIS_PORT to connect to redis. Same goes for local connections as well
