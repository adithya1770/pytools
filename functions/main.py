import markdown
import platform
import psutil
import pprint
import os
import pickle
import pygame
import random
import time
import sys
from rich.console import Console
from rich.table import Table

history_array = []
console = Console()

def history():
    for arch in history_array:
        console.print(arch, style="bold green")

def clear_history():
    history_array.clear()

def html_parser(markdown_path, title_content, command):
    try:
        with open(markdown_path, 'r') as markdown_file:
            markdown_content_raw = markdown_file.read()
        with open('html.txt', 'r') as html_file:
            html_content = html_file.read()
        with open('generated.txt', 'w') as result_file:
            markdown_content = markdown.markdown(markdown_content_raw)
            updated_html_content = html_content.replace("mainContent", markdown_content)
            updated_html_content2 = updated_html_content.replace("Document", title_content)
            result_file.write(updated_html_content2)
        history_array.append(command)
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

def cpu_info(command):
    try:
        memory_info = psutil.virtual_memory()
        cpu_info = {
            "User": platform.node(),
            "Architecture": platform.architecture()[1],
            "OS": platform.system(),
            "Release": platform.release(),
            "Processor": platform.processor(),
            "Version": platform.version(),
            "CPU Cores": psutil.cpu_count(),
            "Memory": memory_info.total / (1024 ** 3)
        }
        console.print(pprint.pformat(cpu_info), style="green")
        history_array.append(command)
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

def network_info(command):
    try:
        net_info = psutil.net_if_addrs()
        net_io = psutil.net_io_counters()
        for interface, addresses in net_info.items():
            console.print(f"Interface: {interface}", style="green")
            for address in addresses:
                console.print(f"  Address: {address.address}", style="green")
                console.print(f"  Netmask: {address.netmask}", style="green")
                console.print(f"  Broadcast: {address.broadcast}", style="green")
                console.print(f"  Family: {address.family}", style="green")
        console.print(f"Bytes Sent: {net_io.bytes_sent}", style="green")
        console.print(f"Bytes Received: {net_io.bytes_recv}", style="green")
        history_array.append(command)
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

def change_color(text, color, command):
    console.print(text, style=color)
    history_array.append(command)

def file_read(file_path, command):
    try:
        with open(file_path, 'r') as file:
            print(file.read())
        history_array.append(command)
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

def file_write(file_name, command):
    try:
        with open(file_name, 'w') as file:
            file_in = input('Enter what to write: ')
            file.write(file_in)
        history_array.append(command)
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

def safe_write(file_name, command):
    try:
        with open(file_name, 'wb') as file:
            binary_in = input("Enter text to store: ")
            pickle.dump(binary_in, file)
        history_array.append(command)
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

def safe_read(file_name, command):
    try:
        with open(file_name, 'rb') as file:
            binary_out = pickle.load(file)
            print(binary_out)
        history_array.append(command)
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

def find(file_path, command):
    exists = os.path.exists(file_path)
    print(exists)
    history_array.append(command)

