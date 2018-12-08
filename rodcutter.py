'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' You are given a rod of length n feet and a list of pairs that contain the
' prices of pieces of various sizes. For instance, [[1, 1], [2, 3]] means
' that a 1-foot rod costs $1 and a 2-foot rod costs $3. Complete the
' rod_cutter function found below. The function should compute the maximum
' value that can be obtained by cutting up the rod and selling the pieces.
' For example, if the length of the rod is 4 feet long and the values are
' [[1, 1], [2, 3]], the maximum value is 6, obtained by cutting the rod into
' two pieces of length 2, each worth $3.
' Hints:
' a. Implement a use-it or lose-it algorithm
' b. Consider multiple bases cases
' c. values[0][0] refers to the length of the rod,
'    values[0][1] refers to the cost of the rod
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def rod_cutter(values, n):
    if values <= 0 or n == 0:
        return 0
    elif n[0] > values:
        rod_cutter(values, n[1:])
    else:
        


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Code to test your work. DO NOT TOUCH.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def test(test_num, function, input1, input2, expected_output):
    received = function(input1, input2)
    try:
        assert(received == expected_output)
        print('Test %d passed.' % test_num)
    except:
        if isinstance(input1, str):
            print('Test %d failed: %s(\'%s\', \'%s\') should be %s.' %
                  (test_num, function.__name__, input1, input2, expected_output))
            print('   -- Received %s.' % received)
        else:
            print('Test %d failed: %s(%s, %s) should be %s.' %
                  (test_num, function.__name__, input1, input2, expected_output))
            print('   -- Received %s.' % received)

test(1, rod_cutter, [], 10, 0)
test(2, rod_cutter, [[1, 1]], 1, 1)
test(3, rod_cutter, [[1, 1], [2, 3]], 2, 3)
test(4, rod_cutter, [[1, 2], [2, 2]], 2, 4)
test(5, rod_cutter, [[1, 1], [2, 3]], 4, 6)
test(6, rod_cutter, [[1, 1], [2, 3], [3, 4]], 2, 3)
test(7, rod_cutter, [[1, 1], [2, 5], [3, 8], [4, 9], [5, 10], [6, 17], [7, 17], [8, 20]], 8, 22)
test(8, rod_cutter, [[1, 1], [2, 5], [3, 8], [4, 9], [5, 10], [6, 17], [7, 17], [8, 20]], 15, 42)
test(9, rod_cutter, [[1, 1], [2, 5], [3, 8], [4, 9], [5, 10], [6, 17], [7, 17], [8, 20]], 23, 64)
test(10, rod_cutter, [[1, 1], [2, 5], [3, 8], [4, 9], [5, 10], [6, 17], [7, 17], [8, 20]], 29, 81)
