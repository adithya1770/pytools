import markdown, platform, psutil, pprint, os, pickle
from rich.console import Console

history_array = list()
console = Console()

def history():
    for arch in history_array:
        console.print(arch, style="bold green")

def clear_history():
    history_array.clear()

def html_parser(markdown_path, title_content, command):
    markdown_file = open(markdown_path, 'r')
    html_file = open('html.txt', 'r')
    result_file = open('generated.txt', 'w')
    markdown_content_raw = markdown_file.read()
    html_content = html_file.read()
    markdown_content = markdown.markdown(markdown_content_raw)
    updated_html_content = html_content.replace("mainContent", markdown_content)
    updated_html_content2 = updated_html_content.replace("Document", title_content)
    result_file.write(updated_html_content2)
    history_array.append(command)


def cpu_info(command):
    memory_info = psutil.virtual_memory()
    cpu_info = {
        "User": platform.node(),
        "Architecture": platform.architecture()[1],
        "OS": platform.system(),
        "Release": platform.release(),
        "Processor": platform.processor(),
        "Version":platform.version(),
        "Wind Edition":platform.win32_edition(),
        "CPU Cores": psutil.cpu_count(),
        "Mac Edition":platform.mac_ver(),
        "Memory":memory_info.total/(1024**3)
    }
    console.print(pprint.pprint(cpu_info), style="green")
    history_array.append(command)

def network_info(command):
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

def change_color(text, color, command):
    console.print(text, style=color)
    history_array.append(command)

def file_read(file_path, command):
    file_read = open(file_path, 'r')
    print(file_read.read())
    history_array.append(command)

def file_write(file_name, command):
    file_write = open(file_name, 'w')
    file_in = input('Enter what to write:')
    file_write.write(file_in)
    history_array.append(command)

def safe_Write(file_name, command):
    file_write = open(file_name, 'wb')
    binary_in = input("Enter text to store:")
    pickle.dump(binary_in, file_write)
    history_array.append(command)

def safe_Read(file_name, command):
    binary_Out = open(file_name, 'rb')
    binary_Out_File = pickle.load(binary_Out)
    history_array.append(command)

def find(file_path ,command):
    exists = os.path.exists(file_path)
    print(exists)
    history_array.append(command)






