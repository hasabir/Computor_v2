#!/bin/env python3
from calculator_parser import CalculatorParser
import readline
class ComputorV2():
    def __init__(self):
        # super().__init__("")
        self.variables = {}




def shell():
    print("Welcome to ComputorV2!")
    print("Type 'help' for a list of commands.")
    bc = ComputorV2()
    # save history of commands  and relults
    try:
        parser = CalculatorParser()
        while True:
            command = input("> ")
            # readline.add_history(command)
            if command == "help":
                print("Available commands:")
                print("  help - Show this help message")
                print("  exit - Exit the program")
                # Add more commands as needed
            elif command == "exit":
                print("Goodbye!")
                break
            elif command.strip() == "":
                continue
            else:
                try:
                    result = parser.parse(command)
                    readline.add_history(f"{command}\nResult: {result}")
                    print(f"{result}")
                except SyntaxError as e:
                    print(f"Syntax error: {e}")
                except NameError as e:
                    print(f"Name error: {e}")
                # print(f"Unknown command: {command}")
                # Handle other commands as needed
    except KeyboardInterrupt:
        print("\nGoodbye!")

if __name__ == "__main__":
    shell()