import kivy
kivy.require('1.11.1')

from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
import time

class PyDate(Widget):

    date_label = Label()

    def __init__(self, **kwargs):
        super(PyDate, self).__init__(**kwargs)
        Clock.schedule_interval(self.update_date, 3600)

    def update_date(self, *args):
        self.date_label.text = time.strftime("%A, %m, %B")

    def configure_date(self):
        self.date_label.font_size ='80sp'
        self.pos_hint = {'top':0.9, 'x':0.1}
        self.add_widget(self.date_label)
