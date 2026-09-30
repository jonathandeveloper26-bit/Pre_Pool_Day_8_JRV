### Task 1.1: Use Pyjokes to print a random chuck norris joke
import pyjokes
import random

print(random.choice(pyjokes.get_jokes("en", category="chuck")))