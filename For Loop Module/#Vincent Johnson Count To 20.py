#Vincent Johnson Count To 20
no = "Hello there I am a person"
hi = 0
def snd(hi, no):
    for i in no:
        hi = hi - 1
        print(hi)
        if hi == 0:
            return
for i in no:
    hi += 1
    print(hi)
    if hi == 20:
        snd(hi, no)
        break