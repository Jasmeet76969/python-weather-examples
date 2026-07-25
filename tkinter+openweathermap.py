import tkinter as tk
from tkinter import messagebox
import requests

API_KEY="42412a71ec9331ab7c1e04fec97602d3"

def get_weather():
    city=city_entry.get()
    if city=="":
        messagebox.showerror("Error","Please enter a city name")
        return
    url=f"https://api.openweathermap.org/data/2.5/weather?"q={city}&appid={API_KEY}&units=metric"
    try:
        response=requests.get(url)
        data=response.json()
        if data["cod"]!=200:
            messagebox.showerror("Error","City not found")
            return
        city_name=data["name"]
        country=data["sys"]["country"]
        temp=data["main"]["temp"]
        feels=data["main"]["feels_like"]
        humidity=data["main"]["humidity"]
        pressure=data["main"]["pressure"]
        weather=data["weather"][0]["description"]
        wind=data["wind"]["speed"]
        result=f"""city:{city_name},{country}
Temperature:{temp}°C
Feels like:{feels}°C
Weather:{weather.title()}
Humidity:{humidity}%
Pressure:{pressure}hPa
Wind Speed:{wind}m/s
"""
        result_label.config(text=result)
    except Exception as e:
        messagebox.showerror("Error",str(e))
root=tk.Tk()
root.title("Weather App")
root.geometry("450x400")
root.config(bg="lightblue")
#heading
title=tk.Label(root, text="openweathermap", font=("Arial",18,"bold"), bg="pink")
title.pack(pady=10)
#input frame
frame = tk.Frame(root, bg="pink")
frame.pack(pady=10)
tk.Label(frame, text="Enter City=", font=("Arial",12), bg="pink").pack(side=tk.LEFT,padx=5)
city_entry=tk.Entry(frame, font=("Arial",12),width=20)
city_entry.pack(side=tk.LEFT,padx=5)

btn=tk.Button(root,text="Get Weather",font=("Arial",12,"bold"),bg="green",fg="white",command=get_weather)
btn.pack(pady=10)
result_label=tk.Label(root,text="",font=("Arial",12),bg="white",justify="left",anchor="nw",width=40,height=12,relief="solid")
result_label.pack(padx=20,pady=10,fill="both",expand=True)
root.mainloop()
