# Using PostgreSQL with FastAPI

To run this project, you'll need to have [Docker](https://docs.docker.com/get-docker/) installed, or connect to a database yourself modifying the connection in the codebase.

## Getting started

Set up a virtual environment for the project:  
`python3 -m venv virtualenv`

Activate the environment:  
`source virtualenv/bin/activate`

Install the dependencies:  
`pip install -r requirements.txt`

Run the database (if needed) using the provided Makefile command:  
`make run-db`

Run the API with Uvicorn:  
`uvicorn src.main:app --reload`

Run the database migration:  
`alembic upgrade head`

Hit the POST endpoint with cURL:  
`curl --request POST --data '{"title": "my first job", "description": "an awesome job"}' localhost:8000`

Hit the GET endpoint:  
`curl --request GET "localhost:8000?id=1"`

Hit the DELETE endpoint:  
`curl --request DELETE "localhost:8000?id=1"`
