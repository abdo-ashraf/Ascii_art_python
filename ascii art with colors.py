from termcolor import colored, cprint
from pyfiglet import figlet_format
from msvcrt import getch

# print(dir(pyfiglet))

name = input("Your Text: ").strip()

print("-" * 64)
print("# Supported fonts on page: http://www.figlet.org/examples.html #")
print("-" * 64)
font = input("your font (press enter to use default font): ")

if font.strip().lower() in ["", "standard", "default"]:
  formated_txt = figlet_format(name)
else:
  formated_txt = figlet_format(name, font=font)

print("-" * 71)
print("# Supported colors are: ", end="")
for clr in ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan']:
    cprint(clr, clr, end=" ")

print("white #")
print("-" * 71)
color = input("your color: ").strip()
colored_txt = colored(formated_txt, color=color)

print(colored_txt)

answer = input("Do you want to save the ASCii art as txt or no: ")
if answer.lower() in ["y", "yes", "yeah", "yy"]:
    filename = input("file name is: ") + ".txt"
    # filename = filename + ".txt"
    with open(filename, "w") as file:
        file.write(formated_txt)
else:
    print(colored("Press any key to exit...", color="yellow"))
    junk = getch()
