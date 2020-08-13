import os
from spotify_client import SpotifyClient
from youtube_client import YoutubeClient

def run():
  # Get youtube playlists
  youtube_client = YoutubeClient('./creds/client_secret.json')
  spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
  playlists = youtube_client.get_playlists()


# Add 20 random tracks to your Liked Songs playlist
  # random_tracks = spotify_client.get_random_tracks()
  # track_ids = [track['id'] for track in random_tracks] 

  # was_added_to_library = spotify_client.add_tracks_to_library(track_ids)
  # if was_added_to_library:
  #   for track in random_tracks:
  #     print(f"Added {track['name']} to your library")
 

  # Choose video's playlist
  # iterate through playlist and print names and position for choice
  for index, playlist in enumerate(playlists):
    print(f"{index}: {playlist.title}")
  choice = int(input("Enter your choice: "))
  chosen_playlist = playlists[choice]
  print(f"Selection: {chosen_playlist.title}")
  

  # Get song videos from playlist user selected
  songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
  print(f"Adding {len(songs)} songs")


  # Search Songs in Spotify
  for song in songs:
    spotify_song_id = spotify_client.search_song(song.artist, song.track)
    if spotify_song_id:
      added_song = spotify_client.add_song_to_spotify(spotify_song_id)
      if added_song:
        print(f"Added {song.artist} - {song.track} to your Like Songs Playlist")


  
  

if __name__ == '__main__':
        run()