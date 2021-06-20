import pyglet, os
from time import sleep
from threading import *
from pyglet.gl import *

pyglet.options['audio'] = ('openal', 'directsound', 'silent')

class worker(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.audio_frames = []
        self.run()

    def add_frame(self, filename):
        self.audio_frames.append(filename)

    def get_frame(self):
         if len(self.audio_frames) > 0:
             return self.audio_frames.pop(0)
         return None

    def run(self):
        while 1:
            for root, folders, files in os.walk('./audio_files/'):
                for f in file:
                    self.add_frame(f)
            sleep(1)

class AudioWindow(pyglet.window.Window):
    def __init__(self):
        self.audio_worker = worker()

    def render(self):
        frame = self.audio_frames.get_frame()
        if frame:
            music = pyglet.resource.media('music.mp3')
            music.play()
    def run(self):
        while self.alive == 1:
            self.render()

        # -----------> This is key <----------
        # This is what replaces pyglet.app.run()
        # but is required for the GUI to not freeze
        #
        event = self.dispatch_events()