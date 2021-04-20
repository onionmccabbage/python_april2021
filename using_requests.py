# we can make calls to API end points to access remote data
import requests
import json # json is part of the standard library
from modules.util import checkInt

def main(which_id=42):
    result = requests.get('https://jsonplaceholder.typicode.com/photos/{}'.format(which_id))
    result_d = result.json()
    print(result_d, type(result_d)) # a dictionary
    print('The id is {} for url of {} and title of {}'.format(result_d['id'], result_d['url'], result_d['title']))

if __name__ == '__main__':
    # ask the user for an id
    id = input('which id? ')
    id = checkInt(id) # use our utility to make sure it is an integer
    main(id)