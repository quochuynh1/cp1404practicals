"""
Prac 08 Do-from-scratch Exercises
"""

from kivy.app import App
from kivy.lang import Builder


class MilesConverter(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MilesConverter().run()
