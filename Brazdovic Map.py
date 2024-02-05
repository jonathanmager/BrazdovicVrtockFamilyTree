import folium
from folium.plugins import AntPath

#create a map object
mapObj = folium.Map(tiles = "CartoDB positron", location=[48.4657,17.4938], zoom_start = 5)

Boleraz = folium.IFrame('''Ernestina is from a suburb of Bratislava, Slovakia.  It is not clear the exact name of that
suburb - perhaps heard something that sounds phonetically like “Bolinraz” but the
spelling and exact location is not available. At the time, it was a farming area and
Bratislava was the closest major city.''')

folium.Marker(location = [48.4657, 17.4938], icon = folium.Icon(icon = "glyphicon-star"), popup = folium.Popup(Boleraz, parse_html=True, min_width = 500 , max_width = 500),tooltip = "Boleraz, Slovakia").add_to(mapObj)
folium.Marker(location = [48.2082, 16.3719], icon = folium.Icon(icon = "glyphicon-star"), tooltip = "Vienna, Austria").add_to(mapObj)
folium.Marker(location = [40.4406, -79.9959], icon = folium.Icon(icon = "glyphicon-star"), tooltip = "Pittsburgh, Pennsylvannia").add_to(mapObj)
folium.Marker(location = [40.0162, -80.7423], icon = folium.Icon(icon = "glyphicon-star"), tooltip = "Bellaire, Ohio").add_to(mapObj)



pathLatLngs = [(48.4657, 17.4938), (48.2082, 16.3719)] #Boleraz slovakia to Vienna Austria
pathLatLngs2     = [(48.2082, 16.3719), (40.4406, -79.9959)] # Vienna Austria to Pittsburgh Pennsylvannia
pathLatLngs3     = [(40.4406, -79.9959), (40.0162, -80.7423)] # Vienna Austria to Pittsburgh Pennsylvannia



AntPath(pathLatLngs, delay = 400, weight = 3, color = "red", dash_array = [30,15]).add_to(mapObj)
AntPath(pathLatLngs2, delay = 400, weight = 3, color = "blue", dash_array = [30,15]).add_to(mapObj)
AntPath(pathLatLngs3, delay = 400, weight = 3, color = "green", dash_array = [30,15]).add_to(mapObj)



mapObj.save("BrazdovicVrtockFamilyTree/outputmap.html")
