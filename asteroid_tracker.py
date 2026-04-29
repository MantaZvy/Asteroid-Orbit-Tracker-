import requests, pandas, matplotlib.pyplot as plt
from datetime import datetime, timedelta

api_key = "qUp5Uujy6vpDNjtG4fSnW6FxGam8F5vHeSTiKwAt"
base_url = "https://api.nasa.gov/neo/rest/v1/feed" #Nasa endpoint for  Earth object data

def fetch_asteroid_data(start_date, end_date, api_key):#Fetches asteroid data from NASA Neows from given date range
    params ={
        'start_date': start_date,
        'end_date': end_date,
        'api_key': api_key
    }
    print(f'Fetching asteroid data from {start_date} to {end_date}.')
    
    response = requests.get(base_url, params=params) #GET request to NASA API
    
    if response.status_code == 200:
        print('Data fetched successfully.')
        return response.json() #convert JSON response to python dictionary
    else:
        print(f'Error fetching data: {response.status_code}')
        return None
    
def process_asteroid_data(data):#Extracts relevant info from raw nasa data JSON. Nasa stores its data as date
    asteroids = []
    earth_objects = data.get('near_earth_objects', {})
    for date, asteroid_list in earth_objects.itens():
        for asteroid in asteroid_list:
            asteroids.append({#Extracting raw data such as name, asteroid unique identifier, date, diameter, and hazerdous status (Nasa's classification).
                'name': asteroid['name'],
                'id': asteroid['id'],
                'close_approach_date': date,
                'estimated_diameter_km': asteroid['estimated_diameter']['kilometers']['estimated_diameter_max'],
                'is_potentially_hazardous': asteroid['is_potentially_hazardous_asteroid']
            })
    