# import Flask
from flask import Flask, jsonify


#list of all routes
Climate_List = [
    {" "}
]






app = Flask(__name__)

#Denfine the index reoute
@app.route("/")
def home():
    """Return the Climate List as json"""
    return jsonify(Climate_variables)

@app.route("/welcome")
def welcome():
    return(
        f"Welcome to API<br>"
        f"Climate List API!,<br/>"
        f"Available route:precipitation<br/>"
        f"/api/vi.0/stations"
        f"/api/vi.0/tobs"
        f"/api/v1.0/<start> and </api/v1.0/<start>/<end>"
    )
@app.route("/api/v1.0/precipitation")
def Precipitation():
    prcp_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    
    year_prcp_data =list(np.ravel(resul)
    year_prcp_data  =[]
        row = {}
        row[Measurement.date] = row[Measurement.prcp]
        year_prcp_data.append(row)"""

    return jsonify(year_prcp)

@app.route("/api/v1.0/station")
def station():   
        
        result = session.query(Station.Sstation).all()

        all_stations= lst(np.ravel(resuls))

        return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():

        year_tobs =[]
        results = session.query(Measurements.tobs. filter(Measurements.date>="08-23-2017").all()

        year_tobs = list(np.ravel(results))
            result = session.query(func.min(Measurement.tobs),
                       func.max(Measurement.tobs),
                       func.avg(Measurement.tobs)).filter(Measurement.station == 'USC00519281').all()

        return Jsonify (year_tobs)

@app.route("/api/v1.0/<start>")
def start_trip_temp(start_date):

        start_trip =[]

    prev_year_start = dt.date(2018, 1, 1) - dt.timedelta(days=365)
prev_year_end = dt.date(2018, 1, 7) - dt.timedelta(days=365)

tmin, tavg, tmax = calc_temps(prev_year_start.strftime("%Y-%m-%d"), prev_year_end.strftime("%Y-%m-%d"))[0]
if __name__ == "__main__":
    app.run(debug=True)


