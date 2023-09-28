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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.new_button = None
        self.last_created_button = None
        self.orientation = "lr-tb"
        self.add_widget(Button(text="Add Button", on_press=self.add_button))

    def add_button(self,widget):
        widget.color = (1,1,1,1)
        new_button = Button(text="new button",on_press=self.remove_button)
        print("test")
        self.add_widget(new_button)
        new_button.bind()
        self.last_created_button = new_button
        return

    def remove_button(self,widget):
        self.remove_widget(widget)


class WidgetLayoutApp(App):
    pass


WidgetLayoutApp().run()
