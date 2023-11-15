# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine('sqlite:///resources/hawaii.sqlite').connect()

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with = engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes"""
    return(
        f"Welcome to the Hawiian Climate Analysis API!"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitaion<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )


@app.route("/api/v1.0/precipitaion")
def percipitation():
    session = Session(engine)

    """Return a list of all percipitation and date """

    base_year = dt.date(2017, 8, 23)-dt.timedelta(days = 365)
    prev_last_date = dt.date(base_year.year, base_year.month, base_year.day)

    scores = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_last_date).order_by(Measurement.date).all()

    session.close()

    all_precipitation = []
    for date, prcp in scores:
        precipitation_dict = {}
        precipitation_dict[date] = prcp
        all_precipitation.append(precipitation_dict)

    return jsonify(all_precipitation)
   
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    results = [Station.id, Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation]
    query_result = session.query(*results).all()
    
    session.close()

    stations = []
    for id, station, name, lat, lon, el in query_result:
        station_dict = {}
        station_dict["Id"] = id
        station_dict["Station"] = station
        station_dict["Name"] = name
        station_dict["Lat"] = lat
        station_dict["Lon"] = lon
        station_dict["Elevation"] = el
        stations.append(station_dict)

    return jsonify(stations)




@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    """Return a list of all temperature observations"""

    query_result = session.query( Measurement.date, Measurement.tobs).filter(Measurement.station=='USC00519281').\
        filter(Measurement.date>='2016-08-23').all()

    temperatures = []
    for tobs, date in query_result:
        tobs_dict = {}
        tobs_dict["date"] = tobs
        tobs_dict["tobs"] = date
        temperatures.append(tobs_dict)
    
    return jsonify(temperatures)     

@app.route("/api/v1.0/<start>")
def get_temps_start(start):
    session = Session(engine)

    """start_date (string) is a date in the format of YYYY-MM-DD."""

    # start = ''

    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
               filter(Measurement.date >= start).all()
   
    session.close()
    
    temps = {}
    temps["Minimum Temperature"] = results[0][0]
    temps["Average Temperature"] = results[0][1]
    temps["Maximum Temperature"] = results[0][2]

    return jsonify(temps)

@app.route("/api/v1.0/<start>/<end>")
def get_temps_start_end(start, end):
    session = Session(engine)

    """start_date (string) is a date in the format of YYYY-MM-DD.
       end_date (string) is a date in the format of YYYY-MM-DD."""

    # start = ''
    # end = ''
    
    results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
              filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    session.close()
    
    temps = {}
    temps["Minimum Temperature"] = results[0][0]
    temps["Average Temperature"] = results[0][1]
    temps["Maximum Temperature"] = results[0][2]
    
    return jsonify(temps)


if __name__ == '__main__':
    app.run(debug=True)
