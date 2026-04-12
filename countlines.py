import os


def countlines(ruta) -> int:
    total = 0
    for entry in os.scandir(ruta):
        if entry.is_file():
            with open(entry.path, encoding='utf-8', errors='ignore') as f:
                total += sum(1 for _ in f)
        elif entry.is_dir():
            total += countlines(entry.path)
    return total


if __name__ == '__main__':
    print(countlines('.'))
