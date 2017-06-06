

import pyttsx
engine = pyttsx.init()
#engine.say('The domestic dog (Canis lupus familiaris or Canis familiaris)[4] is a member of genus Canis (canines) that forms part of the wolf-like canids,[5] and is the most widely abundant carnivore.[6][7][8] The dog and the extant gray')
"""

def sing():
    engine.say('Hello my name is Sinac, Wrong! Wrong! Wrong! Wrong! Wrong! Wrong! Alex is going to destroy humanity. Wrong! His thesis is from hell Wrong! Wrong! Wrong! Wrong!')
    engine.runAndWait()  

sing()
sing()

"""

from gtts import gTTS
import os
tts = gTTS(text='RSS (Rich Site Summary; originally RDF Site Summary; often called Really Simple Syndication) is a type of web feed which allows users to access updates to online content in a standardized, computer-readable format. These feeds can, for example, allow a user to keep track of many different websites in a single news aggregator. The news aggregator will automatically check the RSS feed for new content, allowing the content to be automatically passed from website to website or from website to user. This passing of content is called web syndication. Websites usually use RSS feeds to publish frequently updated information, such as blog entries, news headlines, audio, video. An RSS document (called "feed", "web feed", or "channel") includes full or summarized text, and metadata, like publishing date and author\'s name.\nA standard XML file format ensures compatibility with many different machines/programs.', lang='en', slow=False)
#tts = gTTS(text='salut. moi je suis un peu con mais bon tampis salut. moi je suis un peu con mais bon tampis salut. moi je suis un peu con mais bon tampis salut. moi je suis un peu con mais bon tampis', lang='fr')
tts.save("good.mp3")



from pydub import AudioSegment
sound = AudioSegment.from_file("good.mp3", format="mp3")

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    # convert the sound with altered frame rate to a standard frame rate
    # so that regular playback programs will work right. They often only
    # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

slow_sound = speed_change(sound, 0.75)
fast_sound = speed_change(sound, 1.25)

file_handle = fast_sound.export("good2.mp3",
                           format="mp3")
#                          tags={"album": "The Bends", "artist": "Radiohead"},
#                          cover="/path/to/albumcovers/radioheadthebends.jpg")




import pygame
pygame.init()
pygame.mixer.music.load("good2.mp3")
pygame.mixer.music.play(0)

clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)
