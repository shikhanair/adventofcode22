if __name__ == '__main__':

    play_score = {'X':1,'Y':2,'Z':3}
    play_map = {'A':'X', 'B':'Y', 'C':'Z'}
    win_map = {'X':'Y', 'Y':'Z','Z':'X'}#key is beaten by value
    score1 = 0
    score2 = 0
    with open("inputs/day2in") as f:
        for line in f:
            #part 1
            x, play = line.split()
            opp = play_map[x]
            score1+=play_score[play]
            if play == opp:
                score1+=3
            elif play == win_map[opp]:
                score1+=6
            #part 2
            if play == 'X':#lose
                score2+=(play_score[win_map[win_map[opp]]])
            elif play == 'Y':#draw
                score2+=(3 + play_score[opp])
            else:#win
                score2+=(6 + play_score[win_map[opp]])

    print("part 1 score: " + str(score1))
    print("part 2 score: " + str(score2))
