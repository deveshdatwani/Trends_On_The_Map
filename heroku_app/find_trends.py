import os
from boto.s3.connection import S3Connection
import requests
import pandas as pd

#bearer_token = S3Connection(os.environ['BEARER_TOKEN'])

def find_current_trends():

	url = 'https://api.twitter.com/1.1/trends/available.json'
	bearer = os.environ['BEARER_TOKEN']
	response = requests.get(url=url, headers = {'authorization': 'Bearer ' + bearer})
	response = response.json()
	rending_cities = []

	for trend in response:
		trending_cities.append([trend['name'], trend['country'], trend['woeid']])

	trending_cities_df = pd.DataFrame(trending_cities, columns=['city','country','woeid'])
	city_coordinates = pd.read('worldcities.csv')
	city_coordinates = city_coordinates[['city','country','lat','lng']]
	trending_cities_df = trending_cities_df.merge(city_coordinates,on=['country','city'])

