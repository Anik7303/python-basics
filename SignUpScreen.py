from kivy.uix.screenmanager import Screen
import json
from datetime import datetime


class SignUpScreen(Screen):
    def add_user(self, username, password):
        users = {}
        try:
            with open('users.json') as file:
                users = json.load(file)

        except Exception as e:
            print(e)

        try:
            if not isinstance(users, dict):
                users = {}

            users[username] = {
                'username': username,
                'password': password,
                'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            }

            print(users)
            with open('users.json', 'w') as file:
                file.write(json.dumps(users))

            self.manager.transition.direction = "left"
            self.manager.current = 'signup_success_screen'
        except Exception as e:
            print(e)

    def return_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'
