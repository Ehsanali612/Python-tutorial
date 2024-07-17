#  1
#  City  Names
'''def cityNames(city,country):
    cities= city + country
    return cities
ourCity=cityNames('Dera Bugti ','Baluchistan')
print(ourCity)
'''
# 2
# Album
'''def make_Album(artistName, albumName):
    albumInformation = artistName + " - " + albumName
    return albumInformation.title()

myAlbum = make_Album('Ehsan', 'Unbelievable artist')
print(myAlbum)'''

#3
'''
def greet_users(names):
   for name in names:
    msg=f" Hi {name.title()} welcome to our function "
    print(msg)
me=["hi","great"]
greet_users(me)
'''
#4
# sandwiches
'''def sandwich(items , *list):
  for items in list:    
    print('> '+ items)
sandwich('Hello','Great')
sandwich('items',"Big")'''

from print import prints as prn
prn('Google')
prn("Ehsan ")