import requests

# get petitions

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

# ARTIST RELATED FUNCTIONS

def getArtist(AccessTk, artistID):
    url = f"https://api.spotify.com/v1/artists/{artistID}"

    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

def ArtistAlbums(AccessTk, artistID, Include_groups=None):
    url = f"https://api.spotify.com/v1/artists/{artistID}/albums"

    if Include_groups !=None:
        url += f"?include_groups{Include_groups}"

    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

def aTopTracks(AccessTk, artistID):
    url = f"https://api.spotify.com/v1/artists/{artistID}/top-tracks"

    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

def relatedArtists(AccessTk, artistID):
    url = f"https://api.spotify.com/v1/artists/{artistID}/related-artists"

    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

# ALBUM RELATED FUNCTIONS (GET METHOD)

def getAlbum(AccessTk, AlbumID, Market = None):
    url = f"https://api.spotify.com/v1/albums/{AlbumID}"

    if Market != None:
        url += f"?Market={Market}"
    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

def getAlbumTracks(AccessTk, AlbumID):
    url = f"https://api.spotify.com/v1/albums/{AlbumID}/tracks"

    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

# TRACK RELATED FUNCTIONS

def getTrack(AccessTk, TrackID, Market=None):
    url = f"https://api.spotify.com/v1/tracks/{TrackID}"

    if Market != None:
        url += f"?Market={Market}"

    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

def getAudioFeatures(AccessTk, TrackID):
    url = f"https://api.spotify.com/v1/audio-features/{TrackID}"
    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

def getAudioAnalysis(AccessTk, TrackID):
    url = f"https://api.spotify.com/v1/audio-analysis/{TrackID}"
    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

def getUser(AccessTk, UserID):
    url = f"https://api.spotify.com/v1/users/{UserID}"

    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

def getPlaylist(AccessTk, PlaylistID, market=None):
    url = f"https://api.spotify.com/v1/users/{PlaylistID}"

    if market != None:
        url += f"?market={market}"
    x = requests.get(url, headers={"Authorization" : AccessTk})
    return(x.json())

def getPlaylistTracks(AccessTk, PlaylistID):
    url = f"https://api.spotify.com/v1/playlists/{PlaylistID}/tracks"

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

    return response[f'{type}s']['items'][0]['id']

def GenresSeed(AccessTk):
    url = "https://api.spotify.com/v1/recommendations/available-genre-seeds"

    x = requests.get(url, headers= {"Authorization" : AccessTk})