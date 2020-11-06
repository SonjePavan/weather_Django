from django.http import HttpResponse
from django.shortcuts import render
import re
import requests

def home (request):
    return render(request,'weather.html')
    # return render(request, 'home.html') #for simplest UI
def getinfo(request):
    pattern = "^\d{6}$"
    pattern1 = "[a-z A-Z]"
    pin = request.GET['pincode']
    if (re.search(pattern, pin)):
        url = "http://api.openweathermap.org/data/2.5/weather?zip=" + pin + ",in&appid=d556e008e55ad5e65918a1f441b101a9"
        res = requests.get(url).json()
        area = res['name']
        temp = str(int(res["main"]['temp']) - int(273))+"\N{DEGREE SIGN}C"
        cloud = res["weather"][0]['description']
        return render(request, 'weather.html',
                      {"Ar": area, "te": temp,  "cl": cloud } )
        # Simplest UI
        # return render(request, 'home.html',
        #               {"Ar": area, "te": temp, "cl": cloud})

    elif (re.search(pattern1, pin)):
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + pin + ",in&appid=d556e008e55ad5e65918a1f441b101a9"
        res = requests.get(url).json()
        area = res['name']
        temp = str(int(res["main"]['temp']) - int(273))+"\N{DEGREE SIGN}C"
        cloud = res["weather"][0]['description']
        return render(request, 'weather.html',
                      {"Ar": area, "te": temp, "cl": cloud})
        # Simplest UI
        # return render(request, 'home.html',
        #               {"Ar": area, "te": temp, "cl": cloud})
    else:

        return HttpResponse("<h1>Ooooop's Something Wrong <br> check picode/city Name Once Again</h1>")
