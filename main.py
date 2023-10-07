import sys
import tkinter
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import generator
import customtkinter as CTk
from PIL import Image
import random
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        # app settings
        self.geometry("620x700")
        self.title("Random Letters & digits generator with GUI")
        self.resizable(False, False)

        self.logo = CTk.CTkImage(dark_image=Image.open(resource_path("img.png")), size=(620, 415))
        self.logo_label = CTk.CTkLabel(master=self, text="", image=self.logo)
        self.logo_label.grid(row=0, column=0)

        # FRAME 1
        self.generator_setting = CTk.CTkFrame(master=self, bg_color="white")
        self.generator_setting.grid(row=1, column=0, padx=(20, 20), pady=(10, 0), sticky="n")

        # label 1 line_length_min
        self.line_length_min = CTk.CTkLabel(master=self.generator_setting, text="Line Length Min:")
        self.line_length_min.grid(row=0, column=0, padx=10)
        # entry field 1 line_length_min
        self.line_length_min_var = CTk.CTkEntry(master=self.generator_setting, width=100)
        self.line_length_min_var.grid(row=0, column=1, padx=(0, 10), pady=10)

        # label 2 line_length_max
        self.line_length_max = CTk.CTkLabel(master=self.generator_setting, text="Line Length Max:")
        self.line_length_max.grid(row=1, column=0, padx=(10, 10), pady=0)
        # entry field 2 line_length_max
        self.line_length_max_var = CTk.CTkEntry(master=self.generator_setting, width=100)
        self.line_length_max_var.grid(row=1, column=1, padx=(0, 10), pady=(10, 10))

        # label 1.1 lines_min
        self.lines_min = CTk.CTkLabel(master=self.generator_setting, text="Lines Min:")
        self.lines_min.grid(row=0, column=2, padx=(0, 10))
        # entry field 1.1 line_min
        self.lines_min_var = CTk.CTkEntry(master=self.generator_setting, width=100)
        self.lines_min_var.grid(row=0, column=3, padx=(0, 10))

        # label 2.1 lines_max
        self.lines_max = CTk.CTkLabel(master=self.generator_setting, text="Lines Max:")
        self.lines_max.grid(row=1, column=2, padx=(0, 10))
        # entry field lines_max
        self.lines_max_var = CTk.CTkEntry(master=self.generator_setting, width=100)
        self.lines_max_var.grid(row=1, column=3, padx=(0, 10), pady=(10, 10))

        # FRAME 2
        self.settings_frame = CTk.CTkFrame(master=self, bg_color="white")
        self.settings_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="n")

        # checkbox digits
        self.cb_digits_var = tkinter.StringVar()
        self.cb_digits = CTk.CTkCheckBox(master=self.settings_frame, text="0-9", variable=self.cb_digits_var,
                                         onvalue=digits, offvalue="")
        self.cb_digits.grid(row=2, column=0, padx=10, pady=10)
        self.cb_digits.select(1)

        # checkbox lower letter
        self.cb_lower_var = tkinter.StringVar()
        self.cb_lower = CTk.CTkCheckBox(master=self.settings_frame, text="a-z", variable=self.cb_lower_var,
                                        onvalue=ascii_lowercase, offvalue="")
        self.cb_lower.grid(row=2, column=1, pady=10)

        # checkbox upper letter
        self.cb_upper_var = tkinter.StringVar()
        self.cb_upper = CTk.CTkCheckBox(master=self.settings_frame, text="A-Z", variable=self.cb_upper_var,
                                        onvalue=ascii_uppercase, offvalue="")
        self.cb_upper.grid(row=2, column=2, pady=10)

        # checkbox symbol
        self.cb_symbol_var = tkinter.StringVar()
        self.cb_symbol = CTk.CTkCheckBox(master=self.settings_frame, text="@#$%", variable=self.cb_symbol_var,
                                         onvalue=punctuation, offvalue="")
        self.cb_symbol.grid(row=2, column=3, pady=10)

        # FRAME 3
        self.text_area = CTk.CTkFrame(master=self, fg_color="transparent")
        self.text_area.grid(row=3, column=0, padx=(20, 20), pady=(20, 0), sticky="n")
        # Text Box
        self.textbox = CTk.CTkTextbox(master=self.text_area, bg_color="red", width=200, height=50)
        self.textbox.grid(row=1, column=0, columnspan=2)
        # Generate BTN
        self.generate_btn = CTk.CTkButton(master=self.text_area, text="Generate file", width=100,
                                          command=self.generating)
        self.generate_btn.grid(row=2, column=0, padx=20, pady=10)
        # Dark/Light theme
        self.appearance_mode_option_menu = CTk.CTkOptionMenu(master=self.text_area,
                                                             values=["Light", "Dark", "System"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=2, column=1, padx=(0, 20), pady=10)

        # settings
        self.line_length_min_var.insert(0, "1")
        self.line_length_max_var.insert(0, "2")
        self.lines_min_var.insert(0, "1")
        self.lines_max_var.insert(0, "2")
        self.appearance_mode_option_menu.set("System")

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode):
        CTk.set_appearance_mode(new_appearance_mode)

    def get_characters(self):
        chars = "".join(self.cb_digits.get() + self.cb_upper.get() + self.cb_lower.get() + self.cb_symbol.get())
        return chars

    def generating(self):
        self.textbox.delete("0.0", "end")
        lines_counter = 0

        if int(self.lines_min_var.get()) >= int(self.lines_max_var.get()) or int(self.line_length_min_var.get()) >= int(
                self.line_length_max_var.get()):
            self.textbox.insert("0.0", "ERROR" + "\n" + "Min more or equal that Max!")
        else:
            d = open("Generated.txt", "w")
            for _ in range(random.randrange(int(self.lines_min_var.get()), int(self.lines_max_var.get()))):
                with open("Generated.txt", "a") as f:
                    f.write(''.join(generator.create_new(
                        length=random.randrange(int(self.line_length_min_var.get()),
                                                int(self.line_length_max_var.get())),
                        characters=self.get_characters()) + "\n"))
                lines_counter += 1
            self.textbox.insert("0.0", 'Lines: ' + str(lines_counter))


if __name__ == "__main__":
    app = App()
    app.mainloop()
