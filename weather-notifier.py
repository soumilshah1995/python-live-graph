import requests
import datetime
import smtplib
from email.mime.text import MIMEText





city= "Bridgeport"

def weather_data():


    url='http://api.openweathermap.org/data/2.5/weather?appid=ce45a4d1079e68c410cd42a3054d00e1&q='
    new_url=url+ city
    data=requests.get(new_url).json()


    longitude= data["coord"]["lon"]
    latitude= data["coord"]["lat"]


    wind_speed= data["wind"]["speed"]


    sunrise_timestamp= data["sys"]["sunrise"]
    sunrise_time= time_stamp(sunrise_timestamp)

    sunset_timestamp= data["sys"]["sunset"]
    sunset_time= time_stamp(sunset_timestamp)


    pressure= data["main"]["pressure"]
    date= data["dt"]
    date_updated= time_stamp(date)

    text='''
    City                    :{0} 
    weather Report          :{1}
    Latitude                :{2}
    longitude               :{3}
    Windspeed               :{4}
    SunRise                 :{5}
    SunSet                  :{6}
    Date                    :{7}
    Pressure                :{8}
    
    
    
    
    
    '''.format(city,test(),latitude,longitude,wind_speed,sunrise_time,sunset_time,date_updated,pressure)
    return text




def test():
    url='http://api.openweathermap.org/data/2.5/weather?appid=ce45a4d1079e68c410cd42a3054d00e1&q='
    new_url=url+ "Bridgeport"
    data=requests.get(new_url).json()
    for x in data["weather"]:
        description= x["description"]
        main= x["main"]
    return main+description



def time_stamp(number):
    date_time= datetime.datetime.fromtimestamp(int(number)).strftime('%Y-%m-%d %H:%M:%S')
    return date_time




def email():

    # define content
    recipients = ["Sender Email"]
    sender = "Your Email"
    subject = "Weather update"
    body = weather_data()

    # make up message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)

# sending
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login('YOUR EMAIL ID', 'PASSWORD')
    send_it = session.sendmail(sender, recipients, msg.as_string())
    session.quit()

email()

