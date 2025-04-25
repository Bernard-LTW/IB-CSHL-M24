#2022-02-03 Quiz042.md
#Code the program according to the UML diagram provided.
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class MysteryA(MDScreen):
    def messageA(self):
        print("Printing from MysteryA")
        self.ids.label1.text = "This is mystery A. you pressed a button"

class MysteryB(MDScreen):
    def messageB(self):
        print("Printing from MysteryB")

class Quiz042(MDApp):
    def build(self):
        return


boi = Quiz042()
boi.run()
