from datetime import datetime
from meteostat import Point, Daily


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


def SubNCount(data: Daily, n: int):
    count = 0
    for index, row in data.iterrows():
        if row['tmin'] < n or row['tmax'] < n:
            count += 1
    return count


def SuperNCount(data: Daily, n: int):
    count = 0
    for index, row in data.iterrows():
        if row['tmax'] > n or row['tmin'] > n:
            count += 1
    return count


def SetDate(date):
    return datetime(int(date[0:4]), int(date[5:7]), int(date[8:]))



def main():
    start = SetDate(input("Start Date (YYYY/MM/DD): "))
    end = SetDate(input("\nEnd Date (YYYY/MM/DD): "))
    lat = int(input("\nInput latitudinal coordinate: "))
    lon = int(input("\n Input longitudinal coordinate: "))
    location = SetCoordinates(lat, lon)
    data = Daily(location, start, end)
    data = data.fetch()
    while True:
        print("\nChoose option: \n1. Get Max Temperature \n2. Get Minimum Temperature\
            \n3. Get Temperatures below X \n4. Get Temperatures above X \n5. Exit \n")
        value = int(input())
        if value == 1:
            print(f"The maximum temperature in the selected timeframe and zone is {GetMaxTemp(data)} degrees celsius.")
            continue
        elif value == 2:
            print(f"The lowest temperature in the selected timeframe and zone is {GetMinTemp(data)} degrees celsius.")
            continue
        elif value == 3:
            x = int(input("Input a number X: "))
            print(f"In the selected timeframe and zone, there were {SubNCount(data, x)} days below {x} degrees celsius!")
        elif value == 4:
            x = int(input("Input a number X: "))
            print(f"In the selected timeframe and zone, there were {SuperNCount(data, x)} days above {x} degrees celsius!")
        elif value == 5:
            break
        else:
            print("Not a valid value, please try again.\n")
            continue


if __name__ == "__main__":
    main()
