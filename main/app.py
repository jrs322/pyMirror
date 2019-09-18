#!/usr/bin/env python3

import kivy
from kivy.app import App
from modules.clock.PyClock import PyClock
from modules.date.PyDate import PyDate
from modules.calendar.PyCalendar import PyCalendar
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
kivy.require('1.11.1')


def config_window():
    # Config.set('graphics', 'window_state', 'maximized')
    Config.set('graphics', 'window_state', 'visible')
    Config.write()
    # Config.set('graphics', 'fullscreen', 'auto')
    Config.set('graphics', 'fullscreen', 'fake')
    Config.write()
    Config.set('graphics', 'width', '3500')
    Config.write()
    Config.set('graphics', 'height', '3000')
    Config.write()
    # Config.set('graphics', 'rotation', '270')
    Config.set('graphics', 'rotation', '0')
    Config.write()
    # Config.set('graphics','borderless', '1') #off
    Config.set('graphics', 'borderless', '0')
    Config.write()
    Config.set('graphics', 'left', '0')
    Config.write()
    Config.set('graphics', 'top', '3000')
    Config.write()


class PyMirrorLayout(BoxLayout):

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(PyMirrorLayout, self).__init__(**kwargs)


class PyMirror(App):

    pylayout = PyMirrorLayout()
    pyclock = PyClock()
    pydate = PyDate()
    pycalendar = PyCalendar()
    # functions

    def build(self):
        config_window()
        return self.build_root()

    def build_root(self):
        # Add widgets to root
        self.pylayout.add_widget(self.pycalendar)
        # pylayout.add_widget(pydate)
        # Finish and return root
        return self.pylayout

    def config_clock():
        pass

    def config_date():
        pass


def main():
    PyMirror().run()


if __name__ == "__main__":
    main()
