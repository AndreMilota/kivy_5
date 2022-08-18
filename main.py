import sys
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.uix.label import Label
from kivy.graphics import Ellipse
from kivy.core.window import Window

print("User Current Version:-", sys.version)

class Touch(Widget):
    point_log = ()

    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 0, 0, 1, mode='rgba')
            self.rect = Rectangle(pos=(0, 0), size=(50, 50))

        self._keyboard = Window.request_keyboard(
            self._keyboard_closed, self, 'text')
        if self._keyboard.widget:
            # If it exists, this widget is a VKeyboard object which you can use
            # to change the keyboard layout.
            pass
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)


    def on_touch_down(self, touch):
        print("Mouse down", touch)

    def on_touch_move(self, touch):
        with self.canvas:
            self.point_log += touch.pos
            if len(self.point_log) >= 4:
                Color(0, 1, 0, 1, mode='rgba')
                Line(points=self.point_log)
        print("Mouse move", touch)

    def on_touch_up(self, touch):
        print("Mouse up", touch)

    def _keyboard_closed(self):
        print('My keyboard have been closed!')
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print('The key', keycode, 'have been pressed')
        print(' - text is %r' % text)
        print(' - modifiers are %r' % modifiers)

        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()

        # Return True to accept the key. Otherwise, it will be used by
        # the system.
        return True


        print("key up", scancode[1])
        #print('The key', key, 'have been released')
        #print(' - scancode is %r' % scancode)
        #print(' - codepoint are %r' % codepoint)

        return True




class MyApp_2(App):
    def build(self):
        return Touch()

class MyApp(App):
    def build(self):
        return Label(text="Hello World")

if __name__ == '__main__':
    MyApp_2().run()

