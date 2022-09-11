x = ('python', 'js', 'lua', 'ruby', 'php')

def response_habr():
    for key in keys:
        resp = requests.get(BASE_URL+'/ru/search/', params={
        'q': key,
        'target_type': 'posts',
        'order': 'relevance'

        })

    # some_code