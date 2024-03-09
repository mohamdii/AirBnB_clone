#!/usr/bin/python3
"""
the cmd module
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    hbnb interpreter class!
    """

    prompt = "(hbnb)"

    def emptyline(self):
        """em  pty
        """

        pass

    def do_quit(self, line):
        """ctrl c
        """

        return True

    def help_quit(self):
        """help
        """

        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """the end of each
        """

        return True

    def help_EOF(self):
        """end of each
        """

        print("EOF command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
