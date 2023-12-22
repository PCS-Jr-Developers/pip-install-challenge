# Import the art package
from art import *

def display_art(name):
    # Generate ASCII art for the given name
    ascii_art = text2art(name)
    print(ascii_art)

def main():
    # Ask the user for their name or a word
    name = input("Enter your name or a favorite word: ")
    # Display the ASCII art
    display_art(name)

if __name__ == "__main__":
    main()

    
