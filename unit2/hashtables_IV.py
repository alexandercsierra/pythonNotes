"""
Caching web client
Go get URLS
cache the result

cache entries should timeout after 10 seconds
    this keeps the cache from getting too stale
    at most a webpage is only a few seconds old

Things to do:
-read data from urls
-have a cacheEntry object to hold data and timestamps
-compute time differences against those timestamps
-REPL that reads URL and prints the result data


if given bytes instead of string, can use .decode() to convert to string

--look into html parser -- 
"""

import urllib.request
import time


class CacheEntry:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        self.timestamp = time.time()



cache = {}
CACHE_TIMEOUT_SECONDS = 10

def get_data(url):
    #want to fetch from server the first time, and if it's too old
    curtime = time.time()
    if (url not in cache) or curtime - cache[url].timestamp > CACHE_TIMEOUT_SECONDS:
        print('FETCHING FROM SERVER')
        with urllib.request.urlopen(url) as f:
            #comes back as bytes, .decode changes to a string
            #ignore maybe ignores valid characters
            # cache[url] = f.read().decode('utf-8', "ignore")
            data = f.read().decode('utf-8', "ignore")
            cache[url] = CacheEntry(url, data)
    else:
        print('FETCHING FROM CACHE')
        age = curtime - cache[url].timestamp


    return cache[url]

def main():
    while True:
        url= input("enter URL: ")
        entry = get_data(url)
        print(entry.data[:40])




"""
CSV Files
build various indexes
if there are column names can use DictReader
-what are all the city names in a particular state

"""

import csv


cities_per_state = {} #key will be state name, value is a list of cities in that state
states_per_city = {}
population_buckets = {}
def read_csv_data():
    with open('cities.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            state_id = row['state_id']
            city = row['city']

            if state_id not in cities_per_state:
                cities_per_state[state_id] = []

            cities_per_state[state_id].append(city)

            if city not in states_per_city:
                states_per_city[city] = []

            states_per_city[city].append(state_id)


            #population buckets

            population = int(float(row['population']))
            city_info = f'{city} {state_id} ({population})'

            if population < 10:
                population_buckets[10].append(city_info)
            elif population < 100:
                population_buckets[100].append(city_info)
            elif population < 1000:
                population_buckets[1000].append(city_info)
            elif population < 10000:
                population_buckets[10000].append(city_info)
            elif population < 100000:
                population_buckets[100000].append(city_info)
            elif population < 100000:
                population_buckets[100000].append(city_info)
            elif population < 1000000:
                population_buckets[1000000].append(city_info)
            elif population < 10000000:
                population_buckets[10000000].append(city_info)
            elif population < 100000000:
                population_buckets[100000000].append(city_info)
            else:
                raise(f'Population {population} out of range')


def main_2():

    print("Reading")

    population_buckets[10] = []
    population_buckets[100] = []
    population_buckets[1000] = []
    population_buckets[10000] = []
    population_buckets[100000] = []
    population_buckets[1000000] = []
    population_buckets[10000000] = []
    population_buckets[100000000] = []




    read_csv_data()
    while True:
        # state_id = input('Enter a City: ')
        # state_id = int(input('Enter a pop cap: '))
        pop = int(input('Enter a pop cap: '))
        # print(cities_per_state[state_id])
        # print(states_per_city[state_id])
        print(population_buckets[pop])











if __name__ == "__main__":
    # main()
    main_2()