import pygame
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
        return 3
    if num == 1:
        return 2
    if num == 2:
        return 1
    if num == 4:
        return 7
    if num == 5:
        return 6
    if num == 6:
        return 5     # Takes the position of the highest-scoring tile that can hit the double-letter square and returns what the starting location should be in order for that tile to lie on the square

def doubled_letter(word):
    if len(word) < 5:
        return None
    if len(word) == 5:
        maxi = 0
        for num in [0, 4]:
            if scores[word[num]] > maxi:
                maxi = scores[word[num]]
                high_letter = [word[num], position(num)] 
    if len(word) == 6:
        maxi = 0
        for num in [0, 1, 4, 5]:
            if scores[word[num]] > maxi:
                maxi = scores[word[num]]
                high_letter = [word[num], position(num)] 
    if len(word) == 7:
        maxi = 0
        for num in [0, 1, 2, 4, 5, 6]:
            if scores[word[num]] > maxi:
                maxi = scores[word[num]]
                high_letter = [word[num], position(num)]
    return high_letter                                     # Returns the high letter, along with position

def doubled_letter_blank(word, blank_char):
    new_scores = {}
    count = 0
    for c in word:
        if c == blank_char:
            count += 1
    if count > 1:                               # If the word has more than one of the imitated tile, that means there is at least one natural (assuming only one blank), so you don't have to worry about doubling the blank 
        new_scores = scores
    else:
        for c in "qwertyuiopasdfghjklzxcvbnm":
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
                high_letter = [word[num], position(num)] 
    if len(word) == 6:
        maxi = 0
        for num in [0, 1, 4, 5]:
            if new_scores[word[num]] > maxi:
                maxi = new_scores[word[num]]
                high_letter = [word[num], position(num)] 
    if len(word) == 7:
        maxi = 0
        for num in [0, 1, 2, 4, 5, 6]:
            if new_scores[word[num]] > maxi:
                maxi = new_scores[word[num]]
                high_letter = [word[num], position(num)]
    return high_letter                                         # Returns the high letter, along with position
        
        


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


def the_big_one(rack):
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

        if result == high_blank:
            if len(result[0]) >= 5:
                x = doubled_letter_blank(result[0], result[2])
                result = result + [x[1]]
            else:
                result = result + [6]    # Arbitrarily chosen position value if double-letter cannot be reached
            result = [result[0], result[1], result[3], result[2]]
        else:
            if len(result[0]) >= 5:
                x = doubled_letter(result[0])
                result = result + [x[1], "0"]    # "0" added so result[3] can be referred to even if blank not used
            else:
                result = result + [6, "0"]  
        return result

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
        if len(result[0]) >= 5:
            x = doubled_letter(result[0])
            result = result + [x[1], "0"]          
        else:
            result = result + [6, "0"]

        return result


############################################### PYGAME INCOMING ######################################################


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

board = pygame.image.load("ScrabbleBoard.png")
input_box = pygame.image.load("input_box.png")
a_ = pygame.image.load("A__.png")
b_ = pygame.image.load("B__.png")
c_ = pygame.image.load("C__.png")
d_ = pygame.image.load("D__.png")
e_ = pygame.image.load("E__.png")
f_ = pygame.image.load("F__.png")
g_ = pygame.image.load("G__.png")
h_ = pygame.image.load("H__.png")
i_ = pygame.image.load("I__.png")
j_ = pygame.image.load("J__.png")
k_ = pygame.image.load("K__.png")
l_ = pygame.image.load("L__.png")
m_ = pygame.image.load("M__.png")
n_ = pygame.image.load("N__.png")
o_ = pygame.image.load("O__.png")
p_ = pygame.image.load("P__.png")
q_ = pygame.image.load("Q__.png")
r_ = pygame.image.load("R__.png")
s_ = pygame.image.load("S__.png")
t_ = pygame.image.load("T__.png")
u_ = pygame.image.load("U__.png")
v_ = pygame.image.load("V__.png")
w_ = pygame.image.load("W__.png")
x_ = pygame.image.load("X__.png")
y_ = pygame.image.load("Y__.png")
z_ = pygame.image.load("Z__.png")
__ = pygame.image.load("___.png")
_1 = pygame.image.load("1_.png")
_2 = pygame.image.load("2_.png")
_3 = pygame.image.load("3_.png")
_4 = pygame.image.load("4_.png")
_5 = pygame.image.load("5_.png")
_6 = pygame.image.load("6_.png")
_7 = pygame.image.load("7_.png")
_8 = pygame.image.load("8_.png")
_9 = pygame.image.load("9_.png")
_0 = pygame.image.load("0_.png")
zero = pygame.image.load("redzero.png")

