data: list[str] = []

while True:
    ctt: str = input('')
    data.append(
        ctt
        .replace('/data/data/com.termux/files', '')
        .replace('Android', 'BSD')
        .replace('android', 'bsd')
        .strip()
    )

    if '.?' in ctt:
        for line in data:
            print(line)
        break
