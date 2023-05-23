"""
In a file called playback.py, implement a program in Python that prompts the 
user for input and then outputs that same input, replacing each space with ... (i.e., three periods).
"""

def main():
    string = input()
    print(string_conv(string))

def string_conv(user_input):
    words = user_input.replace(" ", "...")
    return words

main()