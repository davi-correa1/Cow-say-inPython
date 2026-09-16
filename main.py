# Cleaning the terminal and the time function
import os, time
os.system('cls')


# Cow 

#       ___________
#     /             \
#    |    Phrase     |
#     \ ___________ /
#                 \|
#                    ^__^
#                   |* * |
#                   \___/ |_____________
#                      \                \\
#                       |                \\
#====================================================================

phrase = input("What should the cow say?\n =>  ")
size = len(phrase)

print("\n The cow is arriving... ")
time.sleep(2)

def cow():
    print(" \n \n")
    print(f"       _____{(size - 3) * "_"}_____")
    print(fr"     /    {(size + 3) * " "}  \ ")
    print(f'    |     {phrase}      |')
    print(fr"     \ ___{(size + 2) * "_"}__ /")
    print(fr"                 {(size - 4) * " "}\|")
    print(fr"                    {(size - 4) * " "}^__^")
    print(fr"                   {(size - 4) * " "}|* * |")
    print(fr"                   {(size - 4) * " "}\___/ |_____________")
    print(fr"                       {(size - 4) * " "}|                \\")
    print(fr"                       {(size - 4) * " "}|                 \\")
    print(f"===================================================================={size * "="}")

cow()


