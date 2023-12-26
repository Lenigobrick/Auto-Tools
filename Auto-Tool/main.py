import customtkinter
import tkinter as tk
from pynput.keyboard import Listener, KeyCode
import threading
import time
import random
from tools.Anti_AFK import *
from tools.Auto_Click import *

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

toggle_key = KeyCode(char="t")
toogle_key_y = KeyCode(char="y")
clicking = False
afking = False


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Auto Tool - V1")
        self.geometry(f"{600}x{350}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky="nsew", rowspan=2, columnspan=3)
        self.tabview.add("Auto-Click")
        self.tabview.add("Anti-AFK")
        self.tabview.tab("Auto-Click").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Anti-AFK").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs

        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Auto-Click"), text="Bienvenue sur le menu Auto-Click :")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=4)
        self.label_tab_3 = customtkinter.CTkLabel(self.tabview.tab("Auto-Click"), text="Min :")
        self.label_tab_3.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        entrymin = customtkinter.CTkEntry(self.tabview.tab("Auto-Click"), placeholder_text="1")
        entrymin.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="nsew")
        self.label_tab_4 = customtkinter.CTkLabel(self.tabview.tab("Auto-Click"), text="Max :")
        self.label_tab_4.grid(row=1, column=2, padx=20, pady=(0, 20), sticky="nsew")
        entrymax = customtkinter.CTkEntry(self.tabview.tab("Auto-Click"), placeholder_text="1")
        entrymax.grid(row=1, column=3, padx=20, pady=(0, 20), sticky="nsew")
        self.button_tab_click = customtkinter.CTkButton(self.tabview.tab("Auto-Click"), state="disabled", text_color_disabled="white", fg_color="#D64A4A", text="Disabled [Press 'T' to start]")
        self.button_tab_click.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=4)

        self.label_afk = customtkinter.CTkLabel(self.tabview.tab("Anti-AFK"), text="Bienvenue sur le menu Anti-AFK :")
        self.label_afk.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=4)
        self.button_tab_afk = customtkinter.CTkButton(self.tabview.tab("Anti-AFK"), state="disabled", text_color_disabled="white", fg_color="#D64A4A", text="Disabled [Press 'Y' to start]")
        self.button_tab_afk.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=4)
        self.label_afk_inv1 = customtkinter.CTkLabel(self.tabview.tab("Anti-AFK"), text="---------------------", text_color="#2B2B2B")
        self.label_afk_inv1.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="nsew")
        self.label_afk_inv2 = customtkinter.CTkLabel(self.tabview.tab("Anti-AFK"), text="---------------------", text_color="#2B2B2B")
        self.label_afk_inv2.grid(row=2, column=1, padx=20, pady=(0, 20), sticky="nsew")
        self.label_afk_inv3 = customtkinter.CTkLabel(self.tabview.tab("Anti-AFK"), text="---------------------", text_color="#2B2B2B")
        self.label_afk_inv3.grid(row=2, column=2, padx=20, pady=(0, 20), sticky="nsew")
        self.label_afk_inv4 = customtkinter.CTkLabel(self.tabview.tab("Anti-AFK"), text="---------------------", text_color="#2B2B2B")
        self.label_afk_inv4.grid(row=2, column=3, padx=20, pady=(0, 20), sticky="nsew")

        click_thread = threading.Thread(target=self.clicker)
        afk_thread = threading.Thread(target=self.afker)
        click_thread.start()
        afk_thread.start()

        with Listener(on_press=self.toggle_event) as listener:
            self.mainloop()

    def clicker(self):
        while True:
            if clicking:
                print("running click")
                self.button_tab_click.configure(text="Running [Press 'T' to disable]", fg_color="#4AD64E")
                auto_click_function()
            if not clicking:
                self.button_tab_click.configure(text="Disabled [Press 'T' to start]", fg_color="#D64A4A")  
            time.sleep(1)

    def afker(self):
        while True:
            if afking:
                print("running afk")
                self.button_tab_afk.configure(text="Running [Press 'Y' to disable]", fg_color="#4AD64E")
                anti_afk_function()
            if not clicking:
                self.button_tab_afk.configure(text="Disabled [Press 'Y' to start]", fg_color="#D64A4A")
            time.sleep(1)

    def toggle_event(self, key):
        if key == toggle_key:
            global clicking
            clicking = not clicking
        if key == toogle_key_y:
            global afking
            afking = not afking

if __name__ == "__main__":
    app = App()

