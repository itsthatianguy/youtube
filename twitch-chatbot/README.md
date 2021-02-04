# Twitch Chatbot

## Getting Started

First get a TMI token here: https://twitchapps.com/tmi/  
And register your bot as an app to get your client id here: https://dev.twitch.tv/console/apps/create  

Set up environment variables for your client ID, secret, and your TMI token

Update the nick and channel values in the script to match the account and chanel you're using.

Set up a virtual environment for the project:  
`python3 -m venv virtualenv`

Activate the environment:  
`source virtualenv/bin/activate`

Install the dependencies:  
`pip install -r requirements.txt`

Run the bot:  
`python main.py`
