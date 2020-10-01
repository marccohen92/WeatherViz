import folium
from geopy.geocoders import Nominatim
from src.display import write_temperatures, add_legend
from src.scrapping import find_temperatures, get_coordinates
from src.common.constants import ZOOM_INIT

def create_map(citys, month, start_location):
    temp, rain = find_temperatures(citys, month)
    geolocator = Nominatim(user_agent="weather_finder", timeout=3)
    start_coordinates = get_coordinates(geolocator, start_location)
    my_map = folium.Map(location=start_coordinates, zoom_start=ZOOM_INIT)
    my_map = write_temperatures(my_map, temp, rain, geolocator)
    my_map = add_legend(my_map, month)
    return my_map