import folium
import itertools
import json
import requests
import pandas as pd


def load_map_with_trends():

	m = folium.Map(tiles='Stamen Terrain',  zoom_start=3, location=[20.76, 79])
	country_cordinates = pd.read_csv('country_cordinates.csv')
	tooltip = 'See Trends'
	lat = country_cordinates['latitude']
	lon = country_cordinates['longitude']
	country = country_cordinates['country']
    
	for i, country in enumerate(country):

		try:

			folium.Marker([lat[i], lon[i]], popup = '<i>This is {}<i>'.format(country), tooltip = tooltip).add_to(m)
		
		except: pass

	m.save('trends_on_the_map.html')

	return None

if __name__ == '__main__':

	load_map_with_trends()