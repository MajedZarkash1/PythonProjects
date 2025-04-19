# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class HabitTrackerApp(App):
    def build(self):
        self.habits = []
        
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Title
        title = Label(text='Habit Tracker', font_size=32, size_hint=(1, 0.2))
        main_layout.add_widget(title)
        
        # Add habit input
        self.input_habit = TextInput(hint_text='Enter a new habit...', size_hint=(1, 0.1))
        main_layout.add_widget(self.input_habit)

        # Add habit button
        add_button = Button(text='Add Habit', size_hint=(1, 0.1))
        add_button.bind(on_press=self.add_habit)
        main_layout.add_widget(add_button)

        # Scroll area for habits
        self.scrollview = ScrollView(size_hint=(1, 0.6))
        self.habit_list = GridLayout(cols=1, size_hint_y=None, spacing=10)
        self.habit_list.bind(minimum_height=self.habit_list.setter('height'))
        self.scrollview.add_widget(self.habit_list)
        main_layout.add_widget(self.scrollview)

        # Reset all habits button
        reset_button = Button(text='Reset Habits (New Day)', size_hint=(1, 0.1), background_color=(1, 0.3, 0.3, 1))
        reset_button.bind(on_press=self.reset_habits)
        main_layout.add_widget(reset_button)

        return main_layout

    def add_habit(self, instance):
        habit_text = self.input_habit.text.strip()
        if habit_text:
            habit_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
            habit_label = Label(text=habit_text)
            habit_button = Button(text='Mark Done', size_hint=(0.3, 1))

            def mark_done(btn):
                habit_label.color = (0, 1, 0, 1)  # Green color
                btn.disabled = True
                btn.text = 'Done'

            habit_button.bind(on_press=mark_done)
            habit_layout.add_widget(habit_label)
            habit_layout.add_widget(habit_button)
            self.habit_list.add_widget(habit_layout)
            self.habits.append((habit_label, habit_button))
            self.input_habit.text = ''

    def reset_habits(self, instance):
        for label, button in self.habits:
            label.color = (1, 1, 1, 1)  # Reset to white color
            button.disabled = False
            button.text = 'Mark Done'

if __name__ == '__main__':
    HabitTrackerApp().run()
