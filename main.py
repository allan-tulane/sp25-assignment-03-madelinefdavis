####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if S == "":
        return len(T)
    elif T == "":
        return len(S)
    elif S[0] == T[0]:
        return MED(S[1:], T[1:])
    else:
        insert = MED(S, T[1:])
        delete = MED(S[1:], T)
        substitute = MED(S[1:], T[1:])
        return 1 + min(insert, delete, substitute)

def fast_MED(S, T, cache=None):
    if cache is None:
        cache = {}

    if (S, T) in cache:
        return cache[(S, T)]

    if S == "":
        cache[(S, T)] = len(T)
    elif T == "":
        cache[(S, T)] = len(S)
    elif S[0] == T[0]:
        cache[(S, T)] = fast_MED(S[1:], T[1:], cache)
    else:
        insert = fast_MED(S, T[1:], cache)
        delete = fast_MED(S[1:], T, cache)
        substitute = fast_MED(S[1:], T[1:], cache)
        cache[(S, T)] = 1 + min(insert, delete, substitute)

    return cache[(S, T)]

def fast_align_MED(S, T, cache=None):
    if cache is None:
        cache = {}

    if (S, T) in cache:
        return cache[(S, T)]

    if S == "":
        cache[(S, T)] = (len(T), ("-" * len(T), T))
    elif T == "":
        cache[(S, T)] = (len(S), (S, "-" * len(S)))
    elif S[0] == T[0]:
        dist, (aS, aT) = fast_align_MED(S[1:], T[1:], cache)
        cache[(S, T)] = (dist, (S[0] + aS, T[0] + aT))
    else:
        insert_dist, (insS, insT) = fast_align_MED(S, T[1:], cache)
        delete_dist, (delS, delT) = fast_align_MED(S[1:], T, cache)
        sub_dist, (subS, subT) = fast_align_MED(S[1:], T[1:], cache)

        min_cost = 1 + min(insert_dist, delete_dist, sub_dist)

        if min_cost == 1 + insert_dist:
            cache[(S, T)] = (min_cost, ('-' + insS, T[0] + insT))
        elif min_cost == 1 + delete_dist:
            cache[(S, T)] = (min_cost, (S[0] + delS, '-' + delT))
        else:
            cache[(S, T)] = (min_cost, (S[0] + subS, T[0] + subT))

    return cache[(S, T)]
