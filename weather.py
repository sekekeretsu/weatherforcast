import tkinter as tk
import requests

root=tk.Tk()
height=700
width=700
degree_sign= u'\N{DEGREE SIGN}'
def function1(myentry):
    print(" this is funtion1"+ myentry)
    city=myentry
    mykey='688675f92570f6186084e4a3411eca43'
    url='https://api.openweathermap.org/data/2.5/weather'
    params= {'APPID': mykey, 'q':city, 'units': 'Celsius'}
    response=requests.get(url, params=params)
    weather=response.json()
    print(weather)
    label['text']= function2(weather)
    
def function2(weather):
    try:
        cityname=weather['name']
        citycondition=weather['weather'][0]['description']
        citytemperature=weather['main']['temp']
        cityhumidity=weather['main']['humidity']
        print("\n after collection \n")
        citytemperature=int(citytemperature-273.15)
        report= ' City: %s \n Condition: %s \n Temperature(C): %s \n Humidity: %s' %(cityname, citycondition, citytemperature, cityhumidity)
    except:
        report=' Sorry! There was a problem. Please check the city name entered.'
    return report


    


canvas=tk.Canvas(root, height=height, width=width, bg='tan')
canvas.pack()
#frame to contain the city name and search button
upperframe=tk.Frame(canvas, bg='darksalmon')
upperframe.place(relx=0.2, rely=0.2, relwidth=0.5, relheight=0.25)
#text area for the city name
entry=tk.Entry(upperframe,font=10, bg='lightsalmon')
entry.place(relx=0.1, rely=0.4, relwidth=0.44, relheight=0.3)

#the search button
search_button=tk.Button(upperframe, text="search", command= lambda: function1(entry.get()))
search_button.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.3)

label=tk.Label(root,text=" Check current weather", bg='darksalmon', font=40)
label.place(relx=0.2, rely=0.5, relwidth=0.5, relheight=0.35)



root.mainloop()
