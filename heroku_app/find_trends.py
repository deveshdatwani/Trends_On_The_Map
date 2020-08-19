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
	trending_cities = []

	for trend in response:
		trending_cities.append([trend['name'], trend['country'], trend['woeid']])

	trending_cities_df = pd.DataFrame(trending_cities, columns=['city','country','woeid'])
	city_coordinates = pd.read_csv('worldcities.csv')
	city_coordinates = city_coordinates[['city','country','lat','lng']]
	trending_cities_df = trending_cities_df.merge(city_coordinates,on=['country','city'])
	woeids = trending_cities_df['woeid'].values
	trends_in_woeids = []
	url2 = 'https://api.twitter.com/1.1/trends/place.json'
	
	for woeid in woeids:
    	param = {'id':woeid}
    	response = requests.get(url = url2, headers = {'authorization': 'Bearer ' + bearer}, params = param).json()
    	trends_in_woeids.append(response)	

    thirty_trends_in_woeids = trends_in_woeids[:30]
    l1 = []
	
	for i in thirty_trends_in_woeids:
    	l2 = []
    	for j in i[0]['trends']:
        	l2.append(j['name'])
    	l1.append(l2)
 	
 	first_thirty = trending_cities_df[:30]
 	first_thirty.insert(5, 'trends', l1)
 	first_thirty.to_csv('trending_cities.csv')