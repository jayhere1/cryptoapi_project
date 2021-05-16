<p align="center">
  <img width="150" src="https://user-images.githubusercontent.com/23463810/115998709-76d72280-a5e0-11eb-9759-9b352298c1e3.png">
</p>

# cryptoapi_project

Can be accessed on https://cryptoapiproject.herokuapp.com/ or https://flask-app-crypto.nw.r.appspot.com/

This project uses the Alpha vantage API to query data for any single cryptocurrency (Currently set to Ethereum), converts to pandas dataframe, removes metadata and historical data, extracts the data for current date and displays this.

To query information about a different currency, change variables in params.ini and rerun the code.

Code: app.py

Resources used: Python, Flask, Jinja2, HTML, CSS, gunicorn, Heroku, Google App Engine

Libraries: Pandas, Requests, Flask.

Modules: os, datetime.
