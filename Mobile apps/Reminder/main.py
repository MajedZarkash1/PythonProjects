import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class grid(GridLayout):
    def __init__(self, **kwargs):
        super(grid, self).__init__(**kwargs)

        #set colums
        self.cols = 2

        #add widgets
        self.add_widget(Label(text="name: "))
        #add input
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

class Myapp(App):
    def build(self):
        return grid()
    

if __name__ == '__main__':
    Myapp().run()