def print_a(loc):
    screen.blit(a_, loc)
def print_b(loc):
    screen.blit(b_, loc)
def print_c(loc):
    screen.blit(c_, loc)
def print_d(loc):
    screen.blit(d_, loc)
def print_e(loc):
    screen.blit(e_, loc)
def print_f(loc):
    screen.blit(f_, loc)
def print_g(loc):
    screen.blit(g_, loc)
def print_h(loc):
    screen.blit(h_, loc)
def print_i(loc):
    screen.blit(i_, loc)
def print_j(loc):
    screen.blit(j_, loc)
def print_k(loc):
    screen.blit(k_, loc)
def print_l(loc):
    screen.blit(l_, loc)
def print_m(loc):
    screen.blit(m_, loc)
def print_n(loc):
    screen.blit(n_, loc)
def print_o(loc):
    screen.blit(o_, loc)
def print_p(loc):
    screen.blit(p_, loc)
def print_q(loc):
    screen.blit(q_, loc)
def print_r(loc):
    screen.blit(r_, loc)
def print_s(loc):
    screen.blit(s_, loc)
def print_t(loc):
    screen.blit(t_, loc)
def print_u(loc):
    screen.blit(u_, loc)
def print_v(loc):
    screen.blit(v_, loc)
def print_w(loc):
    screen.blit(w_, loc)
def print_x(loc):
    screen.blit(x_, loc)
def print_y(loc):
    screen.blit(y_, loc)
def print_z(loc):
    screen.blit(z_, loc)
def print_1(loc):
    screen.blit(_1, loc)
def print_2(loc):
    screen.blit(_2, loc)
def print_3(loc):
    screen.blit(_3, loc)
def print_4(loc):
    screen.blit(_4, loc)
def print_5(loc):
    screen.blit(_5, loc)
def print_6(loc):
    screen.blit(_6, loc)
def print_7(loc):
    screen.blit(_7, loc)
def print_8(loc):
    screen.blit(_8, loc)
def print_9(loc):
    screen.blit(_9, loc)
def print_0(loc):
    screen.blit(_0, loc)

loc = [0, 0]
print_dict = {"a": print_a, "b": print_b, "c": print_c, "d": print_d, "e": print_e, "f": print_f, "g": print_g, "h": print_h, "i": print_i, "j": print_j, "k": print_k, "l": print_l, "m": print_m, "n": print_n, "o": print_o, "p": print_p, "q": print_q, "r": print_r, "s": print_s, "t": print_t, "u": print_u, "v": print_v, "w": print_w, "x": print_x, "y": print_y, "z": print_z, "1": print_1, "2": print_2, "3": print_3, "4": print_4, "5": print_5, "6": print_6, "7": print_7, "8": print_8, "9": print_9, "0": print_0}

count = 0
tiles_placed = 0
num_blanks = 0
word_played = 0
blank_char_amt = 0
rack = ""

