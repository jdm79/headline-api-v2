from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask import Flask
from flask import jsonify
from flask_cors import CORS
import json
import datetime
import time
import random
import requests
from requests import get
from datetime import date
from bs4 import BeautifulSoup
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://9e7fb37583514ba3b9f13afb0ba70df1@o400717.ingest.sentry.io/5259365",
    integrations=[FlaskIntegration()]
)

app = FlaskAPI(__name__)
CORS(app)

@app.route("/headlines", methods=['GET'])
def headlines_list():  
  with open(f"headlines.py", 'r') as f:
    headlines = f.read()

  return headlines


if __name__ == "__main__":
    app.run(debug=True)