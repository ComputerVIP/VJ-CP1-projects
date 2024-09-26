#Create a program with a function that that takes in a users string and uses a shift cypher to turn the string into a secret code. 

#BONUS: 

#Write another function that decodes someone else's secret message. 

def code():
    var = input("What do you want to encode?")
    inpt = int(input("How many do you want to shift it? (Maximum 26)\n"))
    if inpt > 26:
        print("I said up to 26!")
        return
    var = var.lower()
    a = str(1 + inpt)
    b = str(2 + inpt)
    c = str(3 + inpt)
    d = str(4 + inpt)
    e = str(5 + inpt)
    f = str(6 + inpt)
    g = str(7 + inpt)
    h = str(8 + inpt)
    i = str(9 + inpt)
    j = str(10 + inpt)
    k = str(11 + inpt)
    l = str(12 + inpt)
    m = str(13 + inpt)
    n = str(14 + inpt)
    o = str(15 + inpt)
    p = str(16 + inpt)
    q = str(17 + inpt)
    r = str(18 + inpt)
    s = str(19 + inpt)
    t = str(20 + inpt)
    u = str(21 + inpt)
    v = str(22 + inpt)
    w = str(23 + inpt)
    x = str(24 + inpt)
    y = str(25 + inpt)
    z = str(26 + inpt)
    var1 = var.replace("a", a).replace("b", b).replace("c", c).replace("d", d).replace("e", e).replace("f", f).replace("g", g).replace("h", h).replace("i", i)
    var1 = var1.replace("j", j).replace("k", k).replace("l", l).replace("m", m).replace("n", n).replace("o", o).replace("p", p).replace("q", q).replace("r", r)
    var1 = var1.replace("s", s).replace("t", t).replace("u", u).replace("v", v).replace("w", w).replace("x", x).replace("y", y).replace("z", z)
    #var2 = (var2.translate({ord(i): None for i in 'abcdefghi'})

    print(f"\n\n{var},\n{var1}")
code()