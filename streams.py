import sys
# input_text = input("What is your name? ")
# print(input_text)
# without new lines
for line in sys.stdin:
    print(line, end="")
