# Deploying FastAPI and PostgreSQL to AWS Elastic Beanstalk

To run this project fisrt meet the prerequisites:
- Install and configure the [AWS CLI](https://aws.amazon.com/cli/)
- Install the [Pulumi CLI](https://www.pulumi.com/docs/get-started/aws/begin/)


## Getting started

Navigate to the infrastructure folder:  
`cd infrastructure`

Secrets are encrypted per stack, so can't be re-used.  
Re-set the secret:  
`pulumi config set --secret db_password mysuperpassword`  
When prompted, press enter to create a new stack  
Then provide a name for the stack - I went with `dev`  

This will override the db password in the config file, but leave the region and username values in place

Run the deployment:  
`pulumi up`  
Choose yes when prompted, then wait for the deployment to complete - this took around 7 minutes for me  


From the app folder select:
- `alembic/`
- `src/`
- `alembic.ini`
- `application.py`
- `Procfile`
- `requirements.txt`
Add those to a zip file  

Open the AWS console in a browser and navigate to Elastic Beanstalk  
Select your new environment, and click the deploy button  
Use the file select to select your zip folder, and give it a sensible version such as `0.1`  
Wait for the deployment to complete, this can take several minutes  

Once done, the app is deployed and ready to use


