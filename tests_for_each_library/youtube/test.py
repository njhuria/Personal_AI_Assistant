import urllibimport urllib2from bs4 import BeautifulSoup#from __future__ import unicode_literalsimport youtube_dl"""textToSearch = 'ALDOUS HUXLEY UN MUNDO FELIZ AUDIOLIBRO'query = urllib.quote(textToSearch)url = "https://www.youtube.com/results?search_query=" + queryresponse = urllib2.urlopen(url)html = response.read()soup = BeautifulSoup(html)urls = []for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):    urls.append('https://www.youtube.com' + vid['href'])print urlsydl_opts = {    'format': 'bestaudio/best',    'postprocessors': [{        'key': 'FFmpegExtractAudio',        'preferredcodec': 'mp3',        'preferredquality': '192',    }],}with youtube_dl.YoutubeDL(ydl_opts) as ydl:    ydl.download([urls[0]])"""import vlcinstance_vlc = vlc.Instance()player_vlc = instance_vlc.media_player_new()media = instance_vlc.media_new("https://www.youtube.com/watch?v=BlwBiEhUjig")player_vlc.set_media(media)player_vlc.play()import pafyimport pafyv = pafy.new("https://www.youtube.com/watch?v=BlwBiEhUjig")print(v.title)print(v.duration)print(v.rating)print(v.author)print(v.length)print(v.keywords)print(v.thumb)print(v.videoid)print(v.viewcount)print(v.audiostreams)print(v.audiostreams[0].url)instance_vlc = vlc.Instance()player_vlc = instance_vlc.media_player_new()#media = instance_vlc.media_new(v.getbestaudio().url)media = instance_vlc.media_new(v.getbest().url)player_vlc.set_media(media)player_vlc.play()print media#pafy.get_playlist()