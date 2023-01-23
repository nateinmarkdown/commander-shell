from click_shell import shell
import click
import sys
import os
from termcolor import colored

def get_prompt():
    cwd = os.getcwd()
    return colored(cwd + ' >>> ', 'green')

@shell(prompt=get_prompt, intro="Commander Shell version 1.0.0\nType 'help' for help.")
def commanderShell():
    pass

@commanderShell.command()
def help():
    print("""Here is a list of all available commands:
'help' -- Shows this menu,
'message' -- Prints a message to console,
'touch <dir> <name>' Creates a file with a specific name in a directory
'rm <file>' Deletes a file in the current directory
'mkdir <dir>' Creates a new directory
'rmdir <dir>' Deletes a directory
'mv <original> <new>' Renames or moves a file or directory
'ls [dir]' Lists the files in the current directory or a specific directory
'cd <dir>' Change the current working directory
'cat <file>' Prints the contents of a file
'grep <string> <file>' Search for a string in a file
'find <name> [dir]' Search for a file by name in the current directory or a specific directory
'exit' -- Exits the application""")

@commanderShell.command()
@click.argument('message', default='No message provided')
def message(message):
    print(message)

@commanderShell.command()
@click.argument('name')
def touch(name):
    try:
        with open(name, 'w') as f:
            f.write('')
        print("Successfully created file:", name)
    except Exception as e:
        print("Error creating file:", name)
        print(e)

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

@commanderShell.command()
@click.argument('original')
@click.argument('new')
def mv(original, new):
    try:
        os.rename(original, new)
        print(f"Successfully moved/renamed {original} to {new}")
    except Exception as e:
        print('Unable to rename or move file/directory')
        print(e)

@commanderShell.command()
@click.argument('directory', default=os.getcwd())
def ls(directory):
    try:
        os.chdir(directory)
        files = os.listdir()
        for file in files:
            print(file)
    except Exception as e:
        print("Error listing files in directory:", directory)
        print(e)
    os.chdir('..')

@commanderShell.command()
@click.argument('directory')
def cd(directory):
    try:
        os.chdir(directory)
        print("Successfully changed working directory to:", directory)
    except Exception as e:
        print("Error changing working directory to:", directory)
        print(e)

@commanderShell.command()
@click.argument('file')
def cat(file):
    try:
        with open(file, 'r') as f:
            contents = f.read()
            print(contents)
    except Exception as e:
        print("Error reading file:", file)
        print(e)

@commanderShell.command()
@click.argument('string')
@click.argument('file')
def grep(string, file):
    try:
        with open(file, 'r') as f:
            contents = f.read()
            if string in contents:
                print("String '" + string + "' found in file:", file)
            else:
                print("String '" + string + "' not found in file:", file)
    except Exception as e:
        print("Error searching file:", file)
        print(e)

@commanderShell.command()
@click.argument('name')
@click.argument('directory', default=os.getcwd())
def find(name, directory):
    try:
        for root, dirs, files in os.walk(directory):
            if name in files:
                print("File '" + name + "' found in directory:", root)
                return
        print("File '" + name + "' not found in directory:", directory)
    except Exception as e:
        print("Error searching for file:", name)
        print(e)

if __name__ == '__main__':
    commanderShell()
