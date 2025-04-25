#Recipe GUI

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
class IntroScreen(MDScreen):
    pass

class PrepareDough(MDScreen):
    pass
class PrebakeDough(MDScreen):
    pass

class PutOnToppings(MDScreen):
    pass

class BakePizza(MDScreen):
    pass

class EatPizza(MDScreen):
    pass

class recipe(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        return

my_app = recipe()
my_app.run()