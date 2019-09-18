import kivy
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import time
kivy.require('1.11.1')


class PyClock(AnchorLayout):

    time_label = Label()

    def __init__(self, **kwargs):
        super(PyClock, self).__init__(**kwargs)
        self.configure_clock()
        Clock.schedule_interval(self.update_clock, 1/60)

    def update_clock(self, *args):
        self.time_label.text = time.strftime("%H:%M")

    def configure_clock(self):
        self.time_label.font_size = '100sp'
        self.add_widget(self.time_label)
