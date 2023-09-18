#Input
pieces_you_have = input()

#Splits the input on blank spaces in ot a array
pieces_you_have = pieces_you_have.split()

#Checks how many pices you need to add or subtract
kings = 1 - int(pieces_you_have[0])
queens = 1 - int(pieces_you_have[1])
rooks = 2 - int(pieces_you_have[2])
bishops = 2 - int(pieces_you_have[3])
knights = 2 - int(pieces_you_have[4])
pawns =  8 - int(pieces_you_have[5])

#Prints the result
print(kings, queens, rooks, bishops, knights, pawns)