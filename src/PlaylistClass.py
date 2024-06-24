from spApi import getPlaylist
  


class Playlist:
    def __init__(self, AccessTk, playlistID):
        response = getPlaylist(AccessTk, playlistID, market='US')

        self.name = response['name']
        self.description = response['description']
        self.is_collaborative = response['collaborative']
        self.URL = response['external_urls']['spotify']
        self.followers = response['followers']['total']
        self.endpoint = response['href']
        self.id = response['id']
        self.owner = response['owner']['display_name']
        self.owner_id = response['owner']['id']
        self.is_public = response['public']
        self.imgURLs = [response['images'][0]['url'], response['images'][1]['url'] , response['images'][2]['url']]
        
        self.NoTracks = response['tracks']['total']
        self.tracks = {}
        for i in range(self.NoTracks):
            self.track[f'track_{i+1}'] = response['tracks']['items'][i]['track']['name']
            self.track[f'track_{i+1}_id'] = response['tracks']['items'][i]['track']['id']

