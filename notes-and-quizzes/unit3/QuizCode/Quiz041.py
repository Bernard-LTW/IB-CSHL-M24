#2023-02- Quiz 041
#KivyMD Tic Tac Toe
from kivymd.app import MDApp
class Quiz041(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.values = [0,0,0,0,0,0,0,0,0]
        self.player = "X"

        # "0" means empty
        # "1" means X
        # "2" means O

    def build(self):
        return

    def button_press(self,button_id):
        print(button_id)
        current_player = self.player
        temp = "self.root.ids.button" + button_id
        current_button = eval(temp)
        #current_button.disabled = True
        if self.values[int(button_id)-1] == 0:
            current_button.text = current_player
            if current_player == "X":
                self.player = "O"
                current_button.md_bg_color = "#B0D7FF"
                self.values[int(button_id)-1] = 1
            else:
                self.player = "X"
                current_button.md_bg_color = "#EAE8FF"
                self.values[int(button_id)-1] = 2


        print(self.values)

        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for indices in winning_combinations:
            if all(self.values[i] == self.values[indices[0]] and self.values[i] != 0 for i in indices):
                print(f"Winner is {current_player}")
                self.root.ids.label2.text = f"Winner is {current_player}"
                break
        else:
            print("No Winner Yet")
            self.root.ids.label2.text = f"Current Player: {self.player}"

    def reset(self):
        self.values = [0,0,0,0,0,0,0,0,0]
        self.player = "X"
        for i in range(1,10):
            temp = "self.root.ids.button" + str(i)
            current_button = eval(temp)
            current_button.text = ""
            current_button.md_bg_color = "grey"
            #current_button.disabled = False
        self.root.ids.label2.text = f"Current Player: {self.player}"


tictactoe = Quiz041()
tictactoe.run()
