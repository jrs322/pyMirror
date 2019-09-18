import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.button import Button
from datetime import date
kivy.require('1.11.1')


"""
    Creates a weekday planner displaying the next 7 days of the week
    Schedule: update every hour, call check for new day
"""
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


class PyCalendar(BoxLayout):

    calendar = BoxLayout()

    def __init__(self, **kwargs):
        super(PyCalendar, self).__init__(**kwargs)
        self.current_day = int(date.today().day)
        self.current_month = int(date.today().month)
        self.current_year = int(date.today().year)
        self.weekday = int(date.today().weekday)
        self.configure_calendar()
        Clock.schedule_interval(self.update_calendar, 3600)

    """
    This code is used for the building of the weekly calendar layout
    layout_main = higher level container with month inside
    layout_week = lower level container with week inside
    returns layout_main
    """
    def build_week_container(self):
        return_layout_main = BoxLayout(orientation='vertical')
        return_layout_week = BoxLayout(orientation='horizontal')
        counter = 0
        current_weekday = self.weekday
        while (counter < 7):
            return_layout_week.add_widget(Button(text=weekdays[self.weekday] + ", " + self.current_day))
            if(current_weekday == 6):
                current_weekday = 0
                counter = counter + 1
            else:
                current_weekday = current_weekday + 1
                counter = counter + 1
        return_layout_main.add_widget(Button(text=months[self.current_month]))
        return_layout_main.add_widget(return_layout_week)
        return return_layout_main

    def check_date(self):
        if self.current_day != date.today().day:
            self.update_date()
            return False
        else:
            return True

    def update_date(self):
        self.current_day = date.day()
        self.current_month = date.month()
        self.current_year = date.year()
        self.weekday = date.weekday()

    def configure_calendar(self):
        self.calendar = self.build_week_container(self.current_day, self.weekday,
                                                  self.current_month, self.current_year)
        self.add_widget(self.calendar)

    def update_calendar(self):
        if self.check_date():
            return
        else:
            self.update_date()
            self.calendar = self.build_week_container(self.current_day, self.weekday, self.current_month,
                                                      self.current_year)
