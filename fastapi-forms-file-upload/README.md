# Forms and File Uploads with FastAPI and Jinja2


## Getting started

Create a virtual environment for the project:  
`python3 -m venv virtualenv`

Then activate the virtual environment:  
`source virtualenv/bin/activate`  
Or on Powershell:  
`.\virtualenv\Scripts\Activate.ps1`

Now install the dependencies for the project:  
`pip install -r requirements.txt`

You should now be able to run the API with:  
`python app.py`

In a browser navigate to `http://127.0.0.1:8000/basic` to see the basic form  
Or navigate to `http://127.0.0.1:8000/awesome` to see the form using the Pydantic schema
