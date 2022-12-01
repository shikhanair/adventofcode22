
if __name__ == '__main__':

    cal = 0
    elves = []
    with open("inputs/day1in") as f:
        for line in f:
            if line in ['\n', '\r\n']:
                elves.append(cal)
                cal = 0
            else:
                cal+=int(line)
    elves = sorted(elves)
    print(elves[-1])
    print(sum(elves[-3:]))