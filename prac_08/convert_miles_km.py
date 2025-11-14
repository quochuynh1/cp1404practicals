"""
Prac 08 Do-from-scratch Exercises
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverter(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """

    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def get_valid_integer(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_conversion(self):
        value = self.get_valid_integer()
        result = float(value) * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, value):
        current_miles = self.get_valid_integer()
        new_miles = current_miles + value
        self.root.ids.input_miles.text = str(new_miles)

    def handle_update(self):
        self.message = self.root.ids.input_miles.text


MilesConverter().run()
