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