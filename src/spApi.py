import requests

def getAccessToken(client_id, secret_id):
    url = "https://accounts.spotify.com/api/token"

    credentials = {
        "grant_type" : "client_credentials",
        "client_id" : client_id,
        "client_secret" : secret_id
    }

    x = requests.post(url, headers={"Content-Type": "application/x-www-form-urlencoded"}, data = credentials)

    r = x.json()
    AccessTk = f"Bearer {r['access_token']}"
    return(AccessTk)

def getArtist(AccessTk, artistID):
    url = f"https://api.spotify.com/v1/artists/{artistID}"

    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())
    
def getAlbum(AccessTk, AlbumID):
    url = f"https://api.spotify.com/v1/albums/{AlbumID}"

    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

def getTrack(AccessTk, TrackID):
    url = f"https://api.spotify.com/v1/tracks/{TrackID}"

    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

def getUser(AccessTk, UserID):
    url = f"https://api.spotify.com/v1/users/{UserID}"

    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

def getPlaylist(AccessTk, PlaylistID):
    url = f"https://api.spotify.com/v1/users/{PlaylistID}"

    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

def searchItem(AccessTk, Query, type):
    Query.strip()
    Pquery = ""
    for i in Query:
        if i == ' ':
            Pquery += '+'
        else:
            Pquery += i
    
    url = f"https://api.spotify.com/v1/search?q={Pquery}&type={type}"

    x = requests.get(url , headers={"Authorization" : AccessTk})

    return(x.json())

def getID(AccessTk ,Query, type):
    response = searchItem(AccessTk, Query, type)

    return response['albums']['items'][0]['id']
