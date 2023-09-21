from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class BoxLayoutExample(BoxLayout):
    def add_button(self):
        new_button = Button(text="new button")
        self.new.add_widget(new_button)
        print("Butt-on")

    def remove_button(self):
        self.new.remove_button(self)
        print("Butt-off")


class MainWidget(Widget):
    pass


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"


class WidgetLayoutApp(App):
    pass


WidgetLayoutApp().run()
