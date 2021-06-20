import pyglet
import time
from pyglet.media.synthesis import ADSREnvelope, Sine
duration_in_ms:float=500
frequency:int=440
volume=1
adsr = ADSREnvelope(attack=duration_in_ms/8000,
                    decay=duration_in_ms/2000,
                    release=duration_in_ms/8000,
                    sustain_amplitude=volume)
sine = Sine(duration=duration_in_ms/1000, frequency=frequency,
            sample_size=16, sample_rate=44100, envelope=adsr)
#iyi_günler = pyglet.media.load(r"C:\Users\golge\Desktop\BaşlamasaQ\Memo\ses\iyi_günler.mp3")
#iyi_günler.play()
sound = pyglet.media.load(r"C:\Users\golge\Desktop\BaşlamasaQ\Memo\ses\iyi_günler.mp3")
player = sound.play()
player.on_eos = pyglet.app.exit
pyglet.app.run()

sizi = pyglet.media.load(r"C:\Users\golge\Desktop\BaşlamasaQ\Memo\ses\sizi_digitürkten_arıyorum.mp3")
player = sizi.play()
player.on_eos = pyglet.app.exit
pyglet.app.run()