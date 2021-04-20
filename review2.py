import requests
from modules.sanitize import cleanup

def get_data(category, id):
    # print(category, id)
    url = 'https://jsonplaceholder.typicode.com'
    full_path = '{}/{}/{}'.format(url, category, id)
    j = {'message':'no data'} # we need a dict
    try:
        res = requests.get(full_path)
        j = res.json() # we just want the json data
    except Exception as err:
        print('Something went wrong. ', err)
    finally:
        return j # return the data as a dict

def main():
    # use our sanitize module to clean up some data
    # ask the user for a category and an id
    which_cat = input('which category? ')
    which_id  = input('which id (1-8)? ')
    cleaned = cleanup(category=which_cat, id = which_id)
    # print(cleaned)
    # make a request and return the json
    data = get_data(category = cleaned['category'], id = cleaned['id'])
    print('Category {} member {} gives the following:'.format(cleaned['category'], cleaned['id']))
    for k, v in data.items():
        print('\t{}: {}'.format(k, v))
    # if category is 'users' then we also want all the posts
    if cleaned['category'] == 'users':
        print('Posts for user {}:'.format(cleaned['id']))
        posts = get_data(category='posts', id='')
        for item in posts: # posts is a list
            if item['userId']==cleaned['id']:
                print('Post {}: title: {} body:{}\n'.format(item['id'], item['title'], item['body']))

if __name__ == '__main__':
    main()