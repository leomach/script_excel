
import os

def clean_screen():
    """Clear the screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")