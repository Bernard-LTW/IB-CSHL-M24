# VocabAppMain.py
import re
from kivy.logger import Logger
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import MDScreen
from db_manager import database_handler
from models import Users, Vocabulary
from secure_password import hash_password
global current_user
global vocab_list


class LoginScreen(MDScreen):
    def login(self):
        print(f"Username: {self.ids.uname.text} Password: {self.ids.pwd.text}")
        username = self.ids.uname.text
        password = self.ids.pwd.text
        if VocabApp.db.login_check(username, password):
            Logger.info("Login successful")
            self.parent.current = "LandingScreen"
            global current_user
            current_user = VocabApp.db.session.query(Users).filter_by(username=username).first()
            Logger.info(f"Current user: {current_user.username}")
            self.ids.uname.text = ""
            self.ids.pwd.text = ""
        else:
            Logger.info("Login failed")
            self.ids.uname.text = ""
            self.ids.pwd.text = ""
            dialog = MDDialog(
                title="Error",
                text="Login failed",
                size_hint=(0.8, 0.3),
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=lambda x: dialog.dismiss()
                    )
                ]
            )
            dialog.open()
            print("Login failed")

class RegisterScreen(MDScreen):
    def register(self):
        print(f"Username: {self.ids.uname.text} Email:{self.ids.email.text} Password: {self.ids.pwd.text}")
        uname = self.ids.uname.text
        email = self.ids.email.text
        pwd = self.ids.pwd.text
        cpwd = self.ids.cpwd.text
        # Regular expression pattern for email validation
        email_pattern = r"[^@]+@[^@]+\.[^@]+"
        # Validate the email format
        if not re.match(email_pattern, email):
            # Show an error message
            self.ids.email.error = True
            self.ids.email.helper_text = "Invalid email format"
            self.ids.email.helper_text_mode = "on_error"
            return
        if pwd != cpwd:
            print("Passwords do not match")
            self.ids.cpwd.error = True
            self.ids.cpwd.md_bg_color = "red"
        else:
            if VocabApp.db.username_exists(uname) or VocabApp.db.email_exists(email):
                # Show an error dialog
                existsdialog = MDDialog(
                    title="Error",
                    text="Username or email already exists",
                    size_hint=(0.8, 0.3),
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            on_release=lambda x: existsdialog.dismiss()
                        )
                    ]
                )
                existsdialog.open()
                return
            pwd = hash_password(pwd)
            self.ids.cpwd.error = False
            self.ids.cpwd.md_bg_color = "green"
            db = database_handler("vocab_app.db")
            db.insert_user(email, uname, pwd)
            db.close()
            successdialog = MDDialog(
                title="Success",
                text="User registered successfully",
                size_hint=(0.8, 0.3),
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=lambda x: successdialog.dismiss()
                    )
                ]
            )
            successdialog.open()

            self.parent.current = "LoginScreen"


class LandingScreen(MDScreen):
    def on_enter(self):
        global current_user
        self.ids.welcome_banner.text = f"こんにちは {current_user.username}"

    def logout(self):
        self.parent.current = "LoginScreen"
        current_user = None
class ManageVocabScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        font_name = "Roboto"
        self.checked_rows = None
        self.data_table = MDDataTable(
            size_hint=(0.9, 0.7),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            use_pagination=True,
            check=True,
            column_data=[
                ("ID", 50),
                ("Lesson", 40),
                ("Part", 40),
                ("Hiragana", 40, font_name),
                ("Katakana", 40),
                ("Definition", 40)
            ],
            row_data=[]
        )
        self.data_table.bind(on_row_press=self.on_row_press)
        self.data_table.bind(on_check_press=self.on_check_press)
        self.add_widget(self.data_table)

    def on_pre_enter(self, *args):
        self.load()

    @staticmethod
    def on_row_press(table, row):
        print(f"Row was pressed. Data is: {row.text}")

    @staticmethod
    def on_check_press(table, current_row):
        print(f"Row {current_row} was checked")

    def load(self):
        Logger.info("Loading Vocabulary from database...")
        self.data_table.row_data.clear()
        rows = VocabApp.db.get_vocab()
        try:
            for row in rows:
                temp_hiragana = f"[font=Japanese.ttc]{row.hiragana}[/font]"
                temp_katakana = f"[font=Japanese.ttc]{row.katakana}[/font]"
                row = [str(row.id), str(row.lesson), str(row.part_of_lesson), temp_hiragana, temp_katakana,
                       row.definition]
                if row not in self.data_table.row_data:
                    self.data_table.row_data.append(row)
        except Exception as e:
            Logger.error(f"Error loading vocabulary: {e}")

    def delete_vocab(self):
        checked = self.data_table.get_row_checks()
        Logger.info("Deleting vocabulary from database...")
        try:
            for row in checked:
                vocab_id = int(row[0])
                VocabApp.db.delete_vocab(vocab_id=vocab_id)
            self.load()
            deletedialog = MDDialog(
                title="Success",
                text="Vocabulary deleted successfully",
                size_hint=(0.8, 0.3),
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_press=lambda x: deletedialog.dismiss()
                    )
                ]
            )
            deletedialog.open()
        except Exception as e:
            Logger.error(f"Error deleting vocabulary: {e}")

    def enter_edit(self):
        checked = self.data_table.get_row_checks()
        if len(checked) == 1:
            vocab_id = int(checked[0][0])
            vocab = VocabApp.db.get_vocab_by_id(vocab_id=vocab_id)
            self.parent.get_screen("PerVocabManageScreen").ids.selected_lesson.text = str(vocab.lesson)
            self.parent.get_screen("PerVocabManageScreen").ids.selected_part.text = str(vocab.part_of_lesson)
            self.parent.get_screen("PerVocabManageScreen").ids.selected_hiragana.text = vocab.hiragana
            self.parent.get_screen("PerVocabManageScreen").ids.selected_katakana.text = vocab.katakana
            self.parent.get_screen("PerVocabManageScreen").ids.selected_english.text = vocab.definition
            self.parent.current = "PerVocabManageScreen"

        else:
            Logger.error("Please select only one vocabulary to edit")
            dialog = MDDialog(
                title="Warning",
                text="Please select only one vocabulary to edit",
                size_hint=(0.7, 0.3)
            )
            dialog.open()


class PerVocabManageScreen(MDScreen):
    def on_pre_enter(self, *args):
        if self.ids.selected_hiragana.text == "":
            self.ids.selected_save.on_press = self.add_vocab
        else:
            self.ids.selected_save.text = "Save Changes"
            self.ids.selected_save.on_press = self.save_changes

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = MDDialog(
            title="Warning",
            text="The vocabulary already exists in the database.",
            size_hint=(0.7, 0.3)
        )

    def add_vocab(self):
        Logger.info("Adding vocabulary to database...")
        lesson = int(self.ids.selected_lesson.text)
        part = int(self.ids.selected_part.text)
        hiragana = self.ids.selected_hiragana.text
        katakana = self.ids.selected_katakana.text
        definition = self.ids.selected_english.text

        try:
            VocabApp.db.insert_vocab(lesson, part, hiragana, katakana, definition)
            Logger.info("Vocabulary added successfully")
            save_dialog = MDDialog(
                title="Success",
                text="Vocabulary added successfully",
                size_hint=(0.7, 0.3),
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=lambda x: save_dialog.dismiss()
                    )
                ]
            )
            save_dialog.open()
            self.clear_fields()
            self.parent.current = "ManageVocabScreen"
        except Exception as e:
            Logger.error(f"Error adding vocabulary: {e}")

    def clear_fields(self):
        fields_to_clear = ['selected_lesson', 'selected_part', 'selected_hiragana', 'selected_katakana',
                           'selected_english']
        for field in fields_to_clear:
            self.ids[field].text = ""
        self.ids.selected_save.text = "Save"
        self.ids.selected_save.on_press = self.add_vocab

    def save_changes(self):
        Logger.info("Saving changes to vocabulary...")
        lesson = int(self.ids.selected_lesson.text)
        part = int(self.ids.selected_part.text)
        hiragana = self.ids.selected_hiragana.text
        katakana = self.ids.selected_katakana.text
        definition = self.ids.selected_english.text
        try:
            VocabApp.db.update_vocab(lesson, part, hiragana, katakana, definition)
            Logger.info("Vocabulary updated successfully")
            update_success = MDDialog(
                title="Success",
                text="Vocabulary updated successfully",
                size_hint=(0.7, 0.3),
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=lambda x: update_success.dismiss()
                    )
                ]
            )
            update_success.open()
            self.clear_fields()
            self.parent.current = "ManageVocabScreen"
            ManageVocabScreen.load(self.parent.get_screen("ManageVocabScreen"))
        except Exception as e:
            Logger.error(f"Error updating vocabulary: {e}")


