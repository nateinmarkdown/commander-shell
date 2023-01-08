from click_shell import shell
import click
import sys
import os

@shell(prompt='>>> ', intro="""Commander Shell version 1.0.0
Type 'help' for help.""")

def commanderShell():
    pass

@commanderShell.command()
def help():
    print("""Here is a list of all availible commands:
    'help' -- Shows this menu,
    'message' -- Prints a messsage to console,
    'exit' -- Exits the application
    'touch <dir>' Creates a file in a specific directory
    'rm <dir>' Deletes a file in a specific directory
    'mkdir <dir>' Creates a new directory
    'rmdir <dir>' Deletes a directory""")

@commanderShell.command()
@click.argument('message', default='No message provided')
def message(message):
    print(message)

import sys
import os

@commanderShell.command()
@click.argument('directory')
def touch(directory):
    try:
        with open(file_directory, 'w') as f:
            f.write('')
        print("Successfully created file in directory:", directory)
    except Exception as e:
        print("Error creating file in directory:", directory)
        print(e)

@commanderShell.command()
@click.argument('directory')
def rm(directory):
    try:
        os.remove(directory)
        print("Successfully deleted file:", directory)
    except Exception as e:
        print("Error deleting file:", directory)
        print(e)

@commanderShell.command()
@click.argument('directory')
def mkdir(directory):
    try:
        os.mkdir(directory)
        print("Successfully created directory:", directory)
    except Exception as e:
        print("Error creating directory:", directory)
        print(e)

@commanderShell.command()
@click.argument('directory')
def rmdir(directory):
    try:
        os.rmdir(directory)
        print("Successfully deleted directory:", directory)
    except Exception as e:
        print("Error deleting directory:", directory)
        print(e)

if __name__ == '__main__':
    commanderShell()