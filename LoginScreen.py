from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):
    def redirect_to_signup(self):
        self.manager.current = "signup_screen"

    def login(self):
        pass

    def redirect_to_forgot_pass(self):
        pass
