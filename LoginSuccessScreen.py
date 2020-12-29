from kivy.uix.screenmanager import Screen
import glob
import json
import random
from pathlib import Path


class LoginSuccessScreen(Screen):
    def logout(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

    def search(self, phrase):
        phrase = phrase.strip()
        available_feelings = [
            Path(feeling).stem for feeling in glob.glob('quotes/*.txt')]
        if phrase in available_feelings:
            with open(f'quotes/{phrase}.txt', 'r', encoding='utf-8') as file:
                quotes = file.readlines()

            quote = random.choice(quotes)
            self.ids.message.text = quote
        else:
            self.ids.message.text = "This feeling is not supported yet. Please try another feeling"
