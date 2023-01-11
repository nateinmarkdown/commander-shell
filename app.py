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
'touch <dir>' Creates a file in a specific directory
'rm <dir>' Deletes a file in a specific directory
'mkdir <dir>' Creates a new directory
'rmdir <dir>' Deletes a directory
'mv <original> <new>' Renames or moves a file or directory
'play <game>' Play a fun game in the terminal
'exit' -- Exits the application""")

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
        with open(directory, 'w') as f:
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
@click.argument('game')
def play(game):
    if game == 'dice':
        import random
        dice = str(random.randint(1,6))
        print('You rolled a '+ dice)
    elif game == 'quiz':
        points = 0
        question = input('What does RAM stand for? ').lower
        if question == 'random-access memory' or 'random access memory':
            points += 1
            print('Correct!')
        else:
            print('Incorrect!')  
        question = input('What is the command to remove files in linux? ')  
        if question == 'rm':
            points += 1
            print('Correct!')
        if points <1:
            points = 0
        points = str(points)

        print('You scored ' + points + 'points!')            
    else:
        print("""Unknown game, list of availible games:
'play dice' Rolls a random number between 1 and 6
'play quiz' Play a fun computer quiz""")           

if __name__ == '__main__':
    commanderShell()
