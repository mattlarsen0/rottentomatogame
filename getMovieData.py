import requests
import csv
import sys
import json

API_KEY = 'k_ayyqm7kh'

def getMovieInfo(searchQuery):
    searchUrl = f'https://imdb-api.com/en/API/SearchMovie/{API_KEY}/{searchQuery}'
    searchResult = requests.get(searchUrl).json()['results'][0]
    ratingsUrl = f'https://imdb-api.com/en/API/Ratings/{API_KEY}/{searchResult["id"]}'
    ratingsResult = requests.get(ratingsUrl).json()
    wikiUrl = f'https://imdb-api.com/en/API/Wikipedia/{API_KEY}/{searchResult["id"]}'
    wikiResult = requests.get(wikiUrl).json()

    friendlyResult = lambda: None
    friendlyResult.title = ratingsResult['fullTitle']
    friendlyResult.rottenTomatoes = ratingsResult['rottenTomatoes']
    friendlyResult.image = searchResult['image']
    friendlyResult.wikiUrl = wikiResult['url']
    return friendlyResult

if len(sys.argv) != 2:
    print(f'{len(sys.argv)}]')
    print(f'Usage: {sys.argv[0]} [query]')
    exit(-1)

movieResults = []
for query in sys.argv[1].split(','):
    info = getMovieInfo(query)
    movieResults.append(info)


with open('movieResults.csv', 'w') as csvFile:
    csvWriter = csv.writer(csvFile)

    # Add titles
    csvWriter.writerow(['Title', 'RottenTomatoes', 'Image', 'Wiki'])

    for movie in movieResults:
        csvWriter.writerow([movie.title, movie.rottenTomatoes, movie.image, movie.wikiUrl])
        
print('Done :)')