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
        Clock.schedule_interval(self.update_clock, 1/60)

    def update_clock(self, *args):
        self.time_label.text = time.strftime("%H:%M")

    def configure_clock(self):
        self.time_label.font_size ='100sp'
        self.center = [500, 500]
        self.pos_hint = {'top':0.9, 'x':0.1}
        self.add_widget(self.time_label)
