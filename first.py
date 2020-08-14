import folium 

m = folium.Map(tiles = 'Stamen Toner')

tooltip = 'Click Me'

folium.Marker([19.0760,72.8777], popup = '<i>This is Mumbai<i>', tooltip=tooltip).add_to(m)

m.save('index.html')

