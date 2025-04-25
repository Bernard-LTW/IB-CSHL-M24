# Quiz 039

## Prompt
Code the program and GUI according to the given image.

## Code Structure

### Python File
```.py
#2023-01-27 Quiz 039

from kivymd.app import MDApp
class Quiz039(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0
    def build(self):
        return
    def add(self):
        self.count += 1
        self.root.ids.counter_label.text = f"Count = {self.count}"

quiz39 = Quiz039()
quiz39.run()
```

### KV File
```.kv
#2023-01-27 Quiz 039
Screen:
    size: 500,500
    MDBoxLayout:
        id: main_box
        orientation: 'horizontal'
        size_hint:.7,.3
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        md_bg_color: "#a8dadc"

        MDLabel:
            id : counter_label
            font_size: '34'
            size_hint:.5,1
            text: 'Ready!'
        MDRaisedButton:
            id: up
            text: 'Count +1'
            font_size: '34'
            size_hint:.5,1
            on_press: app.add()
```

## Evidence

![](/Assets/Quiz039_Evidence.jpg)
*Fig.1* **Image showing GUI of program**

## UML Diagram
![](/Assets/Quiz039_UML.jpeg)
*Fig.2* **UML Diagram of Program**
