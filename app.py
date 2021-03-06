from flask import Flask, request, jsonify
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(__name__)
FlaskJSON(app)

from sense_energy import Senseable
import json

sense = Senseable()
sense.authenticate("username", password")
sense.update_realtime()
sense.update_trend_data()


@app.route('/fart', methods=['GET','POST'])
def foo():

    varActive =  ("Active:", sense.active_power, "W")
    varActiveSolar = ("Active Solar:", sense.active_solar_power, "W")
    varDaily = ("Daily:", sense.daily_usage, "KWh")
    varDailySolar = ("Daily Solar:", sense.daily_production, "KWh")
    varActiveDevices = ("Active Devices:",", ".join(sense.active_devices))
    
    solar_deets = {
    'active' : varActive ,
    'active-solar' : varActiveSolar ,
    'daily' : varDaily ,
    'daily-solar' : varDailySolar ,
    'active-device' : varActiveDevices
}
    data = request.args.get(solar_deets)
    return jsonify(data)

@app.route('/get_active')
def get_active ():
 
    varActive =  ("Active:", sense.active_power, "W")

    return json_response(active=varActive)

@app.route('/get_activesolar')
def get_activesolar():

    varActiveSolar = ("Active Solar:", sense.active_solar_power, "W")

    return json_response(activesolar=varActivesolar)

@app.route('/get_daily')
def get_daily ():
 
    varDaily = ("Daily:", sense.daily_usage, "KWh")

    return json_response(daily=varDaily)

@app.route('/get_dailysolar')
def get_dailysolar ():
 
    varDailySolar = ("Daily Solar:", sense.daily_production, "KWh")

    return json_response(dailysolar=varDailySolar)

@app.route('/get_activedevices')
def get_activedevices ():
 
    varActiveDevices = ("Active Devices:",", ".join(sense.active_devices))

    return json_response(activedevices=varActiveDevices)
