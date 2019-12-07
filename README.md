# Easy-SMS-MSG91-Python-Script

This repo shows how to implement a Simple Python SMS Script to Heroku (http://heroku.com/). Send SMS from Python Script Via MSG91 API-> The Simple and Easy to Use Script.

To run this script clone this repo. You will need a MSG91 Account to run this Script. [Sign up](https://world.msg91.com/signup/?u3=PN) for a free account (you will get 100 Free Promotional SMS Credits) or [Login](https://control.msg91.com/signin/) if you already have a account on MSG91 then go to your dashboard then click on API Tab to get your credentials (AUTH KEY). Copy the Auth Key and paste it in the `sms.py` Script in authKey Variable.

```sh
    authKey = {YOUR MSG91 AUTH KEY}
```

#### Screenshot of MSG91 API Tab

![](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSTErY6SvJOCOOZyZnpd_goHGs8B-g8GGfE-y1ntNsAEpVuWzSl)

## Installation

### Requirements

  * Python 3.3+
  * macOS or Linux or Windows
    
### Dependencies

  * Flask
  * Requests
  * Gunicorn (Needed When you Deploy the Script on Heroku)
    
#### To Install the Dependencies: 

Run `pip install -r requirements.txt` in the Command Prompt.
After installing the Dependencies run `python sms.py` in Command Prompt (Only For Windows Users).

## How to Deploy on Heroku

```sh
$ git clone https://github.com/mohd-baquir-qureshi/Easy-SMS-MSG91.git
$ cd Easy-SMS-MSG91
$ git init
$ git add .
$ git commit -m "First Commit"
$ heroku create
$ git push heroku master
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Running Locally

Make sure you have Python 3.3+ [installed locally](https://www.python.org/downloads/).

```sh
$ git clone https://github.com/mohd-baquir-qureshi/Easy-SMS-MSG91.git
$ cd Easy-SMS-MSG91

$ pip install -r requirements.txt

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Usage Demo

#### To Run Locally

Syntax => http://localhost:5000/{SENDER ID}/{MOBILE NUMBER}/{MESSAGE}

Ex. => http://localhost:5000/PYTHON/8888888888/Hello%20Python

#### To Run After Deploying it on Heroku

Syntax => https://demo-app.herokuapp.com/{SENDER ID}/{MOBILE NUMBER}/{MESSAGE}

Ex. => https://demo-app.herokuapp.com/PYTHON/8888888888/Hello%20Python
