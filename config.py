# python
import os

# Max characters to send to the model per turn
MAX_CHARS = 10000

# Absolute path to the calculator workspace
WORKING_DIR = os.path.join(os.path.dirname(__file__), "calculator")

# Safety cap on agent loop iterations
MAX_ITERS = 20

# python
print("CONFIG LOADED FROM:", __file__)
print("WORKING_DIR =", WORKING_DIR)