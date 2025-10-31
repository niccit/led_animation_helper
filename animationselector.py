from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.customcolorchase import CustomColorChase
from adafruit_led_animation.animation.multicolor_comet import MulticolorComet
from adafruit_led_animation.animation.pacman import Pacman
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from custom_animations.breathe import BreatheAnimation

# Single class containing a subset of the available LED animations from the CircuitPython LED Animation library
# Allows the use of animations across many projects, for those of us with lazy bones in our body :)

def build_animation(pixels, data, color):
    obj = None

    if "sparkle" in data['name']:
        if "rainbow" in data['name']:
            obj = RainbowSparkle(pixels, data['speed'], data['sparkles'])
        else:
            obj = Sparkle(pixels, data['speed'], color, data['sparkles'])
    if "breathe" in data['name']:
            obj = BreatheAnimation(pixels, data['speed'], color, data['rate'], data['step'], data['count'])
    if "chase" in data['name']:
        if "rainbow" in data['name']:
            obj = RainbowChase(pixels, data['speed'], data['size'], data['spacing'], True)
        elif "multi" in data['name']:
            obj = CustomColorChase(pixels, data['speed'], data['size'], data['spacing'], colors=color, reverse=True)
        elif "custom" in data['name']:
            obj = Chase(pixels, data['speed'], color, data['size'], data['spacing'], True)
    if "blink" in data['name']:
        obj = Blink(pixels, data['speed'], color=color)
    if "cycle" in data['name']:
        obj = ColorCycle(pixels, data['speed'], colors=color)
    if "comet" in data['name']:
        if "rainbow" in data['name']:
            obj = RainbowComet(pixels, data['speed'], data['tail_length'], False, False)
        elif "multi" in data['name']:
            obj = MulticolorComet(pixels, data['speed'], color, tail_length=data['tail_length'], reverse=False, bounce=False)
        elif "custom" in data['name']:
            obj = Comet(pixels, data['speed'], color, data['tail_length'], reverse=False, bounce=False)
    if 'pacman' in data['name']:
        obj = Pacman(pixels, data['speed'], color)
    if 'rainbow' is data['name']:
        obj = Rainbow(pixels, data['speed'], data['period'])
    if 'solid' in data['name']:
        obj = Solid(pixels, color)

    return obj
