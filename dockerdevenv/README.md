
# Py Dev in a Container
*could just use terminal with vim but the Volume function is cool*
```
docker build -t fastapi-image .

docker run --name fastapi-container -p 80:80 fastapi-image
```

# detatched mode
```
docker run --name fastapi-container -p 80:80 -d fastapi-image 
```

Code changes happen on loacal machine not in the docker image/container.
Need to map code from local mach to docker code, user Volumes > Docker docs
```
docker stop fastapi-container
docker rm fastapi-container
```

# detatched mode and now maps your current working dir to the working dir of the containter
```
docker run --name fastapi-container -p 80:80 -d - v $(pwd):/code fastapi-image 
```
# vscode connect
Requires *Docker* extenction and *Dev Containers* extention
adds a button on bottom left where you can connect to running containers and such
it opens a new instance of vscode that lives inside the container and nolonger complains about packages if only installed in container then install *Python* extension in the container

# Can do all this with Docker Compose
make docker-compose file
then run
```
docker-compose up
docker-compose down
```
adding more service is simple
add redis
then to redo/refresh/build new container image
```
docker-compose up --build -d
```

# add debuggin inside container
requires *debugpy* package installed
debugpy: is the port addition of 5678:5678
```
docker-compose up --build -d
```
in vscode to to *Run and Debug*
then *create a launch.json file*
then *Remote Attach*
leave *localhost*
and default port of *5678*
then *start debugging*
when you go to endpoint it takes you to the debugger
