from kivy.uix.screenmanager import Screen


class SignUpSuccessScreen(Screen):
    def return_to_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login_screen"
