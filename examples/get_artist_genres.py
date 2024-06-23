from route import Cpath
Cpath()
from spApi import getAccessToken, getID
from spApiClasses import Artist



clientid = "e0bccd7a3f894c1ea9f8bd990bba0d69"
secret = "8334aa11b7584401bec8b2221260fad4"

token = getAccessToken(clientid, secret)

ID = getID(token, "Kanye West", "artist")

Kanye = Artist(token, ID)

print(Kanye.genres)

