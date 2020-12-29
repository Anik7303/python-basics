from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from hoverable import HoverBehavior


class ImageButton(ButtonBehavior, Image, HoverBehavior):
    pass
