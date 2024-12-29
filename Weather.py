from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily




location = Point(42.7370, -84.4839)

data = Daily(location, start, end)
data = data.fetch()


def SetCoordinates(lat, lon):
    return Point(lat, lon)

def GetMinTemp(data):
    return min(data.row['tmin'])

def GetMaxTemp(data):
    return max(data.row['tmax'])

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



def main():
    start = SetDate(input("Start Date (YYYY/MM/DD):\n"))
    end = SetDate(input("Start Date (YYYY, MM, DD):\n"))
    print(start, end)
    


if __name__ == "__main__":
    main()