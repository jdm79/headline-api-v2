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

from scraper import print_headlines

# print_headlines()



app = FlaskAPI(__name__)
CORS(app)

@app.route("/headlines", methods=['GET'])
def headlines_list():  
  # print_headlines()

  with open(f"headlines.py", 'r') as f:
    headlines = f.read()

  return headlines


if __name__ == "__main__":
    app.run(debug=True)