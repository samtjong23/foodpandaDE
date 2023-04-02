import sys
import re

from cli_app.util import *

MAIN_MENU = re.sub("\t+", "",
                   """
					Select action:
					* Type `1` to create a table containing the 5 nearest ports to Singapore's Jurong Island port
					* Type `2` to create a table containing the country that has the largest number of ports with a cargo wharf
					* Type `3` to create a table containing the nearest port with provisions, water, fuel oil and diesel
					* Type `4` to view Samuel's understanding of refactoring and testing
					* Type `5` to view Samuel's thoughts on https://github.com/tiangolo/fastapi
					* Type `quit` to exit
					"""
                   )

ACTIONS = {
    "4": "To be updated",
    "5": "To be updated"
}


class CLIApp():
    def __init__(self):
        self.big_query_client = get_big_query_client()

    def print_main_menu(self):
        print(MAIN_MENU)

    def run(self):
        print("\nWelcome to the CLI App.")
        self.print_main_menu()

        for line in sys.stdin:
            action = line.strip()

            if action == "quit":
                print("\nThank you for using the app. Bye. :D\n")
                sys.exit()

            else:
                if action in ["1", "2", "3"]:
                    print(f"\n{self.big_query_client.create_table(action)}")
                    self.print_main_menu()

                elif action in ["4", "5"]:
                    print(f"{ACTIONS[action]}")
                    self.print_main_menu()

                else:
                    print("\nInvalid input. Please try again.")
                    self.print_main_menu()

        return
