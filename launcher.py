# mariam alaa 221000919
# Farida Hazem 221000214
# mohamed emad 221000268
# Omar Bassam tawfik 221000307
# Nada Gamal 221000829

import os
from simple_term_menu import TerminalMenu

def main():
    options = ["X/O","pong",'hangman','rock paper scissors','snake',"exit"]
    games = ['python3 xo.py','python3 pong.py','python3 hangman.py','python3 rockpaperscissors.py','python3 Snake.py',f'kill {os.getpid()}']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    os.system(f"{games[menu_entry_index]}") 

if __name__ == "__main__":
    print("please select game:")
    main()
