from tkinter import *
import requests
import datetime as dt



def cityinfo(weatherinfo):
    try:
        error["text"] = " " 
        cityname = weatherinfo["name"]
        country = weatherinfo["sys"]["country"]
        info_desc = weatherinfo["weather"][0]["description"]
        temperature = weatherinfo["main"]["temp"]
        pressure = weatherinfo["main"]["pressure"]      
        humid = weatherinfo["main"]["humidity"]  

        city["text"] = "City: " + cityname + ", " + country
        descr["text"] = "Cloudiness: " + info_desc
        temp["text"] = "Temperature: " + str(int(temperature)) + "°C"
        press["text"] = "Pressure: " + str(int(pressure)) + "hpa"      
        humidity["text"] = "Humidity:" + str(int(humid)) + "%"
    except:

        error["text"] = "Ocurrio un error al obtener los datos." 
     

def windinfo(citywind):
 
    try:
        windd = citywind["wind"]["speed"]
        grados = citywind["wind"]["deg"]
        infowindgus = citywind["wind"]["gust"]

        if grados > 327 or grados < 22:
            direction = "North Wind"          
        elif grados > 22 and grados < 67:
            direction = "Northeast Wind"
        elif grados > 67 and grados < 112:
            direction = "East Wind"
        elif grados > 113 and grados < 157:
            direction ="Southeast Wind"
        elif grados > 158 and grados < 202:
            direction= "South Wind"
        elif grados > 203 and grados < 248:
            direction = "Southwest Wind"
        elif grados > 249 and grados < 293:
            direction = "West Wind"
        elif grados > 294 and grados <= 326:
            direction = "Northwest Wind"
          
        wind["text"] = "Wind Speed: " + str(int(windd)) + "m/s"
        deg["text"] = direction, str(grados) + "°"
        gust["text"] = str(int(infowindgus))
    
    except:
        print("Ocurrio un error al obtener los datos del viento.")

def suninfo(citysun):
    try:       
        timezone = citysun["timezone"]
        sunrise = "Sunrise at:" + dt.datetime.utcfromtimestamp(citysun['sys']['sunrise'] + timezone).strftime('%H:%M:%S')
        sunset  = "Sunset at:" + dt.datetime.utcfromtimestamp(citysun["sys"]["sunset"] + timezone ).strftime('%H:%M:%S')
        
        #timezonee["text"] = timezone
        sunrisee["text"] = sunrise
        sunsett["text"] = sunset

    except:

        print("Ocurrio un error al intentar obtener los datos sol")

def weather_JSON(city):
    try:
        API_Key = "b578e711134b34b552823f4d322ef744"
        URL =  "https://api.openweathermap.org/data/2.5/weather"
        query = {"APPID": API_Key, "q": city, "units": "metric", "lang": "en"}
        response = requests.get(URL, params = query)
        weatherinfo = response.json()
        citywind = response.json()
        citysun = response.json()
        cityinfo(weatherinfo)
        windinfo(citywind)
        suninfo(citysun)

    except:
        print("Error")
        
windows = Tk()
windows.geometry("500x700")
windows.configure(bg="#5cc0de")
titulo = Label(font = ("arial",15, "normal"), text="Ingrese una ciudad o pais.", background="#5cc0de")
titulo.pack()

inputcity = Entry (windows, font=("arial", 12, "bold"),bd = 0, justify= "center")
inputcity.pack(padx=1, pady=1)

error = Label(font = ("arial",10, "bold"), background="#5cc0de", foreground="red")
error.pack(padx = 10, pady = 10)

buttongetcity = Button(windows, text = "Find Weather", font =("arial", 15, "normal"),background= "#114251",foreground = "#ffffff", bd = 0, command = lambda: weather_JSON(inputcity.get()))
buttongetcity.config(width=50, height=1)
buttongetcity.pack()
btnsalir = Button(windows, text="Quit", font =("arial", 15, "normal"),background= "#114251",foreground = "#ffffff", bd = 0, command=windows.destroy)
btnsalir.config(width=50, height=1)
btnsalir.pack(padx = 0, pady = 1)


city = Label(font = ("arial",20, "bold"), background="#5cc0de")
city.pack(padx = 10, pady = 10)

descr = Label(font = ("arial",15, "normal"), background="#5cc0de")
descr.pack(padx = 10, pady = 10)
temp = Label(font = ("arial",15, "normal"), background="#5cc0de")
temp.pack(padx = 10, pady = 10)
press = Label(font = ("arial",15, "normal"), background="#5cc0de")
press.pack(padx = 10, pady = 10)
#lonn = Label(font = ("arial",10, "normal"))
#lonn.pack(padx = 10, pady = 10)
#latt = Label(font = ("arial",10, "normal"))
#latt.pack(padx = 10, pady = 10)
wind = Label(font = ("arial",15, "normal"), background="#5cc0de")
wind.pack(padx = 10, pady = 10)
deg = Label(font = ("arial",15, "normal"), background="#5cc0de")
deg.pack(padx = 10, pady = 10)
gust = Label(font = ("arial",15, "normal"), background="#5cc0de")
gust.pack(padx = 10, pady = 10)
humidity = Label(font = ("arial",15, "normal"), background="#5cc0de")
humidity.pack(padx = 10, pady = 10)
sunrisee = Label(font = ("arial",15, "normal"), background="#5cc0de")
sunrisee.pack(padx = 10, pady = 3)
sunsett = Label(font = ("arial",15, "normal"), background="#5cc0de")
sunsett.pack(padx = 10, pady = 2)


windows.mainloop()