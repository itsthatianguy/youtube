# Twitter Bot

## Getting Started

First register for a developer account with Twitter here: https://developer.twitter.com/en/apply-for-access  
Once registered take a copy of your consumer key, consumer secret, access token, and access token secret, and set them as environment variables to use in the code.

The example is set to run the script every 60 seconds, which may be too frequent - update the first parameter in the sched `enter` call at the end of the `run_bot` function to the length of time you want to wait between executions.

Set up a virtual environment for the project:  
`python -m venv virtualenv`

Activate the environment:  
`source virtualenv/bin/activate`

Install the dependencies:  
`pip install -r requirements.txt`

Run the bot:  
`python main.py`