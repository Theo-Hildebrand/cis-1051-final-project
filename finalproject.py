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

def perm6(rack):
    a = rack[0] + rack[1]
    b = rack[0] + rack[2]
    c = rack[0] + rack[3]
    d = rack[0] + rack[4]
    e = rack[0] + rack[5]
    f = rack[1] + rack[2]
    g = rack[1] + rack[3]
    h = rack[1] + rack[4]
    i = rack[1] + rack[5]
    j = rack[2] + rack[3]
    k = rack[2] + rack[4]
    l = rack[2] + rack[5]
    m = rack[3] + rack[4]
    n = rack[3] + rack[5]
    o = rack[4] + rack[5]
    aa = rack[0] + rack[1] + rack[2]
    ab = rack[0] + rack[1] + rack[3]
    ac = rack[0] + rack[1] + rack[4]
    ad = rack[0] + rack[1] + rack[5]
    ae = rack[0] + rack[2] + rack[3]
    af = rack[0] + rack[2] + rack[4]
    ag = rack[0] + rack[2] + rack[5]
    ah = rack[0] + rack[3] + rack[4]
    ai = rack[0] + rack[3] + rack[5]
    aj = rack[0] + rack[4] + rack[5]
    ak = rack[1] + rack[2] + rack[3]
    al = rack[1] + rack[2] + rack[4]
    am = rack[1] + rack[2] + rack[5]
    an = rack[1] + rack[3] + rack[4]
    ao = rack[1] + rack[3] + rack[5]
    ap = rack[1] + rack[4] + rack[5]
    aq = rack[2] + rack[3] + rack[4]
    ar = rack[2] + rack[3] + rack[5]
    at = rack[2] + rack[4] + rack[5]
    au = rack[3] + rack[4] + rack[5]
    ba = rack[0] + rack[1] + rack[2] + rack[3]
    bb = rack[0] + rack[1] + rack[2] + rack[4]
    bc = rack[0] + rack[1] + rack[2] + rack[5]
    bd = rack[0] + rack[1] + rack[3] + rack[4]
    be = rack[0] + rack[1] + rack[3] + rack[5]
    bf = rack[0] + rack[1] + rack[4] + rack[5]
    bg = rack[0] + rack[2] + rack[3] + rack[4]
    bh = rack[0] + rack[2] + rack[3] + rack[5]
    bi = rack[0] + rack[2] + rack[4] + rack[5]
    bj = rack[0] + rack[3] + rack[4] + rack[5]
    bk = rack[1] + rack[2] + rack[3] + rack[4]
    bl = rack[1] + rack[2] + rack[3] + rack[5]
    bm = rack[1] + rack[2] + rack[4] + rack[5]
    bn = rack[1] + rack[3] + rack[4] + rack[5]
    bo = rack[2] + rack[3] + rack[4] + rack[5]
    ca = rack[0] + rack[1] + rack[2] + rack[3] + rack[4]
    cb = rack[0] + rack[1] + rack[2] + rack[3] + rack[5]
    cc = rack[0] + rack[1] + rack[2] + rack[4] + rack[5]
    cd = rack[0] + rack[1] + rack[3] + rack[4] + rack[5]
    ce = rack[0] + rack[2] + rack[3] + rack[4] + rack[5]
    cf = rack[1] + rack[2] + rack[3] + rack[4] + rack[5]
    da = rack[0] + rack[1] + rack[2] + rack[3] + rack[4] + rack[5]
    permutations = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, ba, bb, bc, bd, be, bf, bg, bh, bi, bj, bk, bl, bm, bn, bo, ca, cb, cc, cd, ce, cf, da]
    return permutations

def perm5(rack):             # You know, as I get here, it occurs to me that there's probably a function out there that does this exact thing. Ah, well, I'm committed now - efficient code has nothing on Hildebrand stubbornness.
    a = rack[0] + rack[1]
    b = rack[0] + rack[2]
    c = rack[0] + rack[3]
    d = rack[0] + rack[4]
    e = rack[1] + rack[2]
    f = rack[1] + rack[3]
    g = rack[1] + rack[4]
    h = rack[2] + rack[3]
    i = rack[2] + rack[4]
    j = rack[3] + rack[4]
    aa = rack[0] + rack[1] + rack[2]
    ab = rack[0] + rack[1] + rack[3]
    ac = rack[0] + rack[1] + rack[4]
    ad = rack[0] + rack[2] + rack[3]
    ae = rack[0] + rack[2] + rack[4]
    af = rack[0] + rack[3] + rack[4]
    ag = rack[1] + rack[2] + rack[3]
    ah = rack[1] + rack[2] + rack[4]
    ai = rack[1] + rack[3] + rack[4]
    aj = rack[2] + rack[3] + rack[4]
    ak = rack[0] + rack[1] + rack[2] + rack[3]
    al = rack[0] + rack[1] + rack[2] + rack[4]
    am = rack[0] + rack[1] + rack[3] + rack[4]
    an = rack[0] + rack[2] + rack[3] + rack[4]
    ao = rack[1] + rack[2] + rack[3] + rack[4]
    ap = rack[0] + rack[1] + rack[2] + rack[3] + rack[4]
    permutations = [a, b, c, d, e, f, g, h, i, j, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap]
    return permutations

    # You know, one of the advantages to being such a novice coder is that you don't have to worry about being accused of plagiarism - where would I even find this stuff if not my own, troubled mind?


    
def score(word):
    points = 0
    for c in word:
        points = points + scores[c]
    return points

blank = 1
if blank == 0:
    rack = random.choice('qwrtypsdfghjklzxcvbnm')+random.choice('qwrtypsdfghjklzxcvbnm')+random.choice('qwrtypsdfghjklzxcvbnm')+random.choice('qwrtypsdfghjklzxcvbnm')+random.choice('aeiou')+random.choice('aeiou')+random.choice('aeiou')
