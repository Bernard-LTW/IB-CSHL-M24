# Quiz 042

## Prompt
Code the GUI according to the given image(Light/Dark Mode).

HL: Code the functionality of the game.

## Code Structure

### Python File
```.py
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
```

### KV File
```.kv
ScreenManager:
    id:screenmanager
    MysteryA:
        name: "MysteryA"
    MysteryB:
        name: "MysteryB"

<MysteryA>:
    name: "MysteryA"
    MDBoxLayout:
        orientation: "vertical"
        MDLabel:
            id: label1
            text: "Welcome"
            halign: "center"
        MDRaisedButton:
            text: "Click Me"
            on_press: app.root.current = "MysteryB"
            on_press: root.messageA()

<MysteryB>:
    name: "MysteryB"
    MDBoxLayout:
        orientation: "vertical"
        MDLabel:
            id: label2
            text: "This is mystery B. you pressed a button"
            halign: "center"
        MDRaisedButton:
            text: "Click Me"
            on_press: app.root.current = "MysteryA"
```

## Evidence

![](/Assets/Quiz042_Evidence.jpg)
*Fig.1* **Image showing GUI of program**

