#!/usr/bin/python3

import subprocess
import os

def main() -> None:
    clear_screen()
    list_files()


def clear_screen() -> None:
    subprocess.run(['clear'])


def list_files() -> None:
    files: list[str] = os.listdir()

    print('Los elementos del directorio actual son:')

    for i in range(0, len(files)):
        print(f'\t{i+1}) {files[i]}')


if __name__ == "__main__":
    main()