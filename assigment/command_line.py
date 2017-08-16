import cmd


class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    def do_greet(self, line):

        x = input("Please enter letter 'L' to save or letter 'E' to exist")
        x.upper()
        if x == 'L':
            print("l is entered")
        else:
            print(" e is entetred")

    def do_save(self, line):
        print("save file")

    def do_quit(self, line):
        print("quitting...")
        return True


if __name__ == '__main__':
    HelloWorld().cmdloop()
