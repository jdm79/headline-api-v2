from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask import Flask
from flask import jsonify
from flask_cors import CORS
import requests
from requests import get

dummydata = [
  {"paper": "Daily mirror", "headline": "Boris tries to save Dominic Cummings' job by declaring 'it's not like he was visiting a lover' as maverick ally is accused of visiting parents' Durham home a SECOND time and breaking lockdown rules by 'strolling in bluebell wood' with his wife"},
  {"paper": "The Independent", "headline": "Boris tries to save Dominic Cummings' job by declaring 'it's not like he was visiting a lover' as maverick ally is accused of visiting parents' Durham home a SECOND time and breaking lockdown rules by 'strolling in bluebell wood' with his wife"},
  {"paper": "Daily Mail", "headline": "Boris tries to save Dominic Cummings' job by declaring 'it's not like he was visiting a lover' as maverick ally is accused of visiting parents' Durham home a SECOND time and breaking lockdown rules by 'strolling in bluebell wood' with his wifeTrump heads to golf course as US coronavirus death toll nears 100,000"},
  {"paper": "Daily Mirror", "headline": "Trump heads to golf courBoris tries to save Dominic Cummings' job by declaring 'it's not like he was visiting a lover' as maverick ally is accused of visiting parents' Durham home a SECOND time and breaking lockdown rules by 'strolling in bluebell wood' with his wifese as US coronavirus death toll nears 100,000"},
  {"paper": "Financial Times", "headline": "Trump Boris tries to save Dominic Cummings' job by declaring 'it's not like he was visiting a lover' as maverick ally is accused of visiting parents' Durham home a SECOND time and breaking lockdown rules by 'strolling in bluebell wood' with his wife to golf course as US coronavirus death toll nears 100,000"},
  {"paper": "Evening Standard", "headline": "Trump Boris tries to save Dominic Cummings' job by declaring 'it's not like he was visiting a lover' as maverick ally is accused of visiting parents' Durham home a SECOND time and breaking lockdown rules by 'strolling in bluebell wood' with his wife to golf course as US coronavirus death toll nears 100,000"},
  {"paper": "Daily Express", "headline": "Trump heads tBoris tries to save Dominic Cummings' job by declaring 'it's not like he was visiting a lover' as maverick ally is accused of visiting parents' Durham home a SECOND time and breaking lockdown rules by 'strolling in bluebell wood' with his wifeo golf course as US coronavirus death toll nears 100,000"},
  {"paper": "The i", "headline": "Trump heads to golf course as US coronavirus death toll nears 100,000"},
  {"paper": "Metro", "headline": "Trump heads to golfBoris tries to save Dominic Cummings' job by declaring 'it's not like he was visiting a lover' as maverick ally is accused of visiting parents' Durham home a SECOND time and breaking lockdown rules by 'strolling in bluebell wood' with his wife course as US coronavirus death toll nears 100,000"},
  {"paper": "Daily Star", "headline": "Trump heads to golf course as US coronavirus death toll nears 100,000"},
  {"paper": "The Sun", "headline": "Boris tries to save Dominic Cummings' job by declaring 'it's not like he was visiting a lover' as maverick ally is accused of visiting parents' Durham home a SECOND time and breaking lockdown rules by 'strolling in bluebell wood' with his wifeTrump heads to golf course as US coronavirus death toll nears 100,000  nic Cummings' job by declaring 'it's not like he was visiting a lover' as maverick ally is accused of visiting parents' Durham home a SECOND time and breaking lockdown rules by 'strolling in bluebell wood' with his wifeTrump heads to golf course as US coronavirus death toll nears 100,000  "},
  {"paper": "Morning Star", "headline": "Trump heads to golf course as US coronavirus death toll nears 100,000"},
  {"paper": "Irish Sun", "headline": "Trump heads to golf course as US coronavirus death toll nears 100,000"},
  {"paper": "The Scotsman", "headline": "Trump Boris tries to save Dominic Cummings' job by declaring 'it's not like he was visiting a lover' as maverick ally is accused of visiting parents' Durham home a SECOND time and breaking lockdown rules by 'strolling in bluebell wood' with his wife to golf course as US coronavirus death toll nears 100,000"},
  {"paper": "Telegraph", "headline": "Trump heads to golf course as US coronavirus death toll nears 100,000"},
  {"paper": "Times", "headline": "Boris tries to save Dominic Cummings' job by declaring 'it's not like he was visiting a lover' as maverick ally is accused of visiting parents' Durham home a SECOND time and breaking lockdown rules by 'strolling in bluebell wood' with his wife"},
]


# the Route(s)
app = FlaskAPI(__name__)
CORS(app)

@app.route("/test", methods=['GET'])

def headlines_list():
   
  scraped_headlines = dummydata

  return jsonify(scraped_headlines)
    
if __name__ == "__main__":
    app.run(debug=True)