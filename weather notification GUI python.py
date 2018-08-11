import requests
import datetime
import smtplib
from email.mime.text import MIMEText
import tkinter

mainwindow = tkinter.Tk()
mainwindow.title("Weather API")
mainwindow.resizable(0, 0)
mainwindow.configure(background='grey')


label = tkinter.Label(mainwindow, text="Enter City",background="orange",fg="Black")
label.grid(row=0, column=0,sticky= "NENSSESW")

cityValue = tkinter.StringVar()
e = tkinter.Entry(mainwindow,textvariable=cityValue)
e.grid(row=0, column=1,sticky= "NENSSESW")



button = tkinter.Button(mainwindow, text="Submit",background="Black",fg="White", command=lambda: weather_data())
button.grid(row=1, column=0, columnspan=2,sticky= "NENSSESW")

datalabel= tkinter.Label(mainwindow)
datalabel.grid(row=2, column=0,sticky= "NENSSESW",columnspan=2)

label_your_email=tkinter.Label(mainwindow,text="Enter your Email Id",background="Orange")
label_your_email.grid(row=3,column=0,sticky= "NENSSESW")

u_mail=tkinter.StringVar()
entry_your_email= tkinter.Entry(mainwindow,textvariable=u_mail)
entry_your_email.grid(row=3,column=1,sticky= "NENSSESW")


label_password=tkinter.Label(text="Enter your Password",background="orange")
label_password.grid(row=4,column=0,sticky= "NENSSESW")

u_pass= tkinter.StringVar()
enter_password=tkinter.Entry(mainwindow,textvariable=u_pass)
enter_password.grid(row=4,column=1,sticky= "NENSSESW")



label_sender_email=tkinter.Label(text="Enter Sendser Email:",background="orange")
label_sender_email.grid(row=5,column=0,sticky= "NENSSESW")

u_sendmail= tkinter.StringVar()
entry_sender_email=tkinter.Entry(mainwindow,textvariable=u_sendmail)
entry_sender_email.grid(row=5,column=1,sticky= "NENSSESW")



button_submit=tkinter.Button(mainwindow,background="Black",fg="White",text="Submit Report",command=lambda:email())
button_submit.grid(row=6,column=0,columnspan=2,sticky= "NENSSESW")



def weather_data():
    city = str(e.get())
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=ce45a4d1079e68c410cd42a3054d00e1&q='
    new_url = url + cityValue.get()
    print(new_url)

    data = requests.get(new_url).json()
    print(data)

    if(data['cod']=='404'or data['cod']=='400'):
        print('City Not Found')
        datalabel.configure(text='City Not Found')
        return

    longitude = data["coord"]["lon"]
    latitude = data["coord"]["lat"]

    wind_speed = data["wind"]["speed"]

    sunrise_timestamp = data["sys"]["sunrise"]
    sunrise_time = time_stamp(sunrise_timestamp)

    sunset_timestamp = data["sys"]["sunset"]
    sunset_time = time_stamp(sunset_timestamp)

    pressure = data["main"]["pressure"]
    date = data["dt"]
    date_updated = time_stamp(date)

    text = '''
    weather Report                                       :{1}
    Latitude                                             :{2}
    longitude                                            :{3}
    Windspeed                                            :{4}
    SunRise                                              :{5}
    SunSet                                               :{6}
    Date                                                 :{7}
    Pressure                                             :{8}
    '''.format(city, test(), latitude, longitude, wind_speed, sunrise_time, sunset_time, date_updated, pressure)
    datalabel.configure(text = text)
    return text



def test():
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=ce45a4d1079e68c410cd42a3054d00e1&q='
    new_url = url + "Bridgeport"
    data = requests.get(new_url).json()
    for x in data["weather"]:
        description = x["description"]
        main = x["main"]
    return main + description



def time_stamp(number):
    date_time = datetime.datetime.fromtimestamp(int(number)).strftime('%Y-%m-%d %H:%M:%S')
    return date_time


def email():
    u_mail=str(entry_your_email.get())
    u_pass=str(enter_password.get())
    u_sendmail=str(entry_sender_email.get())


    # define content
    recipients = u_sendmail #SENDER TO SEND
    sender = u_mail # YOUR EMAIL
    subject = "Weather update"
    body = weather_data()
    print("BODY is {}".format(body))

    # make up message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)

    # sending
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(u_mail, u_pass)
    send_it = session.sendmail(sender, recipients, msg.as_string())
    session.quit()


mainwindow.mainloop()
