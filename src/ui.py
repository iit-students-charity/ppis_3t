from kivy.app import App
from kivy.config import Config
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.lang import Builder


Builder.load_string("""
<MenuScreen>:
    Button:
        text: 'PLAY'
        on_press: root.manager.current = 'gw'
        font_size: 50
        background_color: [.20, .24, .33, 1]
        background_normal: ""
        background_down: ""

<GW>:
    Game_Window:
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class GW(Screen):
    pass


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
    pos_x = 0
    pos_y = 0
    blocked = False

    def __init__(self, p_x, p_y):
        super(Cell, self).__init__()
        self.font_size = 50
        self.pos_x = p_x
        self.pos_y = p_y
        self.background_color = [.20, .24, .33, 1]
        self.background_normal = ""
        self.background_down = ""

class Field(GridLayout):
    switcher = 0
    cols = 5
    table = []

    def __init__(self, **kwargs):
        super(Field, self).__init__(**kwargs)
        self.spacing = 5
        self.size_hint = (.72, .95)
        self.halign = "center"

        for x in range(self.cols):
            self.table.append([])
            for y in range(self.cols):
                self.bt = Cell(x, y)
                self.bt.bind(on_press = self.switch)
                self.add_widget(self.bt)
                self.table[x].append(None)

        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(
                size = (540, 474),
                pos = (130,38)
            )        

    def switch(self, instance):
        if instance.blocked == False:
            if self.switcher == 0:
                instance.text = "X"
                instance.color = [.41, .53, .64, 1]
                self.switcher = 1
                self.table[instance.pos_x][instance.pos_y] = True
                
            else:
                instance.text = "O"
                instance.color = [.95, .54, .57, 1]
                self.switcher = 0
                self.table[instance.pos_x][instance.pos_y] = False
            instance.blocked = True

            for a in range(5):
                print(self.table[a])
            print(" ")


class Score_bar(BoxLayout):

    score_x = 5
    score_o = 2

    def __init__(self, **kwargs):
        super(Score_bar, self).__init__(**kwargs)
        self.size_hint = (1, .1)
        self.add_widget(
            Label(
                text = "Player X",
                size_hint = (.5, 1),
                font_size = 30,
                color = [.41, .53, .64, 1]
            )
        )
        gl = GridLayout(cols = 3)
        gl.add_widget(
            Label(
                text = str(self.score_x),
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
                text = str(self.score_o),
                halign = "left",
                text_size = (230, 40),
                font_size = 30,
                color = [.95, .54, .57, 1]
            )
        )
        self.add_widget(gl)
        self.add_widget(
            Label(
                text = "Player O",
                size_hint = (.5, 1),
                font_size = 30,
                color = [.95, .54, .57, 1]
            )
        )


class Game_Window(BoxLayout):

    def __init__(self, **kwargs):
        super(Game_Window, self).__init__(**kwargs)
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
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GW(name='gw'))
        self.icon = 'image/icon.png'
        self.title = 'Tic-Tac-Toe'
        return sm


if __name__ == "__main__":
    TickTackToeApp().run()