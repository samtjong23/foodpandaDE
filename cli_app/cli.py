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
    "4": re.sub("\t+", "",
                """
								Refactoring is the process of restructuring existing code without changing its external behavior. The goal of refactoring can include:
								- Improving readability and maintainability
								- Reducing complexity
								- Improving performance
								- Ensuring compatibility with new technologies or platforms
							
								Testing is the process of checking if a software application works as it should. The goal of writing test cases can include:
								- Making sure software behaves as expected
								- Finding and fixing issues early on
								- Ensuring that new changes don't break existing functionality
							
								There are different types of tests, including unit tests and integration tests.
								- Unit tests check individual parts of the code in isolation, to ensure they work as intended.
								- Integration tests check how different parts of the code work together, to ensure the whole system functions as it should.
								"""
                ),
    "5": re.sub("\t+", "",
                """
								The FastAPI repository has a clear structure, which makes it very easy for both users and contributors to find what they are looking for.
								
								Here is a brief overview of the structure:
								- docs/ & docs_src: These directories contains the documentation for the project
								- fastapi/: This directory contains the source code for the FastAPI framework
								- script/ : This directory contains various scripts that can be useful for contributors when working on the repository
								- tests/: This directory contains the tests for the FastAPI framework

								Furthermore, the repository also features clear commit messages and a detailed README file that explains what the repository does and how to use it.
								
								However, there are still areas for improvements:
								- The codebase could benefit from more inline comments to explain what each block of code does. This would help other developers understand the codebase and make it easier to maintain in the future.
								- Some commits can be repetitive. For example, back-to-back commits that say "Update release notes" could be merged into a single commit to keep the commit history clean and concise.
								"""
                )
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
