# Redlines – Visual Diff Between Texts (Markdown)
# Use: Compare two versions of a text with red/green markups.

from redlines import Redlines
from IPython.display import display, Markdown

original = "The AI model is fast and accurate."
modified = "The AI system is efficient and accurate."

# IceCream – For Debugging Output Elegantly
# Use: Print variable names and values for quick debugging.

from icecream import ic

x = 10
y = "AI"
ic(x * 2, y.upper())  # Output: ic| x * 2: 20, y.upper(): 'AI'



# Faker – Generate Fake Data for Testing
# Use: Create dummy data like names, addresses, emails, etc.


from faker import Faker

fake = Faker()
print(fake.name())
print(fake.email())
print(fake.address())


# Textual – Build TUI (Text User Interfaces)
# Use: Create interactive terminal apps using modern UI elements.

from textual.app import App
from textual.widgets import Button

class MyApp(App):
    def compose(self):
        yield Button("Click Me!")

MyApp().run()


# Loguru – Better Logging in Python
# Use: Logging with less boilerplate and more control.

from loguru import logger

logger.info("Training started...")
logger.warning("Memory usage is high.")

# PrettyErrors – Beautify Tracebacks
# Use: Make error tracebacks readable and color-coded.

import pretty_errors
1 / 0  # Will show a pretty, formatted traceback



# tqdm – Progress Bars for Loops
# Use: Show real-time progress bars in loops.

from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.01)


# humanize – Make Data More Readable for Humans
# Use: Convert dates, numbers, file sizes to human-readable formats.

import humanize
import datetime

print(humanize.naturaltime(datetime.datetime.now() - datetime.timedelta(days=1)))
# Output: "a day ago"


# pyperclip – Clipboard Interface
# Use: Copy and paste text programmatically.

import pyperclip

pyperclip.copy("Copied to clipboard!")
print(pyperclip.paste())  # Output: Copied to clipboard!


















