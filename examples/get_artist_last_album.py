from route import Cpath
Cpath()
from spApi import getAccessToken, getID
from ArtistClass import Artist

clientid = ""
secret = ""

token = getAccessToken(clientid, secret)

ID = getID(token, "Kanye West", "artist")

Kanye = Artist(token, ID)

print(Kanye.album['album_1'])
print(Kanye.album['album_1_id'])
