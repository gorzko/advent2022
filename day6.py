def day6(stream: str, marker_len: int):
    marker = -1
    for i in range(len(stream)):
        if len(set(stream[i:i + marker_len])) == marker_len:
            marker = i + marker_len
            break
    return marker

if __name__ == "__main__":
    with open('input\\day6.txt', 'r') as f:
        file = f.readlines()[0]
    print(day6(file, 14))