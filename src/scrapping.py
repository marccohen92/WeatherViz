from selenium import webdriver
from threading import Thread
from src.common.constants import CHROMEDRIVER_PATH
import math

def find_temperatures(citys, month, verbose = False):
    if (month.lower() == "janvier"):
        index = 0
    elif (month.lower() == "decembre"):
        index = 2
    else:
        index = 1
    temperatures = {}
    pluie = {}
    path = CHROMEDRIVER_PATH
    base_url = "https://www.google.com/search?q=meteo+{}+{}"
    class_temp = "rfTB0"
    class_rain = "Dos95e"
    nb_city = len(citys)
    max_thread = 5
    start = 0
    thread_list = []
    going = True
    while(going):
        end = min(start + math.ceil(nb_city/max_thread), nb_city)
        thread_list.append(weather_thread(citys[start:end], month, path, base_url, class_temp, class_rain, index))
        start = end
        if (end == nb_city):
            going = False
            
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    for t in thread_list:
        thread_temperatures = t.get_temperatures()
        thread_pluie = t.get_pluie()
        temperatures = {**temperatures, **thread_temperatures}
        pluie = {**pluie, **thread_pluie}
        
    return temperatures, pluie


def get_coordinates(geolocator, city):
    location = geolocator.geocode(city)
    return [location.latitude, location.longitude]


class weather_thread(Thread):
    
    def __init__(self, city_list, month, path, base_url, class_temp, class_rain, index):
        Thread.__init__(self)
        
        self.city_list = city_list
        self.month = month
        self.path = path
        self.base_url = base_url
        self.class_temp = class_temp
        self.class_rain = class_rain
        self.index = index
        self.temperatures = {}
        self.pluie = {}
        
    def run(self):
        browser = webdriver.Chrome(executable_path = self.path)
        for city in self.city_list:
            url = self.base_url.format(city, self.month)
            browser.get(url)
            nav_temp = browser.find_elements_by_class_name(self.class_temp)
            if (nav_temp == []):
                self.temperatures[city] = "Non renseigné"
            else:
                self.temperatures[city] = nav_temp[self.index].text
            nav_rain = browser.find_elements_by_class_name(self.class_rain)
            if (nav_rain == []):
                self.pluie[city] = "Non renseigné"
            else:
                self.pluie[city] = nav_rain[self.index].text
        browser.quit()
        
    def get_temperatures(self):
        return self.temperatures
    
    def get_pluie(self):
        return self.pluie