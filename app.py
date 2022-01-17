# URL to Canvas page: https://courses.bootcampspot.com/courses/976/pages/9-dot-4-3-set-up-flask-and-create-a-route?module_item_id=358681
# URL to Canvas page #2: https://courses.bootcampspot.com/courses/976/pages/9-dot-5-1-set-up-the-database-and-flask?module_item_id=358685

# Python Magic Methods: https://www.geeksforgeeks.org/dunder-magic-methods-python/
# Flask: https://flask.palletsprojects.com/en/2.0.x/

# ---------------------------------------------------------------------------
# Call dependencies
# ---------------------------------------------------------------------------
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# ---------------------------------------------------------------------------
# End of: Call dependencies
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Setup Database Environment ------------------------------------------------
# ---------------------------------------------------------------------------
# Create Engine
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Set session variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Set Session
session = Session(engine)
# ---------------------------------------------------------------------------
# End: Setup Database Environment
# ---------------------------------------------------------------------------

# Create a Flask app
app = Flask(__name__)

# Define starting or root
@app.route('/')
def welcome():
    print('Accessing welcome page (Route)')
    return(
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        F"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        )

@app.route('/api/v1.0/precipitation')
def precitipation():
    print('Accessing Precipitation Route')
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route('/api/v1.0/stations')
def stations():
    print('Accessing Stations Route')
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

@app.route('/api/v1.0/tobs')
def temp_monthly():
    print('Accessing Tobs Route')
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

if __name__ == "__main__":
    app.run(debug=True)