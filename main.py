import sys
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.label import Label


print("User Current Version:-", sys.version)

class Touch(Widget):

    def on_touch_down(self, touch):
        print("Mouse down", touch)

    def on_touch_move(self, touch):
        print("Mouse move", touch)

    def on_touch_up(self, touch):
        print("Mouse up", touch)

class MyApp_2(App):
    def build(self):
        return Touch()

class MyApp(App):
    def build(self):
        return Label(text="Hello World")

if __name__ == '__main__':
    MyApp_2().run()

