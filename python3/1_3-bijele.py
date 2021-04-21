piece_count = [1, 1, 2, 2, 2, 8]
pieces = map(int, input().split())
differences = [str(piece_count[index] - x) for index, x in enumerate(pieces)]
print(' '.join(differences))