class RandomVocabScreen(MDScreen):
    def random_vocab(self):
        global current_user
        global vocab_list
        global count
        vocab_list = []
        count = 0
        Logger.info("Choosing random vocabulary...")
        try:
            vocab = VocabApp.db.get_vocab_by_user_stats(current_user.id)
            if len(vocab) == 0:
                no_vocab = MDDialog(
                    title="Error",
                    text="There are no vocabulary statistics for this user yet",
                    size_hint=(0.7, 0.3),
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            on_release=lambda x: no_vocab.dismiss()
                        )
                    ]
                )
                no_vocab.open()
                return
            for v in vocab:
                temp = (v.hiragana, v.katakana, v.definition, v.id)
                vocab_list.append(temp)
            self.parent.get_screen("VocabCardScreen").ids.hiragana_label.text = vocab_list[count][0]
            self.parent.get_screen("VocabCardScreen").ids.katakana_label.text = vocab_list[count][1]
            self.parent.get_screen("VocabCardScreen").ids.vocab_description.text = vocab_list[count][2]
            self.parent.current = "VocabCardScreen"
        except Exception as e:
            Logger.error(f"Error choosing random vocabulary: {e}")


class VocabChooserScreen(MDScreen):
    def clear_fields(self):
        self.ids.selected_lesson.text = ""
        self.ids.selected_part.text = ""

    def choose_vocab(self):
        Logger.info("Choosing vocabulary...")
        lesson = int(self.ids.selected_lesson.text)
        part = int(self.ids.selected_part.text)
        global count
        count = 0
        global vocab_list
        try:
            vocabs = VocabApp.db.get_vocab_by_lesson_and_part(lesson, part)
            if len(vocabs) == 0:
                no_vocab = MDDialog(
                    title="Error",
                    text="There are no vocabulary in this lesson and part",
                    size_hint=(0.7, 0.3),
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            on_release=lambda x: no_vocab.dismiss()
                        )
                    ]
                )
                no_vocab.open()
                return
            for vocab in vocabs:
                temp = (vocab.hiragana, vocab.katakana, vocab.definition, vocab.id)
                print(temp)
                vocab_list.append(temp)
            self.parent.get_screen("VocabCardScreen").ids.hiragana_label.text = vocab_list[count][0]
            self.parent.get_screen("VocabCardScreen").ids.katakana_label.text = vocab_list[count][1]
            self.parent.get_screen("VocabCardScreen").ids.vocab_description.text = f"Definition: {vocab_list[count][2]}"
            self.parent.current = "VocabCardScreen"
            self.clear_fields()
        except Exception as e:
            Logger.error(f"Error choosing vocabulary: {e}")


class VocabCardScreen(MDScreen):
    def clear_array(self):
        global vocab_list
        vocab_list = []
    def next_vocab(self):
        print("Next vocab")
        global count
        global vocab_list
        if count > len(vocab_list) - 1:
            self.ids.vocab_description.text = "You have reached the end of the list"
            self.ids.katakana_label.text = ""
            self.ids.hiragana_label.text = ""
        else:
            self.parent.get_screen("VocabCardScreen").ids.hiragana_label.text = vocab_list[count][0]
            self.parent.get_screen("VocabCardScreen").ids.katakana_label.text = vocab_list[count][1]
            self.parent.get_screen("VocabCardScreen").ids.vocab_description.text = f"Definition: {vocab_list[count][2]}"

    def toggle_japanese(self):
        # print(self.ids.hiragana_label.color)
        if self.ids.hiragana_label.color == [1, 1, 1, 1]:
            self.ids.show_japanese.text = "Hide Japanese"
            self.ids.hiragana_label.color = [0, 0, 0, 1]
            self.ids.katakana_label.color = [0, 0, 0, 1]
        else:
            self.ids.show_japanese.text = "Show Japanese"
            self.ids.hiragana_label.color = [1, 1, 1, 1]
            self.ids.katakana_label.color = [1, 1, 1, 1]

    def add_points(self):
        global count
        global current_user
        try:
            user_id = current_user.id
            id = vocab_list[count][3]
            VocabApp.db.update_user_stats(user_id, id, 1)
            VocabApp.db.update_user_stats(user_id, id, 1)
            Logger.info("Points removed successfully")
            count += 1
            self.next_vocab()
        except Exception as e:
            Logger.error(f"Error removing points: {e}")

    def remove_points(self):
        global count
        global current_user
        try:
            user_id = current_user.id
            id = vocab_list[count][3]
            VocabApp.db.update_user_stats(user_id, id, -1)
            Logger.info("Points removed successfully")
            count += 1
            self.next_vocab()
        except Exception as e:
            Logger.error(f"Error removing points: {e}")


class VocabApp(MDApp):
    db = database_handler("vocab_app.db")
    def build(self):
        return


boi = VocabApp()
boi.run()
