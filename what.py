score = {}
score[('a', 'b')] = 4
score[('x', 'y')] = 3
score[('y', 'z')] = 2
score[('x', 'y')] = 1

if 'x' in score:
    print( max(score[('x', 'y')], score[('a', 'b')]) )
else:
    print( min(score[('x', 'y')], score[('y', 'z')]) )