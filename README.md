# vote-app
Simple CRUD service that can be used to build demo docker images and for kubernetes demos


There are 4 endpoints 


  1. `/health` -> Check if the application is running
  2. `/register?name` -> Register a candidate, take query parameter `name`, ex - > `/register?name=sandeep`
  3. `/candidates` -> Returns a list of registered candidated
  4. `/vote/{candidate_name}` -> votes for `candidate_name`
  5. `/winner` -> Returns the candidate with most votes
  6. `/crash` -> Crashes the application
  7. `/version` -> Returns the app version
  
  
 This is automatically built as a docker image. To download the docker image 
 ```bash
 docker pull sandyjswl/vote-app:latest
 ```
 
 ```bash
 docker run -d -p 5000:5000 sandyjswl/vote-app:latest
 ```
