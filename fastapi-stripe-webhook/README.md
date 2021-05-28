# Stripe Webhooks with FastAPI

## Prerequisites
- Stripe account
- Stripe secret key set as an environment variable
- 2 subscription products created in Stripe
- Billing portal configured
- Stripe CLI installed

## Getting started

Create a virtual environment for the project:  
`python3 -m venv virtualenv`

Then activate the virtual environment:  
`source virtualenv/bin/activate`  
Or on Powershell:  
`.\virtualenv\Scripts\Activate.ps1`

Enter your public key value, and price ids, in `static/script.js`  

Now install the dependencies for the project:  
`pip install -r requirements.txt`

Install the Stripe CLI if you don't already have it, instructions can be found [here](https://stripe.com/docs/stripe-cli#install)  
And then login with the CLI  
`stripe login`  
And follow the instructions  

Use the CLI to forward events to the webhook:  
`stripe listen --forward-to localhost:8000/webhook`  

Copy the output webhook secret and set it as an env variable when running the app:  
`export STRIPE_WEBHOOK_SECRET=replace-me`  

You should now be able to run the API with:  
`python app.py`

In a browser navigate to `http://127.0.0.1:8000/`  
Create a premium or basic subscription  
This will create a customer in Stripe, and enable the billing portal  
In the terminal you should be able to see events being triggered, and the webhook endpoint logging out messages about the events  
