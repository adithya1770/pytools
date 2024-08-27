from functions.main import *
import platform, pyfiglet, argparse, os
from rich.console import Console

console = Console()
exitstate = False

print('Welcome', platform.node())
print('Running on', platform.system())

print('\n\n')
print(pyfiglet.figlet_format('PyTools'))
print('\n')
console.print('Type "help" to get information or "exit" to quit.')

def process_command(command):
    parser = argparse.ArgumentParser(description='CLI Tool for Various Utilities')
    
    parser.add_argument('--history', action='store_true', help='Display command history')
    parser.add_argument('--clear-history', action='store_true', help='Clear command history')
    parser.add_argument('--html-parser', nargs=3, metavar=('markdown_path', 'title_content', 'command'), help='Parse markdown to HTML')
    parser.add_argument('--cpu-info', action='store_true', help='Display CPU and memory info')
    parser.add_argument('--network-info', action='store_true', help='Display network info')
    parser.add_argument('--change-color', nargs=2, metavar=('text', 'color'), help='Change text color')
    parser.add_argument('--file-read', metavar='file_path', help='Read a file')
    parser.add_argument('--file-write', metavar='file_name', help='Write to a file')
    parser.add_argument('--safe-write', metavar='file_name', help='Safe write to a file')
    parser.add_argument('--safe-read', metavar='file_name', help='Safe read from a file')
    parser.add_argument('--find', metavar='file_path', help='Find if a file exists')
    parser.add_argument('--game', action='store_true', help='Run the game')
    parser.add_argument('--find-text', nargs=2, metavar=('file_path', 'word'), help='Find text in a file')
    parser.add_argument('--todo', nargs=2, metavar=('data', 'command'), help='Manage todo list')

    args = parser.parse_args(command.split())

    if args.history:
        history()
    elif args.clear_history:
        clear_history()
    elif args.html_parser:
        html_parser(*args.html_parser)
    elif args.cpu_info:
        cpu_info('cpu-info')
    elif args.network_info:
        network_info('network-info')
    elif args.change_color:
        change_color(*args.change_color, 'change-color')
    elif args.file_read:
        file_read(args.file_read, 'file-read')
    elif args.file_write:
        file_write(args.file_write, 'file-write')
    elif args.safe_write:
        safe_write(args.safe_write, 'safe-write')
    elif args.safe_read:
        safe_read(args.safe_read, 'safe-read')
    elif args.find:
        find(args.find, 'find')
    elif args.game:
        game('game')
    elif args.find_text:
        if find_Text(*args.find_text, 'find-text'):
            console.print("Word found in file.", style="green")
        else:
            console.print("Word not found in file.", style="red")
    elif args.todo:
        todo(*args.todo, 'todo')
    elif command.strip().lower() == 'exit':
        global exitstate
        exitstate = True
    elif command.strip().lower() == 'help':
        parser.print_help()
    else:
        console.print('Unknown command. Type "help" for a list of commands.', style="bold red")

if __name__ == '__main__':
    while not exitstate:
        command = input('PyTools>>>> ')
        process_command(command)
    
    console.print('Exiting PyTools...', style="bold green")
