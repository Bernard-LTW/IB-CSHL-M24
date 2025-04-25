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
