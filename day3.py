from itertools import islice
if __name__ == '__main__':

    # part 1
    sum1 = 0
    with open("inputs/day3in") as f:
        for line in f:
            c1 = line[:len(line)//2]
            c2 = line[len(line)//2:]
            for c in c1:
                if c in c2:
                    val = ord(c)
                    sum1 += (val - 96) if val > 96 else (val - 38)
                    break


    #part 2
    sum2 = 0
    with open("inputs/day3in") as f:
        while True:
            elves = list(islice(f, 3))
            if not elves:
                break
            for c in elves[0]:
                if c in elves[1] and c in elves[2]:
                    val = ord(c)
                    sum2 += (val - 96) if val > 96 else (val - 38)
                    break


    print("part 1: " + str(sum1))
    print("part 2: " + str(sum2))

