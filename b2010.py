import imp


import sys

num = int(sys.stdin.readline())
computer = 0

for i in range(num) :
    computer += int(sys.stdin.readline())
print(computer - (num-1))