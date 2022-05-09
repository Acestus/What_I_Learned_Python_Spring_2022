squares = {1: 1, 3: 9, 5: 25, 6: 36, 8: 64, 10: 100, 11: 121, 15: 225}
user_input = int(input())
answer = squares.pop(user_input, 'There is no such key')
print(answer)
print(squares)