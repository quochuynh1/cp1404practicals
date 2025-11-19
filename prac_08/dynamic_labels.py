"""
Prac 08 - Do from scratch Exercise
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """App to display names as labels in GUI"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.names = ["Alex", "Bob", "Mike", "Ross"]

    def build(self):
        """Build the Kivy app from the kv file"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI"""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()
