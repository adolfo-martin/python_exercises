#!/usr/bin/python3

import subprocess

def main():
    result = subprocess.run(
        ['whoami'], 
        capture_output=True,
        text=True, 
    )

    if result.returncode == 0:
        print(f'El comando "{result.args[0]}" ha sido ejecutado con éxito.')
        print(f'El usuario actual es "{result.stdout.strip()}"')

if __name__ == "__main__":
    main()