# Vybz
Django social-network app with Youtube and Spotify API back-end access. 

Utilizing postgresql, the app allows users to:
1. Create profiles
2. Friend other users
3. Add to a list of musical artists that can be seen by all users with information and links (e.g. Spotify page)
4. Add song information and links (e.g. Youtube) for each artist
5. Display user-added songs on user profiles 
6. Spotfiy API access allows the addition of 20 random songs to your Spotify "Liked Songs" playlist. 
7. Youtube API access works in conjunction with Spotify, allowing users to search through songs on any of their Youtube playlists and add the songs to their Spotify liked songs. (Run run.py file in terminal for capability) 



Installation:


Virtual Environment
```
$ pip3 install virtualenv
```

Requirements
```
$ pip3 install -r requirements.txt
```

Postgres 

```$ brew install postgres```

```$ brew tap homebrew/services ``` to install brew services.


```$ brew services start postgresql ``` to start postgres as a background service

``` $ brew services stop postgresql ``` to stop postgres manually. You can also use brew services to restart Postgres brew services restart postgresql


Django and psycop2 (for PostgreSQL within Django)
```
$ pip3 install Django

$ pip3 install psycopg2
```

Spotify and Youtube API
1. YouTube Data API credentials (named as client_secret.json). These must be placed in the creds/ directory.
2. Spotify Web API OAuth Token. Must be sourced in your environment as SPOTIFY_AUTH_TOKEN
3. YouTube Data API: https://developers.google.com/youtube/v3
4. Spotify Web API: https://developer.spotify.com/documentation/web-api/
