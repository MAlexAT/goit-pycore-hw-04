import sys
import os
from pathlib import Path
from colorama import init, Fore, Style

def print_directory_structure(directory, prefix=""):
    # Перебір всіх файлів і директорій в поточній директорії
    for item in sorted(directory.iterdir()):
        # Визначення, чи є елемент директорією або файлом
        if item.is_dir():
            print(f"{prefix}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
            # Рекурсивний виклик функції для виведення структури піддиректорії
            print_directory_structure(item, prefix + "    ")
        else:
            print(f"{prefix}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

def main():
    # Ініціалізація colorama
    init(autoreset=True)
    
    # Перевірка наявності аргументу командного рядка
    if len(sys.argv) != 2:
        print("Usage: python task3.py /Users/newalex/Desktop/Projects/goit-pycore-hw-04")
        return
    
    # Отримання шляху до директорії
    path = Path(sys.argv[1])
    
    # Перевірка, чи існує шлях і чи це директорія
    if not path.exists():
        print(f"Error: The path {path} does not exist.")
        return
    if not path.is_dir():
        print(f"Error: The path {path} is not a directory.")
        return
    
    # Виведення структури директорії
    print(f"{Fore.CYAN}{path.resolve()}{Style.RESET_ALL}")
    print_directory_structure(path)

if __name__ == "__main__":
    main()




