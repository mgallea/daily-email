# Daily Email Newsletter
A repository for a daily newsletter with functionality to customize the content you will receive.

Issues requests to [Open Weather API](https://openweathermap.org/api) and [NewsAPI](https://newsapi.org/docs/client-libraries/python) before parsing the data and posting to the [Sendgrid API](https://sendgrid.com/docs/API_Reference/api_v3.html) to be sent to the user.

## Prerequisites
  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation
Fork this repository under your own control and then clone the resulting repo onto your computer. Use Anaconda to create a new virtual environment and install the package dependencies listed in Requirements.txt:

```sh
pip install -r requirements.txt
```

## .env Setup
To ensure that this application will work as desired, you need to create a .env file. This file will need to include the following content:

```js
SENDGRID_API_KEY=""
MY_EMAIL_ADDRESS=""
NEWS_API_KEY=""
SENDGRID_TEMPLATE_ID=""
OPENWEATHER_API_KEY=""
```

## Uploading Templates to Sendgrid
In the repo, there is a file called "templates/email_template.html" . This is the dynamically generated email that wil be used to create the email on Sendgrid's serers. You will need to create a [Dynamic Transactional Template](https://sendgrid.com/docs/ui/sending-email/how-to-send-an-email-with-dynamic-transactional-templates/) on Sendgrid's Web App and copy and paste the contents of this file into that template.

## Testing
Once you have installed all the required packages, you will need to run the tests included with the application. This can be done by entering the root directory of the repo and running the following command:

```sh
pytest
```

Once all tests have successfully passed, you can begin running the application and sending yourself a daily email.

## Running Locally
Run the script with the following command from the root directory:

```sh
python app/main.py
```

## Running on Heroku
If you do not currently have it installed, [install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install), and make sure you can login and list your applications.

```sh
heroku login

heroku apps:list
```
Once you have logged into Heroku, you will need to navigate to your local repo and create a new application.

```sh
heroku apps:create <<<INSERT APPLICATION NAME>>>
```
You will then need to associate this git repo with the Heroku Server. This can be done with the following command:

```sh
heroku git:remote -a <<<APPLICATION NAME ON HEROKU>>>
```
You will then need to set the environment variables via the Dashboard on the Heroku Web Interface. These are the same variables that would be in your .env file.

Finally, you will need to deploy the script to Heroku using the following command:

```sh
git push heroku master
```
To ensure you receive an email every day (or as often as you would like), you can use the free tool [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler) to ensure this script runs at particular times.

Once you have provisioned Heroku Scheduler for your application from the Heroku Web Dashboard, click on the provisioned "Heroku Scheduler" resource from the "Resources" tab, then click to "Add a new Job". When adding the job, choose to execute the script at a scheduled interval, and finally click to "Save" the job
