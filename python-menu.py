from consolemenu import *
from consolemenu.items import *
import subprocess


def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

def installchocolatey():
    run("Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))')")
    return completed

menu = ConsoleMenu("Configurador de Destops", "Script para configuração padrao de desktops")
menu_item = MenuItem("Menu")

InstalarChocolatey= FunctionItem("Instalar Chocolatey", installchocolatey)


menu.append_item(menu_item)
menu.append_item(InstalarChocolatey)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
