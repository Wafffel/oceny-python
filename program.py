dict1 = {}
b_key = 0
b_mark = 0
with open('oceny.txt') as f:
    line = f.readline()
    while True:
        line = f.readline()
        if not line:
            # print(dict1)
            break
        row = line.strip().split(";")
        if not row[0] in dict1:
            dict1[row[0]]=[int(row[1]), 1]
        else:
            dict1[row[0]][0] += int(row[1])
            dict1[row[0]][1] += 1
        # print(row)

    for key in dict1:
        average = dict1[key][0]/dict1[key][1]
        if average > b_mark:
            b_mark = average
            b_key = key

with open('uczniowie.txt') as g:
    line = g.readline()
    while True:
        line = g.readline()
        if not line:
            break
        row = line.strip().split(";")
        if row[0]==b_key:
            print(f"{row[2]} {row[1]} {b_mark}")
            break
        # print(row)