def game(command):
    try:
        pygame.init()
        pygame.mixer.music.load('./music.mp3')
        pygame.mixer.music.play()

        print("\n")
        table = Table(title="Start Menu")
        player_table = Table(title="")
        action_table = Table(title="Plan")
        hit_table = Table(title="Powers")
        heal_table = Table(title="")

        table.add_column("CANOPY CHAOS", style="green")
        table.add_row(" | Start", style="bold")
        table.add_row(" | Quit", style="bold")

        action_table.add_column("PLANS", style="green")
        action_table.add_row(" 1 -> Try to Start the Plane")
        action_table.add_row(" 2 -> Move Through the Jungle")

        hit_table.add_column("INVENTORY", style="red")
        hit_table.add_row("1 -> Use your Rifle [-50]")
        hit_table.add_row("2 -> Use Dagger [-25]")

        heal_table.add_column("WILD HERBS", style="green bold")
        heal_table.add_row("1 -> NATIVE CRATOS")
        heal_table.add_row("2 -> WILD LUCAS")

        console.print(table)

        timer_delay = 1
        user_name = ""
        user_choice = ""
        user_choice2 = ""
        user_choice3 = ""
        health_user = 100
        health_monster = 100
        health_variable = [10, 30]
        
        entry_input = input("Enter your choice: ")
        refined_entry_input = entry_input.lower()

        def player_killed():
            console.print("You have died....", style="italic red")

        def engine_exploded():
            console.print("Engine exploded and You Have Died....", style="italic red")

        def see_monster():
            console.print("\nYou See a Huge Jungle Monster", style="red italic")
            printable_img = (
                "───▄█▌─▄─▄─▐█▄\n"
                "───██▌▀▀▄▀▀▐██\n"
                "───██▌─▄▄▄─▐██\n"
                "───▀██▌▐█▌▐██▀\n"
                "▄██████─▀─██████▄"
            )
            console.print(printable_img, style="red")

        def continuation():
            console.print("You Walk through the Jungle....", style="green italic")

        def game_over():
            console.print("GAME OVER", style="bold red")

        def end_of_game():
            console.print("GAME FINISHED...", style="bold")
            console.print("Credits: Adithya P S", style="bold")

        if refined_entry_input == "start":
            console.print("Hi Lone Warrior, What's your Name?", style="italic green")
            user_name = input("Enter your Name: ")
            player_table.add_column("Player One Ready", style="italic red")
            player_table.add_row(user_name)
            console.print(player_table)
            time.sleep(timer_delay)
            console.print(f"Ha! So You've Come my Dear, {user_name}", style="italic green")
            time.sleep(timer_delay)
            console.print("We have been stranded in this godforsaken jungle of weird things", style="italic green")
            time.sleep(timer_delay)
            console.print(" | Escape\n | Die\n", style="bold green")
            user_choice = input("Enter your Choice: ").lower()
            time.sleep(timer_delay)
            if user_choice == "escape":
                console.print("You are indeed a fighter!", style="italic green")
                time.sleep(timer_delay)
                console.print("What's our Plan of Action?", style="italic green")
                time.sleep(timer_delay)
                console.print(action_table)
                time.sleep(timer_delay)
                user_choice2 = input("Enter your Plan: ")
                if user_choice2 == "1":
                    engine_exploded()
                elif user_choice2 == "2":
                    console.print("Walking through the Dense Jungle", style="italic green")
                    time.sleep(timer_delay)
                    console.print("Oh NO!!..", style="italic red")
                    time.sleep(timer_delay)
                    see_monster()
                    console.print("You Check your Inventory....", style="italic green")
                    time.sleep(timer_delay)
                    console.print(hit_table)
                    while health_user > 0 and health_monster > 0:
                        user_choice3 = input("Enter Attack: ")
                        if user_choice3 == "1":
                            health_monster -= 51
                            console.print(f"Monster Health is {health_monster}", style="italic green")
                            user_health = random.choice(health_variable)
                            health_user -= user_health
                            console.print(f"User Health is {health_user}", style="italic green")
                            if health_monster < 0:
                                console.print("HAHAHAH!!", style="bold green")
                                time.sleep(timer_delay)
                                console.print("You have Defeated JONGLE!!..", style="italic green")
                                continuation()
                                break
                            elif health_user < 0:
                                console.print("NO..No...no..argghh", style="bold red")
                                time.sleep(timer_delay)
                                console.print("GOODBYE", style="italic red")
                                game_over()
                                sys.exit()
                        else:
                            health_monster -= 26
                            console.print(f"Monster Health is {health_monster}", style="italic green")
                            user_health = random.choice(health_variable)
                            health_user -= user_health
                            console.print(f"User Health is {health_user}", style="italic green")
                            if health_monster < 0:
                                console.print("HAHAHAH!!", style="bold green")
                                time.sleep(timer_delay)
                                console.print("You have Defeated JONGLE!!..", style="italic green")
                                continuation()
                                break
                            elif health_user < 0:
                                console.print("NO..No...no..argghh", style="bold red")
                                time.sleep(timer_delay)
                                console.print("GOODBYE", style="italic red")
                                game_over()
                                sys.exit()
                else:
                    console.print("Invalid Choice", style="bold red")
                    game_over()
            elif user_choice == "die":
                console.print("You Died...!", style="italic red")
                game_over()
            else:
                console.print("Invalid Choice", style="bold red")
                game_over()
        else:
            console.print("Invalid Command", style="bold red")
            game_over()
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")
    finally:
        pygame.quit()

def find_Text(file_path, word, command):
    file = open(file_path, 'r')
    for i in file.readlines():
        if word == i:
            return True
        else:
            return False

def todo(data, command):
    print("Todo List is only viewable till this instance runs")
    todo_list = []
    if command == 'put':
        todo_list.append(data)
    elif command == 'delete':
        todo_list.remove(data)
    elif command == 'display':
        for tasks in todo_list:
            print(tasks)
    else:
        print("Enter valid commands")

