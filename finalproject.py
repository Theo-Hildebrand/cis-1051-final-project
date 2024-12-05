import random

scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}


data = open("NWL2023_7_csv.txt", "r", encoding="utf8")

str1 = data.read()

wordlist = str1.split(",")


data2 = open("NWL2023_7_csv_sorted.txt", "r", encoding = "utf8")

str2 = data2.read()

sortedlist = str2.split(",")


def permutate(rack):
    a = rack[0] + rack[1]
    b = rack[0] + rack[2]
    c = rack[0] + rack[3]
    d = rack[0] + rack[4]
    e = rack[0] + rack[5]
    f = rack[0] + rack[6]
    g = rack[1] + rack[2]
    h = rack[1] + rack[3]
    i = rack[1] + rack[4]
    j = rack[1] + rack[5]
    k = rack[1] + rack[6]
    l = rack[2] + rack[3]
    m = rack[2] + rack[4]
    n = rack[2] + rack[5]
    o = rack[2] + rack[6]
    p = rack[3] + rack[4]
    q = rack[3] + rack[5]
    r = rack[3] + rack[6]
    s = rack[4] + rack[5]
    t = rack[4] + rack[6]
    u = rack[5] + rack[6]
    aa = rack[0] + rack[1] + rack[2]
    ab = rack[0] + rack[1] + rack[3]
    ac = rack[0] + rack[1] + rack[4]
    ad = rack[0] + rack[1] + rack[5]
    ae = rack[0] + rack[1] + rack[6]
    af = rack[0] + rack[2] + rack[3]
    ag = rack[0] + rack[2] + rack[4]
    ah = rack[0] + rack[2] + rack[5]
    ai = rack[0] + rack[2] + rack[6]
    aj = rack[0] + rack[3] + rack[4]
    ak = rack[0] + rack[3] + rack[5]
    al = rack[0] + rack[3] + rack[6]
    am = rack[0] + rack[4] + rack[5]
    an = rack[0] + rack[4] + rack[6]
    ao = rack[0] + rack[5] + rack[6]
    ap = rack[1] + rack[2] + rack[3]
    aq = rack[1] + rack[2] + rack[4]
    ar = rack[1] + rack[2] + rack[5]
    at = rack[1] + rack[2] + rack[6]
    au = rack[1] + rack[3] + rack[4]
    av = rack[1] + rack[3] + rack[5]
    aw = rack[1] + rack[3] + rack[6]
    ax = rack[1] + rack[4] + rack[5]
    ay = rack[1] + rack[4] + rack[6]
    az = rack[1] + rack[5] + rack[6]
    ba = rack[2] + rack[3] + rack[4]
    bb = rack[2] + rack[3] + rack[5]
    bc = rack[2] + rack[3] + rack[6]
    bd = rack[2] + rack[4] + rack[5]
    be = rack[2] + rack[4] + rack[6]
    bf = rack[2] + rack[5] + rack[6]
    bg = rack[3] + rack[4] + rack[5]
    bh = rack[3] + rack[4] + rack[6]
    bi = rack[3] + rack[5] + rack[6]
    bj = rack[4] + rack[5] + rack[6]
    ca = rack[0] + rack[1] + rack[2] + rack[3]
    cb = rack[0] + rack[1] + rack[2] + rack[4]
    cc = rack[0] + rack[1] + rack[2] + rack[5]
    cd = rack[0] + rack[1] + rack[2] + rack[6]
    ce = rack[0] + rack[1] + rack[3] + rack[4]
    cf = rack[0] + rack[1] + rack[3] + rack[5]
    cg = rack[0] + rack[1] + rack[3] + rack[6]
    ch = rack[0] + rack[1] + rack[4] + rack[5]
    ci = rack[0] + rack[1] + rack[4] + rack[6]
    cj = rack[0] + rack[1] + rack[5] + rack[6]
    ck = rack[0] + rack[2] + rack[3] + rack[4]
    cl = rack[0] + rack[2] + rack[3] + rack[5]
    cm = rack[0] + rack[2] + rack[3] + rack[6]
    cn = rack[0] + rack[2] + rack[4] + rack[5]
    co = rack[0] + rack[2] + rack[4] + rack[6]
    cp = rack[0] + rack[2] + rack[5] + rack[6]
    cq = rack[0] + rack[3] + rack[4] + rack[5]
    cr = rack[0] + rack[3] + rack[4] + rack[6]
    cs = rack[0] + rack[3] + rack[5] + rack[6]
    ct = rack[0] + rack[4] + rack[5] + rack[6]
    cu = rack[1] + rack[2] + rack[3] + rack[4]
    cv = rack[1] + rack[2] + rack[3] + rack[5]
    cw = rack[1] + rack[2] + rack[3] + rack[6]
    cx = rack[1] + rack[2] + rack[4] + rack[5]
    cy = rack[1] + rack[2] + rack[4] + rack[6]
    cz = rack[1] + rack[2] + rack[5] + rack[6]
    da = rack[1] + rack[3] + rack[4] + rack[5]
    db = rack[1] + rack[3] + rack[4] + rack[6]
    dc = rack[1] + rack[3] + rack[5] + rack[6]
    dd = rack[1] + rack[4] + rack[5] + rack[6]
    de = rack[2] + rack[3] + rack[4] + rack[5]
    df = rack[2] + rack[3] + rack[4] + rack[6]
    dg = rack[2] + rack[3] + rack[5] + rack[6]
    dh = rack[2] + rack[4] + rack[5] + rack[6]
    di = rack[3] + rack[4] + rack[5] + rack[6]
    ea = rack[0] + rack[1] + rack[2] + rack[3] + rack[4]
    eb = rack[0] + rack[1] + rack[2] + rack[3] + rack[5]
    ec = rack[0] + rack[1] + rack[2] + rack[3] + rack[6]
    ed = rack[0] + rack[1] + rack[2] + rack[4] + rack[5]
    ee = rack[0] + rack[1] + rack[2] + rack[4] + rack[6]
    ef = rack[0] + rack[1] + rack[2] + rack[5] + rack[6]
    eg = rack[0] + rack[1] + rack[3] + rack[4] + rack[5]
    eh = rack[0] + rack[1] + rack[3] + rack[4] + rack[6]
    ei = rack[0] + rack[1] + rack[3] + rack[5] + rack[6]
    ej = rack[0] + rack[1] + rack[4] + rack[5] + rack[6]
    ek = rack[0] + rack[2] + rack[3] + rack[4] + rack[5]
    el = rack[0] + rack[2] + rack[3] + rack[4] + rack[6]
    em = rack[0] + rack[2] + rack[3] + rack[5] + rack[6]
    en = rack[0] + rack[2] + rack[4] + rack[5] + rack[6]
    eo = rack[0] + rack[3] + rack[4] + rack[5] + rack[6]
    ep = rack[1] + rack[2] + rack[3] + rack[4] + rack[5]
    eq = rack[1] + rack[2] + rack[3] + rack[4] + rack[6]
    er = rack[1] + rack[2] + rack[3] + rack[5] + rack[6]
    es = rack[1] + rack[2] + rack[4] + rack[5] + rack[6]
    et = rack[1] + rack[3] + rack[4] + rack[5] + rack[6]
    eu = rack[2] + rack[3] + rack[4] + rack[5] + rack[6]
    fa = rack[0] + rack[1] + rack[2] + rack[3] + rack[4] + rack[5]
    fb = rack[0] + rack[1] + rack[2] + rack[3] + rack[4] + rack[6]
    fc = rack[0] + rack[1] + rack[2] + rack[3] + rack[5] + rack[6]
    fd = rack[0] + rack[1] + rack[2] + rack[4] + rack[5] + rack[6]
    fe = rack[0] + rack[1] + rack[3] + rack[4] + rack[5] + rack[6]
    ff = rack[0] + rack[2] + rack[3] + rack[4] + rack[5] + rack[6]
    fg = rack[1] + rack[2] + rack[3] + rack[4] + rack[5] + rack[6]
    ga = rack[0] + rack[1] + rack[2] + rack[3] + rack[4] + rack[5] + rack[6]

    permutations = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw, ax, ay, az, ba, bb, bc, bd, be, bf, bg, bh, bi, bj, ca, cb, cc, cd, ce, cf, cg, ch, ci, cj, ck, cl, cm, cn, co, cp, cq, cr, cs, ct, cu, cv, cw, cx, cy, cz, da, db, dc, dd, de, df, dg, dh, di, ea, eb, ec, ed, ee, ef, eg, eh, ei, ej, ek, el, em, en, eo, ep, eq, er, es, et, eu, fa, fb, fc, fd, fe, ff, fg, ga]
    return permutations
    

