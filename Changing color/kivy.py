from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

colors = ["gray", "yellow", "white", "green", "red", "brown"]
current_color = 0

class MyApp(App):
    def build(self):
        self.current_color = 0
        self.colors = colors

        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        self.label = Label(text='Click to Change the Color', font_size=24)
        self.button = Button(text='Change Background', size_hint=(1, 0.3), on_press=self.change_color)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)

        return self.layout

    def change_color(self, instance):
        self.layout.background_color = self.colors[self.current_color]
        self.label.color = (0,0,0,1)  # black text
        self.layout.canvas.before.clear()
        with self.layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            color = self.colors[self.current_color]
            Color(*self.kivy_color(color))
            Rectangle(pos=self.layout.pos, size=self.layout.size)
        self.current_color = (self.current_color + 1) % len(self.colors)

    def kivy_color(self, color_name):
        from kivy.utils import get_color_from_hex
        from kivy.utils import get_color_from_string
        try:
            return get_color_from_string(color_name)
        except:
            return (1, 1, 1, 1)

MyApp().run()
