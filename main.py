from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class Field(GridLayout):

     def __init__(self, **kwargs):
        super(Field, self).__init__(**kwargs)
        self.cols = 3
        self.spacing = 3
        self.bt_0_0 = Button(text = "00")
        self.bt_0_1 = Button(text = "01")
        self.bt_0_2 = Button(text = "02")
        self.bt_1_0 = Button(text = "10")
        self.bt_1_1 = Button(text = "11")
        self.bt_1_2 = Button(text = "12")
        self.bt_2_0 = Button(text = "20")
        self.bt_2_1 = Button(text = "21")
        self.bt_2_2 = Button(text = "22")

        self.add_widget(self.bt_0_0)
        self.add_widget(self.bt_0_1)
        self.add_widget(self.bt_0_2)
        self.add_widget(self.bt_1_0)
        self.add_widget(self.bt_1_1)
        self.add_widget(self.bt_1_2)
        self.add_widget(self.bt_2_0)
        self.add_widget(self.bt_2_1)
        self.add_widget(self.bt_2_2)

class Score_bar(BoxLayout):

    def __init__(self, **kwargs):
        super(Score_bar, self).__init__(**kwargs)
        self.size_hint = (1, .10)
        self.add_widget(Label(text = "Player X", halign = "left", size_hint = (.5, 1), font_size = 30))
        self.add_widget(Label(text = "2:1", font_size = 30))
        self.add_widget(Label(text = "Player O", halign = "left", size_hint = (.5, 1), font_size = 30))

class TickTackToeApp(App):

    def build(self):
        bl_1 = BoxLayout(orientation = 'vertical', padding = 25)

        bl_1.add_widget( Score_bar() )
        bl_1.add_widget( Field() )

        return bl_1

if __name__ == "__main__":
    TickTackToeApp().run()