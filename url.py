'''
Soumil Nitin Shah

B.E in Electronic
MS Electrical Engineering
MS  Computer Engineering

'''

import requests
import datetime
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from  matplotlib import style

x_axis=[]
y_axis=[]




def get_time():
    time_z=datetime.datetime.now()
    minutes=time_z.minute
    sec=time_z.second
    hr=time_z.hour
    my_timee=str(hr)+":"+ str(minutes) + ":" + str(sec)

    x_axis.append(my_timee)
    return my_timee


def currency():
    url="https://api.thingspeak.com/apps/thinghttp/send_request?api_key=08UQVZQRNZHZSMNE"
    data=requests.get(url).json()
    y_axis.append(data)
    return data




def weather_data():
    url= 'http://api.openweathermap.org/data/2.5/weather?appid=ce45a4d1079e68c410cd42a3054d00e1&q=London,uk'
    data=requests.get(url).json()
    timestamp=data["sys"]["sunset"]
    print(time_stampconversion(timestamp))


def time_stampconversion(number):
    val= datetime.datetime.fromtimestamp(int(number)).strftime('%Y-%m-%d %H:%M:%S')
    return val



fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)



def animate(i):
    currency()
    get_time()

    ax1.clear()
    ax1.plot(x_axis,y_axis)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()