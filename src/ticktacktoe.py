# kivy.reqire("1.8.0")
from kivy.app import App
from kivy.config import Config
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from functools import partial
from IPython import embed

import mysql.connector
import random

class Cell(Button):
    pos_x = 0
    pos_y = 0
    blocked = False

    def __init__(self, p_x, p_y):
        super(Cell, self).__init__()
        self.pos_x = p_x
        self.pos_y = p_y


class WinCond():
    winner = ''

    def win(self, table):
        embed()
        for a in range(len(table)):
            if None not in table[a]:
                horizont_sum = 0
                for b in range(len(table)):
                    horizont_sum += table[a][b]

                if horizont_sum == len(table):
                    self.winner = 'x'

                elif horizont_sum == 0:
                    self.winner = 'o'
        self.vertical(table)
        self.random_place(table)

    def vertical(self, table):
        table_transp = list(zip(*table))

        for a in range(len(table_transp)):
            if None not in table_transp[a]:
                horizont_sum = 0
                for b in range(len(table_transp)):
                    horizont_sum += table_transp[a][b]

                if horizont_sum == len(table_transp):
                    self.winner = 'x'

                if horizont_sum == 0:
                    self.winner = 'o'
        self.diagonal_right(table)

    def diagonal_right(self, table):
        diagonal_right_sum = 0
        count = 0
        for a in range(len(table)):
            if table[a][a] is not None:
                count += 1
        if count == len(table):
            for a in range(len(table)):
                if table[a][a] is not None:
                    diagonal_right_sum += table[a][a]

            if diagonal_right_sum == len(table):
                self.winner = 'x'

            if diagonal_right_sum == 0:
                self.winner = 'o'
        self.diagonal_left(table)

    def diagonal_left(self, table):
        diagonal_left_sum = 0
        count = 0
        is_pat = 0
        for a in range(len(table) - 1, -1, -1):
            if table[len(table) - 1 - a][a] is not None:
                count += 1
        if count == len(table):
            for a in range(len(table)):
                if table[len(table) - 1 - a][a] is not None:
                    diagonal_left_sum += table[len(table) - 1 - a][a]

            if diagonal_left_sum == len(table):
                self.winner = 'x'

            if diagonal_left_sum == 0:
                self.winner = 'o'
        for a in range(len(table)):
            for b in range(len(table)):
                if table[a][b] is not None:
                    is_pat += 1
        if is_pat == len(table)**2:
            self.winner = 'n'

    def random_place(self, table):
        embed()
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if table[x][y] is None:
            self.random_place(table)
        else:
            table[x][y] = 0


class ScoreBar(BoxLayout):
    pass


class Field(GridLayout):
    switcher = 0
    cols = 3
    table = []
    wc = WinCond()


class Label_x(Label):
    score = 0


class Label_y(Label):
    score = 0


class Text_Input(TextInput):
    pass

class Game(BoxLayout):
    name_x = ""
    name_o = ""

    def __init__(self, **kwargs):
        super(Game, self).__init__()
        bl_top = BoxLayout(orientation = 'vertical', size_hint = (1, .95))
        bl_bott = BoxLayout(orientation = 'horizontal', size_hint = (1, .05))

        lb_x = Label_x()
        lb_x.text = str(0)
        lb_y = Label_y()
        lb_y.text = str(0)
        sb_g = ScoreBar()
        sb_g.add_widget(lb_x)
        sb_g.add_widget(lb_y)
        fl_g = Field()
        al = AnchorLayout()
        al.add_widget(fl_g)

        bl_top.add_widget(sb_g)
        bl_top.add_widget(al)

        bt_cls = BtCls()
        bt_cls.on_press = partial(self.clear_screen, fl_g, bl_bott, fl_g, lb_x, lb_y)

        bl_bott.add_widget(bt_cls)

        self.add_widget(bl_top)
        self.add_widget(bl_bott)
        for x in range(fl_g.cols):
            fl_g.table.append([])
            for y in range(fl_g.cols):
                bt = Cell(x, y)
                bt.on_press = partial(self.callback, bt, fl_g, lb_x, lb_y)
                fl_g.add_widget(bt)
                fl_g.table[x].append(None)

    def callback(self, bt, fl, lb_x, lb_y):
        if not bt.blocked:
            if fl.switcher == 0:
                bt.text = "X"
                bt.color = [.41, .53, .64, 1]
                fl.switcher = 1
                fl.table[bt.pos_x][bt.pos_y] = 1
            else:
                bt.text = "O"
                bt.color = [.95, .54, .57, 1]
                fl.switcher = 0
                fl.table[bt.pos_x][bt.pos_y] = 0
            bt.blocked = True
        fl.wc.win(fl.table)
        if fl.wc.winner == 'x':
            lb_x.score += 1
            lb_x.text = str(lb_x.score)
            self.clear_field(fl)
        elif fl.wc.winner == 'o':
            lb_y.score += 1
            lb_y.text = str(lb_y.score)
            self.clear_field(fl)
        elif fl.wc.winner == 'n':
            self.clear_field(fl)

        fl.wc.winner = ''

    def clear_field(self, fl):
        for el in fl.children:
            el.text = ''
            el.blocked = False
        for i in range(fl.cols):
            for j in range(fl.cols):
                fl.table[i][j] = None
        return

    def clear_screen(self, fl_g, bl_bott, fl, lb_x, lb_y):
        for el in fl.children:
            el.text = ''
            el.blocked = False
        for i in range(fl.cols):
            for j in range(fl.cols):
                fl.table[i][j] = None

        lb_x.text = str(0)
        lb_y.text = str(0)

        bl_bott.clear_widgets()
        ti = TextInputer()
        bt = EnterBt()
        bt.on_press = partial(self.input_x, fl_g, fl, lb_x, lb_y, bl_bott, bt, ti, self.name_x, self.name_o)
        bl_bott.add_widget(ti)
        bl_bott.add_widget(bt)
        return

    def input_x(self, fl_g, fl, lb_x, lb_y, bl_bott, bt, ti, name_x, name_o):
        self.name_x = ti.text
        ti.text = "O's name"
        RecordPlayers().db_connect(self.name_x, lb_x.score)
        print(self.name_x)
        bt.on_press = partial(self.input_o, fl_g, fl, lb_x, lb_y, bl_bott, bt, ti, self.name_o)
        return

    def input_o(self, fl_g, fl, lb_x, lb_y, bl_bott, bt, ti, name_o):
        self.name_o = ti.text
        RecordPlayers().db_connect(self.name_o, lb_y.score)
        print(self.name_o)
        bt_cls = BtCls()
        bt_cls.on_press = partial(self.clear_screen, bl_bott, fl_g, lb_x, lb_y)
        bl_bott.clear_widgets()
        bl_bott.add_widget(bt_cls)
        return

class RecordPlayers():
    def db_connect(self, name, score):
        playersdb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="playersdatabase"
        )

        players = playersdb.cursor()

        sql = "INSERT INTO users (name, wins) VALUES (%s, %s)"
        val = (name, score)
        players.execute(sql, val)

        playersdb.commit()

        print(players.rowcount, "record inserted.")

class TextInputer(TextInput):
    pass

class BtCls(Button):
    pass

class EnterBt(Button):
    pass


class MenuScreen(Screen):
    pass


class GameScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


class TickTackToeApp(App):
    def build(self):
        sm = ScreenManagement()
        self.icon = 'image/icon.png'
        self.title = 'Tic-Tac-Toe'
        return sm


if __name__ == "__main__":
    TickTackToeApp().run()
