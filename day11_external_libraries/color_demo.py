from colorama import init, Fore, Back, Style

# Initialize Colorama
init(autoreset=True)

print(Fore.RED + "This is red text.")
print(Fore.GREEN + "This is green text.")
print(Back.YELLOW + "This has a yellow background.")
print(Style.BRIGHT + "This is bright text.")
print(Fore.CYAN + Back.MAGENTA + Style.DIM + "Styled combo text.")

# ✅ init(autoreset=True) ensures color resets automatically after each print.