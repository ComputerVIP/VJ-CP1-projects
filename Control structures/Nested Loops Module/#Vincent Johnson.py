#Vincent Johnson
grid = ['A', 'B', 'C', 'A', 'D','C', 'A', 'B', 'D', 'E','A', 'D', 'C', 'E', 'A','B', 'A', 'C', 'A', 'D','D', 'C', 'B', 'E', 'A']
cnt1 = len(grid)
cnt = 0

num = 0
counta = 0
countb = 0
countc = 0
countd = 0
counte = 0

while cnt != cnt1:
    while num != cnt1:
        if grid[num] == "A":
            counta +=1
            num += 1
            cnt +=1
        elif grid[num] == "B":
            countb +=1
            num += 1
            cnt +=1
        elif grid[num] == "C":
            countc +=1
            num += 1
            cnt +=1
        elif grid[num] == "D":
            countd +=1
            num += 1
            cnt +=1
        elif grid[num] == "E":
            counte +=1
            num += 1
            cnt +=1
        else:
            print("What are you doing computer?")
            num += 1
            cnt +=1
if cnt >= cnt1:
    print(f"A count: {counta}\nB count: {countb}\nC count: {countc}\nD count: {countd}\nE count: {counte}")