# proxy-demo
The purpose of the repository is to demonstrate how a proxy setup affects the services behind it.  
This is a real world example (simplified) and used to give people a better understanding of the problem.  
 
## Running locally
To get this running locally, you would need to install Docker, docker-compose and optionally make.  
Then simply run it with:  
```bash
make build run
```
This will build all the images used, and then run them.
If everything goes well, you should now be able to access the setup on [localhost:8080](http://localhost:8080).   
