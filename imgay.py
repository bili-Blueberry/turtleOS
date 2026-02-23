import time
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
doc = "Hello world Im Gay"
x = ""
for i in doc:
    for j in letters:
        if i == j:
            x += i
        print(x + j)
        time.sleep(0.001)
for i in range(100):
    print(x)
    time.sleep(0.01)