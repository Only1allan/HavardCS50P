"""
In a file called camel.py, implement a program that prompts the user for the name of a 
variable in camel case and outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case.

"""

def main():
    name = input("camelCase: ")
    snake = snakecase(name)
    print("snake_case: ", snake)

def snakecase(str):
    string = []
    for i in str:
        if i == i.upper() and len(string) > 0:
            string.append("_")
        string.append(i.lower())
    return ''.join(string)

main()