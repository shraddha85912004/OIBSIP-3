from tkinter import *
from tkinter import messagebox
import requests
from PIL import Image
from datetime import datetime

root=Tk()
root.title("Weather Forecast App")
root.configure(bg="Light blue")
root.geometry("500x500")

def get_weather():
    city=cityentry.get()
    api_key='ca563036662a1af33997855eff2fb74b'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        temp=data['main']['temp']-273.15
        humidity=data['main']['humidity']
        pressure=data['main']['pressure']
        wind=(data['wind']['speed'])*3.6
        epoch_time=data['dt']
        date_time=datetime.fromtimestamp(epoch_time)
        desc=data['weather'][0]['description']
        cloudy=data['clouds']['all']
        
        timelbl.config(text=str(date_time))
        tempenter.insert(0,'{:.2f}'.format(temp) + "celcius")
        pressureenter.insert(0,str(pressure) + "hPa")
        humidenter.insert(0,str(humidity) + " %")
        windenter.insert(0,'{:.2f}'.format(wind) + "km/h")
        cloudenter.insert(0,str(cloudy) + " %")
        descenter.insert(0,str(desc))
    else:
        messagebox.showerror("Error","City Not Found. Enter a vald city name")
        cityentry.delete(0,END)
def reset():
    cityentry.delete(0,END)
    tempenter.delete(0,END)
    pressureenter.delete(0,END)
    humidenter.delete(0,END)
    windenter.delete(0,END)
    cloudenter.delete(0,END)
    descenter.delete(0,END)
    timelbl.config(text='')
        
title=Label(root,text="Weather detection",font=('bold',12),bg="Light Blue")
citylabel=Label(root,text="Enter city name:",font=('bold',12),bg="Light Blue")
cityentry=Entry(root,width=20,font=12)
timelbl=Label(root,text='',font=('bold',12),bg="Light Blue")

submitbtn=Button(root,text="Get weather",command=get_weather)

resetbtn=Button(root,text="Reset",command=reset)

templbl=Label(root,text="Temperature: ",font=('bold',12),bg="Light Blue")
pressurelbl=Label(root,text="Pressure: ",font=('bold',12),bg="Light Blue")
humidlbl=Label(root,text="Humidity: ",font=('bold',12),bg="Light Blue")
windlbl=Label(root,text="Wind: ",font=('bold',12),bg="Light Blue")
cloudinesslbl=Label(root,text="Cloudiness: ",font=('bold',12),bg="Light Blue")
desclbl=Label(root,text="Desc: ",font=('bold',12),bg="Light Blue")

tempenter=Entry(root,width=20,font=11)
pressureenter=Entry(root,width=20,font=11)
humidenter=Entry(root,width=20,font=11)
windenter=Entry(root,width=20,font=11)
cloudenter=Entry(root,width=20,font=11)
descenter=Entry(root,width=20,font=11)

title.grid(row=0,column=1)
timelbl.grid(row=1,column=2)
submitbtn.grid(row=2,column=1,pady=4)
templbl.grid(row=3,column=0,padx=4,pady=4)
pressurelbl.grid(row=4,column=0,padx=4,pady=4)
humidlbl.grid(row=5,column=0,padx=4,pady=4)
windlbl.grid(row=6,column=0,padx=4,pady=4)
cloudinesslbl.grid(row=7,column=0,padx=4,pady=4)
desclbl.grid(row=8,column=0,padx=4,pady=4)

citylabel.grid(row=1,column=0,padx=4,pady=4)
cityentry.grid(row=1,column=1,padx=4,pady=4)
tempenter.grid(row=3,column=1,padx=4,pady=4)
pressureenter.grid(row=4,column=1,padx=4,pady=4)
humidenter.grid(row=5,column=1,padx=4,pady=4)
windenter.grid(row=6,column=1,padx=4,pady=4)
cloudenter.grid(row=7,column=1,padx=4,pady=4)
descenter.grid(row=8,column=1,padx=4,pady=4)
resetbtn.grid(row=9,column=1,pady=4)

root.mainloop()

