import os

filename = "message-from-home.txt"
here = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(here, filename)

with open(filepath, "r") as f:
    content = f.read()

secret_key = "Roads? Where We're Going, We Don't Need Roads."
char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! '()"

final_str = ""
mode = -1 # 1 for encrypt, -1 for decrypt
for i in range(0, len(content)):
    if content[i] in char_set:
        temp = char_set.find(secret_key[i%len(secret_key)])+1
        char = char_set[(char_set.find(content[i])+(mode*temp))%len(char_set)]
        final_str += char
    else:
        final_str += content[i]
print(final_str) # Answer: codingquest2022
