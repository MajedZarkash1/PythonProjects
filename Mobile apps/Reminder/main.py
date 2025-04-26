from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class Task(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(orientation='horizontal', size_hint_y=None, height=70, **kwargs)
        self.label = Label(text=text, size_hint_x=0.7)
        self.done_button = Button(text="Done", size_hint_x=0.15, on_press=self.mark_done)
        self.delete_button = Button(text="Remove", size_hint_x=0.15, on_press=self.delete_task)
        self.add_widget(self.label)
        self.add_widget(self.done_button)
        self.add_widget(self.delete_button)

    def mark_done(self, instance):
        self.label.text = "[s]{}[/s]".format(self.label.text)  # strike-through
        self.label.markup = True

    def delete_task(self, instance):
        self.parent.remove_widget(self)

class ReminderApp(App):
    def build(self):
        self.root = BoxLayout(orientation='vertical')

        self.task_input = TextInput(hint_text="Enter a new task...", size_hint_y=None, height=50, multiline=False)
        add_button = Button(text="Add Task", size_hint_y=None, height=50)
        add_button.bind(on_press=self.add_task)

        self.task_list_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.task_list_layout.bind(minimum_height=self.task_list_layout.setter('height'))

        scroll_view = ScrollView()
        scroll_view.add_widget(self.task_list_layout)

        self.root.add_widget(self.task_input)
        self.root.add_widget(add_button)
        self.root.add_widget(scroll_view)

        return self.root

    def add_task(self, instance):
        task_text = self.task_input.text.strip()
        if task_text:
            task = Task(task_text)
            self.task_list_layout.add_widget(task)
            self.task_input.text = ""

if __name__ == "__main__":
    ReminderApp().run()
