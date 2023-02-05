import customtkinter

from settings import *


class App(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title("Mathematical Analysis")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        
        customtkinter.set_appearance_mode(APPEARANCE)
        
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        
        self.sidebar_button_1 = customtkinter.CTkButton(self)
        self.sidebar_button_1.grid(row=0, column=1, sticky=customtkinter.NW)
        