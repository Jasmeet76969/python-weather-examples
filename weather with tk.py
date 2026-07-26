import tkinter as tk
from tkinter import messagebox
import requests
from tkinter import*

def get_weather():
    city1=city_entry.get()
    api_key=""
    url="https://api.openweathermap.org/data/2.5/weather?"
    complete_url=url+"appid="+api_key+"&q="+city1
    res=requests.get(complete_url)
    data=res.json()
    humidity=data['main']['humidity']
    pressure=data['main']['pressure']
    wind=data['wind']['speed']
    description=data['weather'][0]['description']
    temp=data['main']['temp']

    print('Temperature:',temp,'K')
    print('wind:',wind)
    print('Pressure:',pressure)
    print('Humidity:',humidity)
    print('Description:',description)


master=Tk()
Label(master,text="City Name:").grid(row=0)
city_entry=Entry(master)

city_entry.grid(row=0,column=1)
Button(master,text="get_weather",command=get_weather).grid(row=0,column=2,sticky=W,pady=4)
mainloop()
