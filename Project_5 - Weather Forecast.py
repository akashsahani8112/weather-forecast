from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title('Weather App')
root.geometry('900x500+300+200')
root.resizable(False, False)

def getWeather():
    city = text_field.get()
    geolocator = Nominatim(user_agent='geoapiExercises')
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime('%I:%M %p')

    clock.config(text=current_time)
    name.config(text='CURRENT WEATHER')

    #Weather
    api = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,'°'))
    c.config(text=(condition,'|', 'FEELS', 'LIKE', temp,'°'))

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)
    

#Search Box.
search_image = PhotoImage(file='D:\Pictures/Copy of search.png')
my_image = Label(image=search_image)
my_image.place(x=20, y=20)

text_field = tk.Entry(root, justify='center', width=17, font=('poppins', 25,'bold'), bg='#404040', fg='white')
text_field.place(x=50, y=40)
text_field.focus()

search_icon = PhotoImage(file='D:\Pictures/Copy of search_icon.png')
my_image_icon = Button(image=search_icon, borderwidth=0, cursor='hand2', bg='#404040', command=getWeather)
my_image_icon.place(x=400, y=32)

#Logo Bar.
logo_image = PhotoImage(file='D:\Pictures/Copy of logo.png')
my_image_logo = Label(image=logo_image)
my_image_logo.place(x=150, y=100)

#Bottom Box.
frame_image = PhotoImage(file='D:\Pictures/Copy of box.png')
my_image_frame = Label(image=frame_image)
my_image_frame.pack(padx=5, pady=5, side=BOTTOM)

#Time
name = Label(root, font=('arial', 15, 'bold'))
name.place(x=30, y=100)

clock = Label(root, font=('Helvetica', 20))
clock.place(x=30, y=130)

#Label.

label_1 = Label(root, text='WIND', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label_1.place(x=120, y=400)

label_2 = Label(root, text='HUMIDITY', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label_2.place(x=250, y=400)

label_3 = Label(root, text='DESCRIPTION', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label_3.place(x=430, y=400)

label_4 = Label(root, text='PRESSURE', font=('Helvetica', 15, 'bold'), fg='white', bg='#1ab5ef')
label_4.place(x=650, y=400)


t = Label(font=('arial', 70, 'bold'), bg='#1ab5ef')
t.place(x=400, y=150)

c = Label(font=('arial', 15, 'bold'))
c.place(x=400, y=250)

w = Label(text='....', font=('arial', 20, 'bold'), bg='#1ab5ef')
w.place(x=120, y=430)

h= Label(text='....', font=('arial', 20, 'bold'), bg='#1ab5ef')
h.place(x=280, y=430)

d= Label(text='....', font=('arial', 20, 'bold'), bg='#1ab5ef')
d.place(x=430, y=430)

p= Label(text='....', font=('arial', 20, 'bold'), bg='#1ab5ef')
p.place(x=690, y=430)

root.mainloop()
