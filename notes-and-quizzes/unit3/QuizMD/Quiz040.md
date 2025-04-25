# Quiz 040

## Prompt
Code the program and GUI according to the given image.

## Code Structure

### Python File
```.py
#2023-01-31 Quiz 040
from kivymd.app import MDApp
class Quiz040(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        return
    def change_appearance(self):
        print(self.root.ids.main_screen.md_bg_color)
        if self.root.ids.main_screen.md_bg_color == [1.0, 1.0, 1.0, 1.0]:
            self.root.ids.main_screen.md_bg_color = "#000000"
            self.root.ids.changebutton.text_color = 1,1,1,1
            self.root.ids.name.text_color = 1, 1, 1, 1
            self.root.ids.changebutton.text = "Light Mode"
        else:
            self.root.ids.main_screen.md_bg_color = "#FFFFFF"
            self.root.ids.changebutton.text_color = 0,0,0,1
            self.root.ids.name.text_color = 0, 0, 0, 1
            self.root.ids.changebutton.text = "Dark Mode"

quiz40 = Quiz040()
quiz40.run()
```

### KV File
```.kv
#2023-01-31 Quiz040
MDScreen:
    size:500,500
    MDBoxLayout:
        id: main_screen
        orientation:"vertical"
        md_bg_color: "#FFFFFF"
        MDLabel:
            id:name
            text: "Bernard Lee"
            halign: "center"
            font_style: "H2"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            pos_hint: {"center_x": .5, "center_y": .5}
        MDRaisedButton:
            id: changebutton
            text: "Dark Mode"
            pos_hint: {"center_x": 0.06, "center_y": 0.1}
            on_release: app.change_appearance()
```

## Evidence

![](/Assets/Quiz040_Evidence.jpg)
*Fig.1* **Image showing GUI of program**
