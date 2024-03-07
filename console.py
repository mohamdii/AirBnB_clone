#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt ="(hbnb)"
    def emptyline(self):
        pass
    def do_quit(self, line):
        return True
    def help_quit(self):
        print("Quit command to exit the program\n")
    def do_EOF(self, line):
        return True
    def help_EOF(self):
        print("EOF command to exit the program\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
