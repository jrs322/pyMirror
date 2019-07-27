#!/usr/#!/usr/bin/env python3

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from modules.clock.PyClock import PyClock
from kivy.uix.widget import Widget
#global variables
class RootWidget(Widget): pass

class PyMirrorLayout(AnchorLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(PyMirrorLayout, self).__init__(**kwargs)

class PyMirror(App):
    #functions
    def build(self):
        return self.config_layout()

    def config_layout(self):
        #Root Layout for PyMirror
        root = RootWidget()
        pylayout = PyMirrorLayout()
        #Declare widgets for addition to root
        pyclock = PyClock()
        #Add widgets to root
        root.add_widget(pylayout)
        pylayout.add_widget(pyclock)
        #Finish and return root
        return root

if __name__ == "__main__":
    PyMirror().run()
