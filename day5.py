import re
from itertools import islice
if __name__ == '__main__':
    stacks1 = [[], [], [], [], [], [], [], [], []]
    stacks2 = [[], [], [], [], [], [], [], [], []]
    with open("inputs/day5in") as f:
        drawing = list(islice(f, 8))
        for level in drawing:
            boxes = [level[i:i + 4] for i in range(0, len(level), 4)]
            boxes = [re.sub(r'\W+', '', i) for i in boxes]
            for i in range(len(boxes)):
                if boxes[i] != '':
                    stacks1[i].insert(0, boxes[i])
                    stacks2[i].insert(0, boxes[i])

    with open("inputs/day5in") as f:
        for line in f:
            if "move" in line:
                moves = re.findall(r'\d+', line)
                numbox = int(moves[0])
                og = int(moves[1]) - 1
                dest = int(moves[2]) - 1
                stacks2[dest] = stacks2[dest]+(stacks2[og][-1*numbox:])
                for i in range(numbox):
                    stacks2[og].pop()
                    stacks1[dest].append(stacks1[og].pop())

    tops = ''
    tops2 = ''
    for stack in stacks1:
        tops+=stack.pop()
    for stack in stacks2:
        tops2 += stack.pop()
    print(tops)
    print(tops2)