from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily
from flask import Flask, render_template, request

app = Flask(__name__)

def SetCoordinates(lat, lon):
    return Point(lat, lon)

def GetMinTemp(data):
    min_temp = 99
    for index, row in data.iterrows():
        if row['tmin'] < min_temp:
            min_temp = row['tmin']
    return min_temp

def GetMaxTemp(data):
    max_temp = -200
    for index, row in data.iterrows():
        if row['tmax'] > max_temp:
            max_temp = row['tmax']
    return max_temp

def SubNCount(data : Daily, n : int):
    count = 0
    for index, row in data.iterrows():
        if row['tmin'] < n or row['tmax'] < n:
            count += 1
    return count

def SuperNCount(data : Daily, n : int):
    count = 0
    for index, row in data.iterrows():
        if row['tmax'] > n or row['tmin'] > n:
            count += 1
    return count

def SetDate(date):
    return datetime(int(date[0:4]), int(date[5:7]), int(date[8:]))



@app.route('/', methods=['GET', 'POST'])

def index():
    result = None
    if request.method == 'POST':
        try:
            start_date = SetDate(request.form['start_date'])
            end_date = SetDate(request.form['end_date'])
            lat = float(request.form['latitude'])
            lon = float(request.form['longitude'])
            option = int(request.form['option'])
            x = request.form.get('x', type=float)

            location = SetCoordinates(lat, lon)
            data = Daily(location, start_date, end_date).fetch()

            if option == 1:
                result = f"The maximum temperature between {start_date} and {end_date} is {GetMaxTemp(data)} °C."
            elif option == 2:
                result = f"The minimum temperature between {start_date} and {end_date} is {GetMinTemp(data)} °C."
            elif option == 3 and x is not None:
                result = f"There are {SubNCount(data, x)} days below {x} °C."
            elif option == 4 and x is not None:
                result = f"There are {SuperNCount(data, x)} days above {x} °C."
        except Exception as e:
            result = f"An error occurred: {e}"
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)