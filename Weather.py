from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

start = datetime(2018, 1, 1)
end = datetime(2018, 12, 31)

location = Point(49.2497, -123.1193, 70)

data = Daily(location, start, end)
data = data.fetch()

data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()