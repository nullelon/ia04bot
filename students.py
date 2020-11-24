with open("students.txt", "r") as f:
    lines = f.read().splitlines()
students = dict()

for line in lines:
    fields = line.split()
    if len(fields) == 3 and fields[0].isnumeric():
        students[int(fields[0])] = fields[1:]
