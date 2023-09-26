from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class LayoutAssignment(BoxLayout):
    pass
class GridLayoutExample(GridLayout):
    pass
class BoxLayoutExample(BoxLayout):
    def add_button(self):

        print("Butt-on")

    def remove_button(self):
        self.remove_button(self)
        print("Butt-off")


class MainWidget(Widget):
    pass


class StackLayoutExample(StackLayout):
    def __init__(self, last_created_button, **kwargs):
        super().__init__(**kwargs)
        self.last_created_button = last_created_button
        self.orientation = "lr-tb"
        b = Button("Add Button", on_press=self.add_button(self))

    def add_button(self):
        new_button = Button(text="new button")
        new_b = self.add_widget(new_button)
        new_b.bind(on_press=self.remove_button())
        self.last_created_button = new_b

    def remove_button(self):
        self.remove_widget(self.last_created_button)


class WidgetLayoutApp(App):
    pass


WidgetLayoutApp().run()