elif blank == 1:
    rack = random.choice('qwrtypsdfghjklzxcvbnm')+random.choice('qwrtypsdfghjklzxcvbnm')+random.choice('qwrtypsdfghjklzxcvbnm')+random.choice('aeiou')+random.choice('aeiou')+random.choice('aeiou')+"?"
rack = 'qullis?'
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
        alpha = alpha[2:7] + "??"      # Put the blanks at the end
    return alpha

def position(num):
    if num == 0:
        return 2
    if num == 1:
        return 1
    if num == 2:
        return 0
    if num == 4:
        return 6
    if num == 5:
        return 5
    if num == 6:
        return 4     # Takes the position of the highest-scoring tile that can hit the double-letter square and returns what the starting location should be in order for that tile to lie on the square

def doubled_letter(word):
    if len(word) < 5:
        return None
    if len(word) == 5:
        maxi = 0
        for num in [0, 4]:
            if scores[word[num]] > maxi:
                maxi = scores[word[num]]
                high_letter = [word[num], scores[word[num]], position(num)] 
    if len(word) == 6:
        maxi = 0
        for num in [0, 1, 4, 5]:
            if scores[word[num]] > maxi:
                maxi = scores[word[num]]
                high_letter = [word[num], scores[word[num]], position(num)] 
    if len(word) == 7:
        maxi = 0
        for num in [0, 1, 2, 4, 5, 6]:
            if scores[word[num]] > maxi:
                maxi = scores[word[num]]
                high_letter = [word[num], scores[word[num]], position(num)]
    return high_letter

def doubled_letter_blank(word, blank_char):
    new_scores = {}
    count = 0
    for c in word:
        if c == blank_char:
            count += 1
    if count > 1:                               # If the word has more than one of the imitated tile, that means there is at least one natural (assuming only one blank), so you don't have to worry about doubling the blank 
        new_scores = scores
    else:
        for c in "qwertyuiopasdghjklzxcvbnm":
            if c == blank_char:
                new_scores[c] = 0
            else:
                new_scores[c] = scores[c]
    if len(word) < 5:
        return None
    if len(word) == 5:
        maxi = 0
        for num in [0, 4]:
            if new_scores[word[num]] > maxi:
                maxi = new_scores[word[num]]
                high_letter = [word[num], new_scores[word[num]], position(num)] 
    if len(word) == 6:
        maxi = 0
        for num in [0, 1, 4, 5]:
            if new_scores[word[num]] > maxi:
                maxi = new_scores[word[num]]
                high_letter = [word[num], new_scores[word[num]], position(num)] 
    if len(word) == 7:
        maxi = 0
        for num in [0, 1, 2, 4, 5, 6]:
            if new_scores[word[num]] > maxi:
                maxi = new_scores[word[num]]
                high_letter = [word[num], new_scores[word[num]], position(num)]
    return high_letter
        
        


def high_word(rack):
    alpha = alphagram(rack)
    if len(rack) == 7:
        x = []
        y = permutate(alpha)
        for a in y:
            if a not in x:
                x = x + [a]       # x is the list of unique permutations of the rack
    elif len(rack) == 6:
        x = []
        y = perm6(alpha)
        for a in y:
            if a not in x:
                x = x + [a]
    elif len(rack) == 5:
        x = []
        y = perm5(alpha)
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
                    points = score(word)
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
        
    return [high_word, max_score, blank_char]   
                        

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
            high_char = p[2]
            
    return [high_poss, max_poss, high_char]


       
if "?" in rack:
    alpha = alphagram(rack)
    alpha_blankless = alpha[0:6]
    high_blank = high_word_blank(alpha)
    high_blankless = high_word(alpha_blankless)
    if "s" in rack:
        alpha_sless = alpha_blankless[0:alpha_blankless.index("s")] + alpha_blankless[(alpha_blankless.index("s") + 1):]   # Removes one s from the rack
        high_sless = high_word(alpha_sless)
        if high_blankless[1] < high_sless[1] + 10:   # That is, if you cannot score ten more points using the s than not
            high_blankless = high_sless    
    if high_blank[1] >= high_blankless[1] + 30:      # That is, if you can score thirty more points using the blank than not
        result = high_blank
    else:
        result = high_blankless  
    print(result[0])
    print(result[1])
    if result == high_blank:
        print(result[2])
        if len(result[0]) >= 5:
            print(doubled_letter_blank(result[0], result[2]))
else:
    if "s" in rack:  
        rack_sless = rack[0:rack.index("s")] + rack[(rack.index("s") + 1):]
        high_s = high_word(rack)
        high_sless = high_word(rack_sless)
        if high_s[1] >= high_sless[1] + 10:          # That is, if you can score ten more points using the s than not
            result = high_s
        else:
            result = high_sless
    else:
        result = high_word(rack)
    print(result[0])
    print(result[1])
    if len(result[0]) >= 5:
        print(doubled_letter(result[0]))




# The program so far: Accurately (I hope) finds the highest-scoring play and its associated score. Can incorporate a single blank with
# appropriate score, and refrains from using an s (unless the rack has multiple s's) or a blank unless the score gain is high enough
# (currently 10 and 30 points respectively). Adding the potential of another blank would be a bit of a hassle - and, with my coding style
# (that is to say, my utter lack of efficiency), doing so would probably increase the runtime to a comical degree, so I might hold off
# on that and do it at the end if I have time. Accurately works out where a word should be situated to maximize score - all that should
# be left are the visuals.
# Todo: Visuals, second blank functionality (if the stars align).


