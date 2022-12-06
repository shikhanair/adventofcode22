def find_marker(len_data, len_window):
    for i in range(len_data):
        if len(set(data[i:i+len_window])) == len_window:
            return i + len_window

if __name__ == '__main__':
    with open("inputs/day6in") as f:
        data = f.read()

    print(find_marker(len(data), 4))
    print(find_marker(len(data), 14))
