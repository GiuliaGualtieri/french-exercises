import tkinter
import tkinter.messagebox
import customtkinter
import pandas as pd
import random
from time import sleep

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

df_QA = pd.read_csv("data/out/df_QA.csv", header=0)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.rnd = 0
        self.first = True
        self.counter = 0
        self.right = 0
        # configure window
        self.title("FRENCH EXERCISES")
        self.geometry(f"{800}x{600}")
        self.my_font = customtkinter.CTkFont(family="Calibri", size=20)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # title and text question frame
        # title 
        self.frame_title_text = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_title_text.grid(row=0, column=0, rowspan=2, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
        self.frame_title_text.grid_rowconfigure(1, weight=1)
        self.frame_title_text.grid_columnconfigure(1, weight=1)
        self.title_label = customtkinter.CTkLabel(
            self.frame_title_text, text="Let's practice in French!", 
            font=customtkinter.CTkFont(family = "Calibri", size=30, weight="bold",slant ='roman'))
        self.title_label.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(20, 20))
        # text question
        self.textbox = customtkinter.CTkTextbox(master=self.frame_title_text, font = self.my_font)
        self.textbox.grid(row=1, column=1, columnspan=2, padx=(20, 20), pady=(10, 20),  sticky="nsew")
        # self.textbox.insert("insert", self.combobox.get() + "\n")
        self.textbox.insert("insert", self.insert_new_question())
        # self.textbox.configure(state="disabled")

        # chose your answer
        self.combobox = customtkinter.CTkComboBox(master=self, values=self.possible_answers(), font=self.my_font)
        self.combobox.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        self.combobox.set(self.possible_answers()[0])
        # insert to the check
        self.button = customtkinter.CTkButton(master=self, command=self.insert_answer_callback, text="Insert Answer", font=self.my_font)
        self.button.grid(row=2, column=1, padx=20, pady=20, sticky="ew")
        # go to next question
        self.button = customtkinter.CTkButton(master=self, command=self.next_question_callback, text="Next Question", font=self.my_font)
        self.button.grid(row=3, column=0, columnspan =2, padx=20, pady=20, sticky="ew")

        # change appearance
        self.appearance_mode_label = customtkinter.CTkLabel(master=self, text="Appearance Mode:", anchor="w", font=self.my_font)
        self.appearance_mode_label.grid(row=4, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master=self, values=["Light", "Dark", "System"], font=self.my_font,
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=5, column=0, padx=20, pady=(20, 20))
        self.scaling_label = customtkinter.CTkLabel(master=self, text="UI Scaling:", anchor="w", font=self.my_font)
        self.scaling_label.grid(row=4, column=1, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(master=self, values=["80%", "90%", "100%", "110%", "120%"], font=self.my_font,
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=5, column=1, padx=20, pady=(10, 20))

    # supporting functions
    def random_sample(self):
        # set seed
        self.rnd = random.randint(0, df_QA.shape[0] - 1)

    def insert_new_question(self):
        # insert a new question
        return df_QA['question'].iloc[self.rnd] + ".\n"
    
    def possible_answers(self):
        answer_txt = df_QA['answers'].iloc[self.rnd][1:-1]
        answer_list = answer_txt.split("'")
        answer_set = set(answer_list)
        answer_set.remove(", ")
        answer_set.remove("")
        answer_list = list(answer_set)
        if len(answer_list) < 2:
            pass
        # answer_set.shuffle()
        return answer_list

    def insert_answer_callback(self):
        # inserisco e check the answer of the user
        self.textbox.insert("insert", "\n" + "<mask> : " + self.combobox.get())
        answer = df_QA['answer'].iloc[self.rnd]
        right = False
        # check if it is the right answer
        if self.combobox.get() == answer:
            right = True
            if self.first:
                self.right += 1
        # print weel done! or bad answer! and try again
        if right:
            self.textbox.insert("insert", " is correct. Well Done! :) \n")
        else:
            self.textbox.insert("insert", " is the wrong answer :( Try again! \n")
        self.first = False   

    def next_question_callback(self):
        # update random index to be sampled
        self.random_sample()
        # clear textbox
        self.textbox.delete("0.0", "end")
        if self.counter<20:
            # go to the next question
            self.textbox.insert("insert", self.insert_new_question())
            # update counters
            self.counter += 1
            # update first check
            self.first = True
            # update possible answers
            self.combobox.configure(values=self.possible_answers(), font=self.my_font)
            # set default value
            self.combobox.set(self.possible_answers()[0])
        else:
            # print your final score
            self.textbox.insert("insert", f"YOUR FINAL SCORE IS {str(self.right)} over {self.counter}")
            self.textbox.configure(state="disabled")
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = App()
    app.mainloop()