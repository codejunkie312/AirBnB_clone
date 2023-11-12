#!/usr/bin/python3
"""This module contains the code for the console implementation."""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class contains the code for the console implementation."""
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
