import kivy #import kivy

from kivy.app import App #Main
from kivy.uix.label import Label #import Label
from kivy.uix.button import Button #import Button
from kivy.uix.gridlayout import GridLayout

class MyApp(GridLayout): #the code should start here

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3

        self.add_widget(Label(text="Hello I am Label"))
        self.add_widget(Button(text="Hello I am Button"))
        

    
if __name__ == '__main__':
    MyApp().run() #the code should end here