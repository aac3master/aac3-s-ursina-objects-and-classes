from ursina import *
import sys

class Script(Entity):
    '''''Script entity
    used to create in map script
    input code by using    content='your python code'
    '''''
    def __init__(self, content = '', auto_play = False, **kwargs):
        super().__init__(
            model = '',
            **kwargs
            )
        self.content = content
        self.auto_play = auto_play
        if self.auto_play == True:
            self.use()
    def use(self):
        if self.content == '':
            return
    def use(self):
        exec(self.content)

class FUi(Entity):
    '''''Fast Ui entity
    used to create menu UI fast
    if you dont want to change text and image just input pl_act = 'your python code'
    '''''
    def __init__(self, bg_texture = '', pl_txt = 'Play', quit_act = 'application.quit()', pl_tt = '', pl_act = '', pl_img = '', quit_txt = 'Quit', quit_tt = '', quit_img = '', game_name = '''barakuda engine''', **kwargs):
        super().__init__(
            model = '',
            **kwargs
            )
        self.background_texture = bg_texture
        self.pl_txt = pl_txt
        self.pl_act = pl_act
        self.quit_txt = quit_txt
        self.pl_tt = pl_tt
        self.pl_img = pl_img
        self.quit_txt = quit_txt
        self.quit_act = quit_act
        self.quit_tt = quit_tt
        self.quit_img = quit_img
        self.game_name = game_name
    def show(self):

        background = Sprite(self.background_texture)
        play_button = Button(text=self.pl_txt, color=color.azure, icon=self.pl_img, radius=.10, x=-0.81,
                             y=0.25)
        play_button.on_click = self.on_play_pressed
        play_button.fit_to_text()
        play_button.tooltip = Tooltip(self.pl_tt)
        exit_button = Button(text=self.quit_txt, color=color.azure, icon=self.quit_img, radius=.10, x=-0.81,
                             y=-0.2)
        exit_button.on_click = self.on_quit_pressed  # without parentheses!
        exit_button.fit_to_text()
        exit_button.tooltip = Tooltip(self.quit_tt)
        Text(self.game_name, font='unifont.ttf', scale=6, origin=(0, 0), x=0.10, y=0.40)
    def on_play_pressed(self):
        exec(self.pl_act)

    def on_quit_pressed(self):
        exec(self.quit_act)


class Dynamic_Audio(Audio):
    '''''Script entity
    used to create in map script
    input code by using    content='your python code'
    '''''
    def __init__(self, **kwargs):
        super().__init__(
            model = 'cube',
            color = color.red,
            **kwargs
            )
    def update(self):
        self.volume = self.volume - distance(camera, self)



if __name__ == '__main__':
    app = Ursina()
    Script(content='print("work")', auto_play=True)
    #EditorCamera()
    Ui = FUi(bg_texture = 'shore', pl_txt = 'Play', pl_tt = 'play', pl_act = 'print("play pressed")', pl_img = '', quit_txt = 'Quit', quit_act='application.quit()', quit_tt = '', quit_img = '', game_name = '''Ursina Stuff''')
    Ui.show()
    app.run()
