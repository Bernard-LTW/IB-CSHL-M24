#kivy_start
from kivymd.app import MDApp
class test1(MDApp):
    def build(self):
        return
    def hello_world(self):
        print("Hello World")
        self.root.ids.label.text = "Clicked!"

demonstration = test1()
demonstration.run()