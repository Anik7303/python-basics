from kivy.app import App
from kivy.lang import Builder

from RootWidget import RootWidget
from LoginScreen import LoginScreen
from SignUpScreen import SignUpScreen
from LoginSuccessScreen import LoginSuccessScreen
from SignUpSuccessScreen import SignUpSuccessScreen
from ImageButton import ImageButton

Builder.load_file('design.kv')


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
