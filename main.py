#: -*- encoding: utf-8 -*-

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder

root = Builder.load_string('''

GridLayout:
    cols: 1
    ProgressBar:
        id: progressbar
        max: 100
    BoxLayout:
        orientation: 'horizontal'
        size_hint: 1, None
        height: '70dp'
        Button:
            text: '-'
            on_release: progressbar.value -= 10
        Button:
            text: '+'
            on_release: progressbar.value += 10
''')

class ProgressBarTestApp(App):

    def build(self):
        return root

    
if __name__ == '__main__':
    ProgressBarTestApp().run()