screen.blit(board, [0, 0])
screen.blit(input_box, [463, 576])


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            count = 0
        if event.type == pygame.KEYDOWN:
            if word_played == 1:
                screen.blit(board, [0,0])
                screen.blit(input_box, [463, 576])
                rack = ""
                tiles_placed = 0
                word_played = 0
                num_blanks = 0
                

    keys = pygame.key.get_pressed()

    if count == 0:
        if len(rack) < 7:
            if keys[pygame.K_a]:
                print_a([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "a"
            elif keys[pygame.K_b]:
                print_b([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "b"
            elif keys[pygame.K_c]:
                print_c([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "c"
            elif keys[pygame.K_d]:
                print_d([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "d"
            elif keys[pygame.K_e]:
                print_e([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "e"
            elif keys[pygame.K_f]:
                print_f([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "f"
            elif keys[pygame.K_g]:
                print_g([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "g"
            elif keys[pygame.K_h]:
                print_h([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "h"
            elif keys[pygame.K_i]:
                print_i([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "i"
            elif keys[pygame.K_j]:
                print_j([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "j"
            elif keys[pygame.K_k]:
                print_k([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "k"
            elif keys[pygame.K_l]:
                print_l([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "l"
            elif keys[pygame.K_m]:
                print_m([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "m"
            elif keys[pygame.K_n]:
                print_n([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "n"
            elif keys[pygame.K_o]:
                print_o([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "o"
            elif keys[pygame.K_p]:
                print_p([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "p"
            elif keys[pygame.K_q]:
                print_q([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "q"
            elif keys[pygame.K_r]:
                print_r([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "r"
            elif keys[pygame.K_s]:
                print_s([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "s"
            elif keys[pygame.K_t]:
                print_t([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "t"
            elif keys[pygame.K_u]:
                print_u([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "u"
            elif keys[pygame.K_v]:
                print_v([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "v"
            elif keys[pygame.K_w]:
                print_w([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "w"
            elif keys[pygame.K_x]:
                print_x([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "x"
            elif keys[pygame.K_y]:
                print_y([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "y"
            elif keys[pygame.K_z]:
                print_z([474 + (tiles_placed * 48), 578])
                tiles_placed += 1
                count = 1
                rack += "z"
            elif keys[pygame.K_SPACE] and num_blanks == 0:
                screen.blit(__, [474 + (tiles_placed * 48), 578])
                tiles_placed +=1
                count = 1
                num_blanks = 1
                rack += "?"
        if keys[pygame.K_BACKSPACE]:
            if tiles_placed > 0:
                screen.blit(board, [474 + (48*(tiles_placed - 1)), 578], pygame.Rect(474 + (48*(tiles_placed - 1)), 578, 44, 44))
                screen.blit(input_box, [474 + (48*(tiles_placed - 1)), 578], pygame.Rect(10, 0, 44, 44))
                tiles_placed -= 1
                count = 1
                rack = rack[0:len(rack) - 1]
                if "?" not in rack:
                    num_blanks = 0
        if keys[pygame.K_RETURN]:
            count = 1
            if len(rack) == 7:
                screen.blit(board, [0,0])
                screen.blit(input_box, [463, 576])
                tiles_placed = 0
                result = the_big_one(rack)
                blank_char_amt = result[0].count(result[3])
                if blank_char_amt == 0:
                    for c in result[0]:     
                        loc = [282 + (48*(tiles_placed + result[2])), 338]
                        print_dict[c](loc)
                        tiles_placed += 1          # Place the tiles corresponding to the letters of the word on the board
                else:
                    pos_order = []
                    for i in range(len(result[0])):
                        pos_order += [i]
                    if len(result[0]) >= 5:
                        if result[2] in [1, 2, 3]:
                            doubled_letter_pos = pos_order.index(3 - result[2])
                            del pos_order[doubled_letter_pos]
                            pos_order = [doubled_letter_pos] + pos_order   # Move the position that falls on the double letter tile to the first in the queue
                        elif result[2] in [5, 6, 7]:
                            doubled_letter_pos = pos_order.index(11 - result[2])
                            del pos_order[doubled_letter_pos]
                            pos_order = [doubled_letter_pos] + pos_order
                    blank_char_count = 0
                    for pos in pos_order:
                        c = result[0][pos]
                        loc = [282 + (48*(pos + result[2])), 338]
                        print_dict[c](loc)
                        if c == result[3]:
                            blank_char_count += 1
                            if blank_char_count == blank_char_amt:
                                screen.blit(zero, [loc[0] + 28, loc[1] + 25])
                                input_box.set_alpha(50)
                                screen.blit(input_box, loc, pygame.Rect(10, 0, 44, 44))
                                input_box.set_alpha(255)                                   # Visually marks the blank tile with a score of zero and a slight darkening

                    # Alright, this whole song and dance is just to ensure that, if the blank is imitating a tile that you also have a natural copy of, and that letter
                    # falls on the double letter score in order to maximize score, it's the natural, and not the blank, that is shown to fall on the double letter score.
                    # It does this by placing the tiles down in a certain order, with the tile that falls on the double letter score being placed first, and marking as the
                    # blank the copy of the imitated tile that comes down last. (At least, that's the idea. It works with my test words, but something may well have slipped
                    # through the cracks)                           
                        
                word_played = 1
                loc[0] += 50
                loc[1] -= 21
                for digit in str(result[1]):
                    print_dict[digit](loc)
                    loc[0] += 12                  # Place the digits of the score         


    pygame.display.flip()

pygame.quit()




# The program so far: Accurately (I hope) finds the highest-scoring play and its associated score. Can incorporate a single blank with
# appropriate score, and refrains from using an s (unless the rack has multiple s's) or a blank unless the score gain is high enough
# (currently 10 and 30 points respectively). Adding the potential of another blank would be a bit of a hassle - and, with my coding style
# (that is to say, my utter lack of efficiency), doing so would probably increase the runtime to a comical degree, so this program can
# only handle a single blank. Accurately works out where a word should be situated to maximize score - it's a bloated mess, but it works!
# Todo: Change visually the blank character used, make sure the correct tile is marked, error sound alteration


