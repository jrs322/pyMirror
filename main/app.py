#!/usr/bin/env python3

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from modules.clock.PyClock import PyClock
from modules.date.PyDate import PyDate
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.config import Config
from kivy.core.window import Window

def config_window():
    #Config.set('graphics', 'window_state', 'maximized')
    Config.set('graphics', 'window_state', 'visible')

    #Config.set('graphics', 'fullscreen', 'auto')
    Config.set('graphics', 'fullscreen', 'fake')

    Config.set('graphics', 'width', '1000')
    Config.set('graphics', 'height', '1000')

    #Config.set('graphics', 'rotation', '270')
    Config.set('graphics', 'rotation', '0')

    #Config.set('graphics','borderless', '1') #off
    Config.set('graphics', 'borderless', '0') #on
    Config.write()

class PyMirrorLayout(BoxLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(PyMirrorLayout, self).__init__(**kwargs)
        self.orientation='vertical'

class PyMirror(App):
    #functions
    def build(self):
        config_window()
        return self.config_layout()

    def config_layout(self):
        #Root Layout for PyMirror
        pylayout = PyMirrorLayout()
        #Declare widgets for addition to root
        pyclock = PyClock()
        pydate =  PyDate()
        #Add widgets to root
        pylayout.add_widget(pyclock)
        #pylayout.add_widget(pydate)
        #Finish and return root
        return pylayout

def main():
    PyMirror().run()

if __name__ == "__main__":
    main()
