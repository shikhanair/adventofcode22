if __name__ == '__main__':
    pairs1 = 0
    pairs2 = 0
    with open("inputs/day4in") as f:
        # part 1
        for line in f:
            e1, e2 = line.split(',')
            e1 = e1.split('-')
            e2 = e2.split('-')
            e1 = [int(i) for i in e1]
            e2 = [int(i) for i in e2]
            if (e1[0] >= e2[0] and e1[1] <= e2[1]) or (e2[0] >= e1[0] and e2[1] <= e1[1]):
                pairs1+=1
            if (e1[0] >= e2[0] and e1[0] <= e2[1]) or (e2[0] >= e1[0] and e2[0] <= e1[1]) or (e1[1] >= e2[0] and e1[1] <= e2[1]) or (e2[1] >= e1[0] and e2[1] <= e1[1]):
                pairs2+=1

    print(pairs1)
    print(pairs2)