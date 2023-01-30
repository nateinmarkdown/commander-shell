from click_shell import shell
from termcolor import colored
import click
import sys
import os

@shell(prompt=colored('{} >>> '.format(os.getcwd()), 'green'), intro="""Commander Shell version 1.0.0
Type 'help' for help.""")

def commanderShell():
    pass

@commanderShell.command()
def help():
    print("""Commands:
'help' -- Show this menu
'message' -- Print a message
'touch' -- Create a file
'rm' -- Delete a file
'mkdir' -- Create a directory
'rmdir' -- Delete a directory
'mv' -- Rename or move a file or directory
'ls' -- List files in a directory
'cd' -- Change working directory
'cat' -- Print contents of a file
'grep' -- Search for string in a file
'find' -- Search for a file by name
'exit' -- Exit the application
For more info on each command, type '<command> --help'""")

@commanderShell.command()
@click.argument('message', default='No message provided')
def message(message):
    print(message)

@commanderShell.command()
@click.argument('name')
@click.argument('directory', default=os.getcwd(), required=False)
def touch(name, directory=None):
    if directory is None:
        directory = os.getcwd()
    try:
        os.chdir(directory)
        with open(name, 'w') as f:
            f.write('')
        print(f"Successfully created file {name} in directory {directory}")
    except Exception as e:
        print("Error creating file:", name)
        print(e)
    os.chdir('..')

@commanderShell.command()
@click.argument('file')
def rm(file):
    try:
        os.remove(file)
        print("Successfully deleted file:", file)
    except Exception as e:
        print("Error deleting file:", file)
        print(e)

@commanderShell.command()
@click.argument('directory', default=os.getcwd(), required=False)
def mkdir(directory=None):
    if directory is None:
        directory = os.getcwd()
    try:
        os.mkdir(directory)
        print("Successfully created directory:", directory)
    except Exception as e:
        print("Error creating directory:", directory)
        print(e)

@commanderShell.command()
@click.argument('directory', default=os.getcwd(), required=False)
def rmdir(directory=None):
    if directory is None:
        directory = os.getcwd()
    try:
        os.rmdir(directory)
        print("Successfully deleted directory:", directory)
    except Exception as e:
        print("Error deleting directory:", directory)
        print(e)

@commanderShell.command()
@click.argument('original')
@click.argument('new')
def mv(original, new):
    try:
        os.rename(original, new)
    except Exception as e:
        print('Unable to rename or move file/directory')
        print(e)

@commanderShell.command()
@click.argument('directory', default=os.getcwd(), required=False)
def ls(directory=None):
    if directory is None:
        directory = os.getcwd()
    try:
        os.chdir(directory)
        print("Files in directory:", directory)
        print(os.listdir())
    except Exception as e:
        print("Error listing files in directory:", directory)
        print(e)
    os.chdir('..')

@commanderShell.command()
@click.argument('directory', default=os.getcwd(), required=False)
def cd(directory=None):
    if directory is None:
        directory = os.getcwd()
    try:
        os.chdir(directory)
        print("Successfully changed working directory to:", directory)
    except Exception as e:
        print("Error changing working directory to:",directory)
        print(e)
        
@commanderShell.command()
@click.argument('file')
def cat(file):
    try:
        with open(file, 'r') as f:
            print(f.read())
    except Exception as e:
        print("Error reading file:", file)
        print(e)

@commanderShell.command()
@click.argument('string')
@click.argument('file')
def grep(string, file):
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if string in line:
                    print(line)
    except Exception as e:
        print("Error searching file:", file)
        print(e)

@commanderShell.command()
@click.argument('name')
@click.argument('directory', default=os.getcwd(), required=False)
def find(name, directory=None):
    if directory is None:
        directory = os.getcwd()
    try:
        os.chdir(directory)
        for root, dirs, files in os.walk("."):
            if name in files:
                print(os.path.join(root, name))
    except Exception as e:
        print("Error finding file:", name)
        print(e)
    os.chdir('..')

if __name__ == '__main__':
    commanderShell()
