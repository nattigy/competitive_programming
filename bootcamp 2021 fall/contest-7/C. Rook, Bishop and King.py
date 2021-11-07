def rookBishopKing(start, end):
    rook = moveRook(start, end)
    bishop = moveBishop(start, end)
    king = moveKing(start, end)
    print(rook, bishop, king)


def moveRook(start, end):
    # if either the row or the column are equal it only needs one move else return 2
    if start[0] == end[0] or start[1] == end[1]:
        return 1
    return 2


def moveBishop(start, end):
    # if they are on different color then it can't make any move
    if (start[0] + start[1]) % 2 != (end[0] + end[1]) % 2:
        return 0
    # if they are on the same diagonal it needs to make only one move
    if abs(start[0] - end[0]) == abs(start[1] - end[1]):
        return 1
    return 2


def moveKing(start, end):
    count = 0
    # if either they have the same column or the same row it only needs the difference between them 
    # to make a move
    # else it should move across the diagonal to make the distance shorter 
    column_distance = abs(start[1] - end[1])
    row_distance = abs(start[0] - end[0])
    if start[0] == end[0]:
        return column_distance
    if start[1] == end[1]:
        return row_distance
    diag = min(row_distance, column_distance)
    count += diag
    if row_distance < column_distance:
        count += abs(column_distance - diag)
    elif row_distance > column_distance:
        count += abs(row_distance - diag)
    return count


grid = input().rstrip().split(" ")
rookBishopKing([int(grid[0]), int(grid[1])], [int(grid[2]), int(grid[3])])