def score(word):
    points = 0
    for c in word:
        points = points + scores[c]
    return points

rack = random.choice('qwrtypsdfghjklzxcvbnm')+random.choice('qwrtypsdfghjklzxcvbnm')+random.choice('qwrtypsdfghjklzxcvbnm')+random.choice('aeiou')+random.choice('aeiou')+random.choice('aeiou')+"?"
print(rack)

rack = rack.lower()

if len(rack) != 7:
    print("Invalid rack length. Try again.")

count = 0
for c in rack:
    if c not in "qwertyuiopasdfghjklzxcvbnm?":
        count = count + 1
if count != 0:
    print("Invalid characters. Try again.")


def alphagram(rack):
    alpha = ''
    racksorted = sorted(rack)
    for c in racksorted:
        alpha = alpha + c
    if "?" in alpha and "??" not in alpha:
        alpha = alpha[1:7] + "?"             
    elif "??" in alpha:
        alpha = alpha[2:7] + "??"      # Put the blanks at the end - it doesn't make the code more efficient, but it's convention for Scrabble players, so it's what I'm used to
    return alpha

def high_letters(word):
    high_letters = []
    if len(word) == 5:
        maxi = max(scores[word[0]], scores[word[4]])
        for num in [0, 4]:
            if scores[word[num]] == maxi:
                high_letters += [word[num], scores[word[num]], num+1]
    if len(word) == 6:
        maxi = max(scores[word[0]], scores[word[1]], scores[word[4]], scores[word[5]])
        for num in [0, 1, 4, 5]:
            if scores[word[num]] == maxi:
                high_letters += [word[num], scores[word[num]], num+1]
    if len(word) == 7:
        maxi = max(scores[word[0]], scores[word[1]], scores[word[2]], scores[word[4]], scores[word[5]], scores[word[6]])
        for num in [0, 1, 2, 4, 5, 6]:
            if scores[word[num]] == maxi:
                high_letters += [word[num], scores[word[num]], num+1]
    return high_letters
                   

