import urllib
import urllib2
from bs4 import BeautifulSoup
import youtube_dl
import threading
import vlc
import pafy
import time
PAUSE = 2
YOUTUBE_URL ="https://www.youtube.com/results?search_query="

class youtube_player:
    def __init__(self, instance_vlc, player_vlc):
        self.instance_vlc = instance_vlc
        self.player_vlc = player_vlc
        self.stream = []
        self.youtube_url = []
        self.current_stream_idx = 0
        self.current_youtube_url_idx = 0
        self.run = True

    def search_youtube_urls(self,text_to_search):
        query = urllib.quote(text_to_search)
        url = YOUTUBE_URL + query
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        self.youtube_url = []
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            self.youtube_url.append('https://www.youtube.com' + vid['href'])
        
    def generate_urls_list(self, youtube_url, playlist = True):
        playlist = pafy.get_playlist(youtube_url)
        for i_video in range(len(playlist['items'])):
            v = playlist['items'][i_video]['pafy']
            print i_video
            try:
                self.stream.append(v)
            except:
                pass

    def play_youtube_playlist(self, request):
        self.run = True
        if "playlist" not in request:
            text_to_search = 'playlist '+request
        self.search_youtube_urls(text_to_search)
        self.play_songs_background()

    def play_songs(self):
        print "start playing songs"
        while self.current_youtube_url_idx < len(self.youtube_url) and self.run:
            youtube_url = self.youtube_url[self.current_youtube_url_idx]
            self.generate_urls_list(youtube_url, playlist=True)
            while self.current_stream_idx < len(self.stream) and self.run:
                v = self.stream[self.current_stream_idx]
                try:
                    url = v.getbest().url
                    media = self.instance_vlc.media_new(url)
                    self.player_vlc.set_media(media)
                    self.player_vlc.play()
                    time.sleep(3*PAUSE)
                    for j in range(v.length):
                        if not self.player_vlc.is_playing() or not self.run:
                            break
                        time.sleep(1)
                except:
                    pass
                time.sleep(PAUSE)
                self.current_stream_idx += 1

    
    def stop(self):
        self.run = False

    def next_song(self):
        self.player_vlc.stop()
        self.run = False
        time.sleep(PAUSE)
        self.run = True
        self.play_songs_background()

    def previous_song(self):
        self.player_vlc.stop()
        self.run = False
        self.current_stream_idx -= 1
        if self.current_stream_idx < 0:
            self.current_youtube_url_idx -= 1
            self.current_stream_idx = -1
        if self.current_youtube_url_idx < 0:
            self.run = False
        else:
            time.sleep(PAUSE)
            self.run = True
            self.play_songs_background()

    def add_simple_song(self, textToSearch):
        url = query_youtube_video(textToSearch)[0]
        v = pafy.new(url)
        media = instance_vlc.media_new(v.getbest().url)
        player_vlc.set_media(media)
        player_vlc.play()

    def download_song(self,textToSearch):
        url = query_youtube_video(textToSearch)[0]
        ydl_opts = {'format': 'bestaudio/best',
                    'postprocessors': [{'key': 'FFmpegExtractAudio',
                                        'preferredcodec': 'mp3',
                                        'preferredquality': '192',
                                        }],
                    }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def increase_volume(self):
        volume = player_vlc.audio_get_volume()
        self.player_vlc.audio_set_volume(min(volume +10,100))

    def decrease_volume(self):
        volume = player_vlc.audio_get_volume()
        self.player_vlc.audio_set_volume(max(volume -10,0))

    def play_songs_background(self):
        self.thread = threading.Thread(target=self.play_songs, args=())
        self.thread.start()

    def return_information_of_current_song(self):
        v = self.stream[self.current_stream_idx]
        return {"title": v.title,
                "length": v.length,
                "viewcount": v.viewcount,
                "category": v.category,
                "dislikes": v.dislikes,
                "likes": v.likes,
                "rating": v.rating}
if __name__ == "__main__":
    instance_vlc = vlc.Instance()
    player_vlc = instance_vlc.media_player_new()
    yp = youtube_player(instance_vlc,player_vlc)
    yp.play_youtube_playlist("Jose Luis Perales")
    for i in range(5):
        time.sleep(20)
        yp.next_song()
    yp.stop()
