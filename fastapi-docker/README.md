# Containerize a FastAPI app with Docker

To run this project, you'll need to have [Docker](https://docs.docker.com/get-docker/) installed.

## Getting started

Build the container, providing a tag:  
`docker build -t fastapi-hello-world:0.1 .`

Then you can run the container, passing in a name for the container, and the previously used tag:  
`docker run -p 8000:8000 --name my-api fastapi-hello-world:0.1`

Note that if you used the code as-is with the `--reload` option that you won't be able to kill the container using `CTRL + C`.  
Instead in another terminal window you can kill the container using Docker's kill command:  
`docker kill my-api`
