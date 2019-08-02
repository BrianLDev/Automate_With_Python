# first make sure that pyperclip is installed, import if it is
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        from pip._internal import main as pipmain

        pipmain(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('pyperclip')


#import pyperclip
import random

messageList = ["I'm watching you...",
            "That was a bad idea",
            "Copy Paste, Copy Paste, Copy Paste",
            "This is the FBI.  Do not move.  We will arrive shortly",
            "Paste",
            "What, do you not know how to type?",
            "This is the end",
            "Oh by the way, you've been hacked",
            "Your computer will shut down in 1 minute",
            "Hey!  Remember David Hasslehoff?  Whatever happened to him?",
            "Nope",
            "You should really clear your search history.  ...I mean right away",
            "Noooooooooo!",
            "Hahaha!!  Good one, that was a good one."]

message = messageList[random.randint(0, len(messageList)-1)]

pyperclip.copy(message)

