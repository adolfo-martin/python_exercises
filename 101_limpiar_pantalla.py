#!/usr/bin/python3

import subprocess

def main() -> None:
    limpiar_pantalla()

def limpiar_pantalla() -> None:
    subprocess.run(['clear'])

if __name__ == "__main__":
    main()