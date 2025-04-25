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