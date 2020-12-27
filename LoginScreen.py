from kivy.uix.screenmanager import Screen
import json


class LoginScreen(Screen):
    def redirect_to_signup(self):
        self.manager.transition.direction = "left"
        self.manager.current = "signup_screen"

    def login(self, username, password):
        users = {}
        try:
            with open('users.json', 'r') as file:
                users = json.load(file)
                print(users)

                if any(username == user for user in users.keys()):
                    if password == users[username]['password']:
                        self.manager.transition.direction = "left"
                        self.manager.current = "login_success_screen"
                    else:
                        self.ids.message.text = "Wrong password"
                else:
                    self.ids.message.text = "Username not found"
        except Exception as e:
            print(e)

    def redirect_to_forgot_pass(self):
        pass
