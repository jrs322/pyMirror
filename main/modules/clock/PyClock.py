import kivy
kivy.require('1.11.1')

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
import time

class PyClock(Widget):

    time_label = Label()

    def __init__(self, **kwargs):
        super(PyClock, self).__init__(**kwargs)
        self.add_widget(self.time_label)
        Clock.schedule_interval(self.update_clock, 1/60)

    def update_clock(self, *args):
        current_time = time.localtime()
        self.time_label.text = time.strftime("%H:%M:%S")
