import json
filename = 'username.json'
with open(filename) as fiel_obj:
    username =json.load(fiel_obj)
    print('Welcome back ,{} !'.format(username))