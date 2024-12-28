import os
import objc

def open_file(filename):
    print(f"Opening file: {filename}")
    try:
        os.startfile(filename)
    except FileNotFoundError:
        print(f"File not found: {filename}")
