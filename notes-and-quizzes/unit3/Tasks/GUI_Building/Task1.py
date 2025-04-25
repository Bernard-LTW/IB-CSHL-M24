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