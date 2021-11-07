def kingEscape(queen, king, win, grid):
    if (
        (
            king[0] < queen[0]
            and win[0] < queen[0]
            and king[1] < queen[1]
            and win[1] < queen[1]
        )
        or (
            king[0] > queen[0]
            and win[0] > queen[0]
            and king[1] > queen[1]
            and win[1] > queen[1]
        )
        or (
            king[0] < queen[0]
            and win[0] < queen[0]
            and king[1] > queen[1]
            and win[1] > queen[1]
        )
        or (
            king[0] > queen[0]
            and win[0] > queen[0]
            and king[1] < queen[1]
            and win[1] < queen[1]
        )
    ):
        return "YES"
    return "NO"


grid = int(input())
queen = input().rstrip().split(" ")
king = input().rstrip().split(" ")
win = input().rstrip().split(" ")
queen = [int(queen[0]), int(queen[1])]
king = [int(king[0]), int(king[1])]
win = [int(win[0]), int(win[1])]
print(kingEscape(queen, king, win, int(grid)))
