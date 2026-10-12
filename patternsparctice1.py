n = 5

for i in range(1, n + 1):
    ch=64
    for j in range(1, i + 1):
        print(chr(ch+1), end="")
        ch = ch+1
    print()
