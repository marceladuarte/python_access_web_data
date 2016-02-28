import re

file = open("file_task.txt");

sum = 0

for line in file:
    num_str = re.findall("[0-9]+", line)
    for string in num_str:
        sum = sum+ int(string)

print sum
