from folium import Map, FeatureGroup, CircleMarker, Popup, Tooltip, IFrame, GeoJson, LayerControl
import pandas as pd

def get_marker_color(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 3000:
        return 'yellow'
    else:
        return 'red'

def get_population_color(element):
    population = element['properties']['POP2005']

    if population < 100000000:
        color = 'green'
    elif population < 200000000:
        color = 'yellow'
    else:
        color = 'red'
    
    return { 'fillColor': color, 'fillOpacity': 0.3, 'color': color }

data = pd.read_csv(open('volcanoes.txt', 'r'))

popup = """
<h4>Information</h4>
<table>
<tbody>
<tr>
<td>Name</td>
<td>{}</td>
</tr>
<tr>
<td>Elevation</td>
<td>{}</td>
</tr>
<tr>
<td>Status</td>
<td>{}</td>
</tr>
<tr>
<td>Type</td>
<td>{}</td>
</tr>
</tbody>
</table>
"""

map = Map(
    location=(41.85, -112.59),
    zoom_start=6,
    min_zoom=3,
    max_zoom=13,
    control_scale=True
)

fg_vol = FeatureGroup(name="Volcano")

for index in data.index:
    info = dict(data.loc[index, :])
    iframe = IFrame(
        html=popup.format(
            info['NAME'],
            info['ELEV'],
            info['STATUS'],
            info['TYPE']
        ),
        width='200px',
        ratio='100%'
    )

    CircleMarker(
        location=(info['LAT'], info['LON']),
        radius=7,
        popup=Popup(iframe),
        tooltip=Tooltip(info['NAME']),
        color="grey",
        fill=True,
        fill_color=get_marker_color(info['ELEV']),
        fill_opacity=0.8
    ).add_to(fg_vol)

fg_pop = FeatureGroup(name="Population")

GeoJson(
    data=open('world.json', 'r', encoding='utf-8-sig').read(),
    style_function=get_population_color
).add_to(fg_pop)

fg_vol.add_to(map)
fg_pop.add_to(map)
LayerControl().add_to(map)

map.save('map.html')
