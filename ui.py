from kivy.app import App
from kivy.config import Config
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


Config.set(
        'graphics',
        'minimum_width',
        '800'
    )
Config.set(
        'graphics',
        'minimum_height',
        '600'
    )
Config.set(
        'graphics',
        'resizable',
        '0'
    )


class Cell(Button):

    def __init__(self):
        super(Cell, self).__init__()
        self.on_press = self.x_add
        self.font_size = 50
        self.background_color = [.20, .24, .33, 1]
        self.background_normal = ""
        self.background_down = ""

    def x_add(self):
        self.text = "X"


class Field(GridLayout):

    def __init__(self, **kwargs):
        super(Field, self).__init__(**kwargs)
        self.cols = 3
        self.spacing = 5
        self.size_hint = (.72, .95)
        self.halign = "center"
        self.bt_0_0 = Cell()
        self.bt_0_1 = Cell()
        self.bt_0_2 = Cell()
        self.bt_1_0 = Cell()
        self.bt_1_1 = Cell()
        self.bt_1_2 = Cell()
        self.bt_2_0 = Cell()
        self.bt_2_1 = Cell()
        self.bt_2_2 = Cell()
        self.add_widget(self.bt_0_0)
        self.add_widget(self.bt_0_1)
        self.add_widget(self.bt_0_2)
        self.add_widget(self.bt_1_0)
        self.add_widget(self.bt_1_1)
        self.add_widget(self.bt_1_2)
        self.add_widget(self.bt_2_0)
        self.add_widget(self.bt_2_1)
        self.add_widget(self.bt_2_2)
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(
                size = (540, 474),
                pos = (130,38)
            )


class Score_bar(BoxLayout):

    def __init__(self, **kwargs):
        super(Score_bar, self).__init__(**kwargs)
        self.size_hint = (1, .1)
        self.add_widget(
            Label(
                text="Player X",
                size_hint = (.5, 1),
                font_size = 30,
                color = [.41, .53, .64, 1]
            )
        )
        gl = GridLayout(cols = 3)
        gl.add_widget(
            Label(
                text="2",
                halign = "right",
                text_size = (230, 40),
                font_size = 30,
                color = [.40, .52, .63, 1]
            )
        )
        gl.add_widget(
            Label(
                text = ":",
                font_size = 30
            )
        )
        gl.add_widget(
            Label(
                text="1",
                halign = "left",
                text_size = (230, 40),
                font_size = 30,
                color = [.95, .54, .57, 1]
            )
        )
        self.add_widget(gl)
        self.add_widget(
            Label(
                text="Player O",
                size_hint = (.5, 1),
                font_size = 30,
                color = [.95, .54, .57, 1]
            )
        )


class Window(BoxLayout):

    def __init__(self, **kwargs):
        super(Window, self).__init__(**kwargs)
        self.padding = 25
        self.orientation = "vertical"
        self.add_widget(Score_bar())
        al_field = AnchorLayout(anchor_x='center', anchor_y='center')
        al_field.add_widget(Field())
        self.add_widget(al_field)
        with self.canvas.before:
            Color(.20, .24, .33, 1)
            self.rect = Rectangle(
                size=(800, 600),
                pos=self.pos
            )


class TickTackToeApp(App):

    def build(self):
        win = Window()
        return win


if __name__ == "__main__":
    TickTackToeApp().run()
