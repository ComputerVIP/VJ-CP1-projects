#Vincent Johnson RAID
count = 1
num1 = 1
num2 = 1
row = "1 |  "

print("     1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |  11 | 12")

while count < 13:
    if num1 > 12:
        count += 1
        print(row)
        num1 = 1
        num2 += 1
        if len(str(count)) == 1:
            row = (f"{count} |  ")
        elif len(str(count)) == 2:
            row = (f"{count}| ")
            if count >= 10:
                row = (f"{count}|  ")
    ans = (num1 * num2)
    ans = str(ans)
    if count >= 10:
        ans = ans + "  "
    else:
        ans = ans + " "
    row = row + ans
    
    if len(ans) == 2:
        row = row + ("  | ")
    elif len(ans) == 3:
        row = row + (" | ")
    elif len(ans) == 4:
        row = row + ("| ")
    elif len(ans) == 5:
        row = row + ("|")
    num1 += 1