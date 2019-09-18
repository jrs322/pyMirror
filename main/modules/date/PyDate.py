import kivy
kivy.require('1.11.1')

from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.anchorlayout import AnchorLayout
import time

class PyDate(AnchorLayout):

    date_label = Label()

    def __init__(self, **kwargs):
        super(PyDate, self).__init__(**kwargs)
        self.configure_date()
        Clock.schedule_once(self.update_date)
        Clock.schedule_interval(self.update_date, 3600)

    def update_date(self, *args):
        self.date_label.text = time.strftime("%A, %B %m")

    def configure_date(self):
        self.date_label.font_size ='100sp'
        self.add_widget(self.date_label)
