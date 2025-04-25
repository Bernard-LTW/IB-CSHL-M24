# GUI Building Task

## Task 1: Currency Conversion

### Python Code
```py
#GUI Building Task 1 - Python
from kivymd.app import MDApp
#Conversion rates are based on rated provided by Yahoo Finance on 2023-01-29
class task1(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.original = 0
        self.output = 0
    def build(self):
        return

    def convert_currency(self, choice:str):
        if self.root.ids.original_in.text.isdigit():
            if 'USD' in choice:
                self.output = float("{:.2f}".format(int(self.root.ids.original_in.text)*0.13))
            elif 'JPY' in choice:
                self.output = float("{:.2f}".format(int(self.root.ids.original_in.text)*17))

            self.root.ids.final_label.text = f"{self.output} {choice}"
        else:
            self.root.ids.final_label.text = "Invalid Input"
            self.root.ids.original_in.text = ""
            self.root.ids.final_label.text_color = (1,0,0,1)



hey = task1()
hey.run()
```

### KV Code
```kv
#GUI Building Task 1 - KivyMD
Screen:
    size: 500,500
    MDBoxLayout:
        id: main_box
        orientation: 'vertical'
        size_hint:1,.8
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDLabel:
            text:"Currency Converter"
            halign: 'center'
            font_style: 'H3'
            text_color: "#000000"
            size_hint: 1, .2
            pos_hint: {'center_x':0.5}

        MDTextField:
            id: original_in
            hint_text: "Enter Amount in HKD"
            helper_text: "Integers Only"
            helper_text_mode: "on_focus"
            icon_right: "cash"
            icon_right_color: app.theme_cls.primary_color
            pos_hint: {'center_x':0.5}
            size_hint: .7, .1

        MDBoxLayout:
            id: currency_box
            orientation: 'horizontal'
            size_hint: 1, .4
            pos_hint: {'center_x':0.5}
            padding: 10
            spacing: 10
            MDLabel:
                id : hint_label
                text: "Click to convert"
                halign: 'center'
                font_style: 'Overline'
                text_color: "#000000"
                size_hint: .3, 1
                pos_hint: {'center_x':0.2, 'center_y':0.5}
            MDBoxLayout:
                id: button_output_box
                orientation:"vertical"
                size_hint: .3, 1
                MDBoxLayout:
                    id: buttons_box
                    orientation: "horizontal"
                    size_hint: .7, 1
                    pos_hint: {'center_x':0.7, 'center_y':0.9}
                    MDChip:
                        text: "USD"
                        pos_hint: {"center_x": 0.25, "center_y": .25}
                        on_press: app.convert_currency("USD")
                        md_bg_color:"#002B41"
                        text_color: "#FFFFFF"
                    MDChip:
                        text: "JPY"
                        pos_hint: {"center_x": 0.75, "center_y": .25}
                        on_press: app.convert_currency("JPY")
                        md_bg_color:"#F20021"
                MDLabel:
                    id: final_label
                    halign: 'center'
                    font_style: 'H5'
                    text_color: "#000000"
                    size_hint: .3, 1
                    pos_hint: {'center_x':0.6}
                    font_size:80
```

### Screenshot
![](/Tasks/GUI_Building/task1.jpg)
*Fig.1* **Image showing GUI of Task 1**

## Task 2: Bit/Byte Converter

### Python Code
```py
#GUI Building Task 2 - Python
from kivymd.app import MDApp
class task2(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        return
    def byte2bit(self):
        if self.root.ids.byte_in.text.isdigit():
            self.output = float("{:.2f}".format(int(self.root.ids.byte_in.text)*8))
            self.root.ids.output_label.text = f"{self.output} bits"
        else:
            self.root.ids.output_label.text = "Invalid Input"
            self.root.ids.byte_in.text = ""
            self.root.ids.output_label.text_color = (1,0,0,1)
    def bit2byte(self):
        if self.root.ids.bit_in.text.isdigit():
            self.output = float("{:.2f}".format(int(self.root.ids.bit_in.text)/8))
            self.root.ids.output_label.text = f"{self.output} bytes"
        else:
            self.root.ids.output_label.text = "Invalid Input"
            self.root.ids.bit_in.text = ""
            self.root.ids.output_label.text_color = (1,0,0,1)

hey = task2()
hey.run()
```

### KV Code
```kv
#GUI Building Task 2 - KivyMD
Screen:
    size: 500,500
    MDBoxLayout:
        id: main_box
        orientation: 'vertical'
        size_hint:1,.8
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDLabel:
            text: 'Bit/Byte Converter'
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 0,0,0,1
            font_style: 'H4'
            size_hint: 1, .2
        MDBoxLayout:
            id: byte_box
            orientation: 'horizontal'
            size_hint: 1, .2
            padding: 10
            MDTextField:
                id: byte_in
                hint_text: 'Enter Bytes'
                helper_text: 'Enter Bytes'
                helper_text_mode: 'on_focus'
            MDRaisedButton:
                id: byte_button
                text: 'Convert to Bits'
                on_press: app.byte2bit()
        MDBoxLayout:
            id: bit_box
            orientation: 'horizontal'
            size_hint: 1, .2
            padding: 10
            MDTextField:
                id: bit_in
                hint_text: 'Enter Bits'
                helper_text: 'Enter Bits'
                helper_text_mode: 'on_focus'
            MDRaisedButton:
                id: bit_button
                text: 'Convert to Bytes'
                on_press: app.bit2byte()

        MDLabel:
            id: output_label
            text: 'Ready!'
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 0,0,0,1
            font_style: 'H4'
            size_hint: 1, .2
```

### Screenshot
![](/Tasks/GUI_Building/task2.jpg)
*Fig.2* **Image showing GUI of Task 2**

