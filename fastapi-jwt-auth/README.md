# FastAPI JWT Auth

## Getting Started

Set up a virtual environment for the project:  
`python3 -m venv virtualenv`

Activate the environment:  
`source virtualenv/bin/activate`

Install the dependencies:  
`pip install -r requirements.txt`

Run the API with Uvicorn:  
`uvicorn src.main:app --reload`

Hit the unprotected endpoint with cURL:  
`curl localhost:8000/unprotected`

Hit the protected endpoint with cURL to get a 403:  
`curl localhost:8000/protected`

Register a user:  
`curl --header "Content-Type: application/json" --request POST --data '{"username": "ian", "password": "secretpassword"}' localhost:8000/register`

Log in and get a token:  
`curl --header "Content-Type: application/json" --request POST --data '{"username": "ian", "password": "secretpassword"}' localhost:8000/login`

Then use that token as an auth header to get a valid response from the protected endpoint:  
`curl --header "Authorization: Bearer <TOKEN>" localhost:8000/protected`