def high_word(rack):
    alpha = alphagram(rack)
    x = []
    y = permutate(alpha)
    for a in y:
        if a not in x:
            x = x + [a]       # x is the list of unique permutations of the rack

    max_score = 0
    for perm in x:
        if perm in sortedlist:
            potential_words = []
            for num in range(len(wordlist)):
                if sortedlist[num] == perm:
                    potential_words = potential_words + [wordlist[num]]
                for word in potential_words:
                    points = 0
                    for c in word:
                        points = points + scores[c]
                    if len(word) == 5:
                        points = points + max(scores[word[0]], scores[word[4]])
                    if len(word) == 6:
                        points = points + max(scores[word[0]], scores[word[1]], scores[word[4]], scores[word[5]])
                    if len(word) == 7:
                        points = points + max(scores[word[0]], scores[word[1]], scores[word[2]], scores[word[4]], scores[word[5]], scores[word[6]])
                        points = points + 25     # Bingo score (divided by two)
                    if points > max_score:
                        max_score = points
                        high_word = word
                        
    max_score = max_score * 2
    if max_score == 0:
        high_word = ''
    return [high_word, max_score]

def blank_score(rack, blank_char):                     # The rack, including the blank, along with what the blank is imitating 
    alpha = alphagram(rack)                            # Alphabetize the rack
    alpha = alphagram(alpha[0:6] + blank_char)         # Replace the blank with the character in question, then alphabetize it again
    x = []
    y = permutate(alpha)
    for a in y:
        if a not in x:
            x = x + [a]


    max_score = 0
    for perm in x:
        if perm in sortedlist:
            potential_words = []
            for num in range(len(wordlist)):
                if sortedlist[num] == perm:
                    potential_words = potential_words + [wordlist[num]]
                for word in potential_words:
                    points = 0
                    count = 0
                    for c in word:
                        if c == blank_char:
                            count = count + 1
                            if count > rack.count(blank_char):   # If more of the imitated tile are used than there are naturals on the rack, a blank must be used, netting zero points.
                                points = points
                            else:
                                points = points + scores[c]    
                        else:
                            points = points + scores[c]
                    if len(word) == 5:
                        if rack.count(blank_char) > 0:
                            points = points + max(scores[word[0]], scores[word[4]])
                        else:
                            if blank_char == word[0]:
                                points = points + scores[word[4]]
                            elif blank_char == word[4]:
                                points = points + scores[word[0]]
                            else:
                                points = points + max(scores[word[0]], scores[word[4]])
                    if len(word) == 6:
                        if rack.count(blank_char) > 0:
                            points = points + max(scores[word[0]], scores[word[1]], scores[word[4]], scores[word[5]])
                        else:
                            if blank_char == word[0]:
                                points = points + max(scores[word[1]], scores[word[4]], scores[word[5]])
                            elif blank_char == word[1]:
                                points = points + max(scores[word[0]], scores[word[4]], scores[word[5]])
                            elif blank_char == word[4]:
                                points = points + max(scores[word[0]], scores[word[1]], scores[word[5]])
                            elif blank_char == word[5]:
                                points = points + max(scores[word[0]], scores[word[1]], scores[word[4]])
                            else:
                                points = points + max(scores[word[0]], scores[word[1]], scores[word[4]], scores[word[5]])
                    if len(word) == 7:
                        if rack.count(blank_char) > 0:
                            points = points + max(scores[word[0]], scores[word[1]], scores[word[2]], scores[word[4]], scores[word[5]], scores[word[6]])
                        else:
                            if blank_char == word[0]:
                                points = points + max(scores[word[1]], scores[word[2]], scores[word[4]], scores[word[5]], scores[word[6]])
                            elif blank_char == word[1]:
                                points = points + max(scores[word[0]], scores[word[2]], scores[word[4]], scores[word[5]], scores[word[6]])
                            elif blank_char == word[2]:
                                points = points + max(scores[word[0]], scores[word[1]], scores[word[4]], scores[word[5]], scores[word[6]])
                            elif blank_char == word[4]:
                                points = points + max(scores[word[0]], scores[word[1]], scores[word[2]], scores[word[5]], scores[word[6]])
                            elif blank_char == word[5]:
                                points = points + max(scores[word[0]], scores[word[1]], scores[word[2]], scores[word[4]], scores[word[6]])
                            elif blank_char == word[6]:
                                points = points + max(scores[word[0]], scores[word[1]], scores[word[2]], scores[word[4]], scores[word[5]])
                            else:
                                points = points + max(scores[word[0]], scores[word[1]], scores[word[2]], scores[word[4]], scores[word[5]], scores[word[6]])
                        points = points + 25
                    if points > max_score:
                        max_score = points
                        high_word = word
                        
    max_score = max_score * 2
    if max_score == 0:
        high_word = ''
        
    return [high_word, max_score]
                            
    
                        


def high_word_blank(rack):
    alpha = alphagram(rack)
    poss = []
    for char in "qwertyuiopasdfghjklzxcvbnm":
        poss = poss + [blank_score(alpha, char)]
    
    max_poss = 0
    for p in poss:
        if p[1] > max_poss:
            high_poss = p[0]
            max_poss = p[1]
            
    return [high_poss, max_poss] 


        
if "?" in rack:
    result = high_word_blank(rack)
    print(result[0])
    print(result[1])
else:
    result = high_word(rack)
    print(result[0])
    print(result[1])









# The program so far: Accurately (I hope) finds the highest-scoring play and its
# associated score. Can incorporate a single blank with appropriate score.
# Todo: Blanks, strategic use of s's and blanks, visuals.


