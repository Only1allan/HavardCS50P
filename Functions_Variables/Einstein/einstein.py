"""
In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms)
and then outputs the equivalent number of Joules as an integer.
Assume that the user will input an integer.

E = mc**2
c = 300000000

"""
def einstein(mass):
    c = 300000000
    E = mass * c**2
    return E

def main():
    m = int(input("m: "))
    print("E: ",einstein(m))

main()