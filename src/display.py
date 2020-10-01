import folium
from folium.features import DivIcon
from folium.map import Marker, Popup
from folium.features import RegularPolygonMarker
from geopy.geocoders import Nominatim
from src.scrapping import get_coordinates


def add_legend(my_map, month):
    item_txt = """<br> &nbsp; {item} &nbsp; <i class="fa fa-map-marker fa-2x" style="color:{col}"></i>"""
    html_itms = ""
    for color, text in zip(["blue", "green", "orange", "red", "grey"], ["Max ≤ 18", "18 < Max ≤ 24", "24 < Max ≤ 30", "Max > 30"]):
        html_itms += item_txt.format( item= text , col= color)
    legend_html = """
         <div style="
         position: fixed; 
         bottom: 50px; left: 50px; width: 120px; height: 100px; 
         border:2px solid grey; z-index:9999; 

         background-color:white;
         opacity: .85;

         font-size:10px;
         font-weight: bold;

         ">
         &nbsp; {title} 

         {itm_txt}

          </div> """.format( title = "Month: "+month, itm_txt= html_itms)
    my_map.get_root().html.add_child(folium.Element( legend_html ))
    return my_map


def write_temperatures(my_map, temp, rain, geolocator):
    for city in temp:
        my_map = _write_pop_up(my_map, city, temp[city], rain[city], geolocator)
    return my_map


def _write_pop_up(my_map, city, temp, rain, geolocator):
    min_temp, max_temp = _extract_min_max_temp(temp)
    pluie = _extract_pluie(rain)
    position = get_coordinates(geolocator, city)
    text_to_write = _define_text(city, min_temp, max_temp, pluie)
    color = _get_color_from_temp(max_temp)
    icon, icon_color = _get_icon_from_rain(pluie)
    my_map = _add_label_icon(my_map, position, text_to_write, color, icon, icon_color)
    return my_map


def _define_text(city, min_temp, max_temp, pluie):
    if (min_temp == 100):
        min_temp = "Non renseigné"
    if (max_temp == 100):
        max_temp = "Non renseigné"
    if (pluie == 100):
        pluie = "Non renseigné"
    text_city = "<i>"+city+"<i>"
    text_max = "Max : <b>"+ str(max_temp) + "°</b>"
    text_min = "Min: <b>"+ str(min_temp) +"°</b>"
    text_pluie = "Pluie:<b>"+ str(pluie) +" jours</b>"
    return text_city + "<br>" + text_max + "<br>" + text_min + "<br>" + text_pluie


def _extract_pluie(pluie):
    if (pluie == "Non renseigné"):
        pluie_int = 100
    else:
        pluie_int = int(pluie[:pluie.find(" ")])
    return pluie_int


def _extract_min_max_temp(temp):
    if (temp == "Non renseigné"):
        min_int = 100
        max_int = 100
    else:
        min_int, max_int = int(temp[temp.find("/")+2:-1]), int(temp[:temp.find("°")])
    return min_int, max_int 


def _add_label_icon(my_map, position, text, color, icon, icon_color):
    html = folium.Html(text, script=True)
    Marker(location=position,
           popup=Popup(html, True, 200,False, True),
           icon= folium.Icon(icon=icon,color=color, icon_color=icon_color, prefix = 'fa' )
          ).add_to(my_map)
    return my_map

def _get_icon_from_rain(rain):
    if rain == 100:
        icon = "question"
        icon_color = "black"
    elif rain>12:
        icon = "tint"
        icon_color = "blue"
    elif rain>7:
        icon = "cloud"
        icon_color = "grey"
    else:
        icon = "sun-o"
        icon_color = "yellow"
    return icon, icon_color
        

def _get_color_from_temp(temp_max):
    if temp_max == 100:
        color = "gray"
    elif (temp_max > 30):
        color = "red"
    elif (temp_max > 24):
        color = "orange"
    elif (temp_max > 18):
        color = "green"
    else:
        color = "blue"
    return color