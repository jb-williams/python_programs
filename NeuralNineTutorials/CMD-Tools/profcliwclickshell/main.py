from click_shell import shell

@shell(prompt="xf-shell > ", intro="""Welcome to the xf shell!
Please enter a command down below. If you want to see a list of all available commands, enter "help".""")
def xf_shell():
    pass

@xf_shell.command()
def help():
    print("""Here is a list of all commands:
    help: See this list
    hello-world: Prints a message
    add: Add two numbers
    create-file: create new file and write into it
    exit: Exit the shel""")

@xf_shell()
def hello_world():
    print("Hello World")

@xf_shell()
def add():
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    print(n1 + n2)

@xf_shell()
def create_file():
    file_name = input("Enter the file name: ")
    content = input("Enter the file content: ")
    with open(file_name, "w") as f:
        f.write(content)

if __name__ == "__main__":
    xf_shell()