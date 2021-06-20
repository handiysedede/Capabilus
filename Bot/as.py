import time

tts = gTTS(text=m, lang='en')
tts.save("greeting.mp3")
p = vlc.MediaPlayer("greeting.mp3")
p.play()
time.sleep(120) # number of seconds in