import time

# 1.

def edition_rec(s1: str, s2: str) -> int:
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    if s1[-1] == s2[-1]:
        return min(1 + edition_rec(s1[:-1], s2), 1 + edition_rec(s1, s2[:-1]), edition_rec(s1[:-1], s2[:-1]))
    return 1 + min(edition_rec(s1[:-1], s2), edition_rec(s1, s2[:-1]), edition_rec(s1[:-1], s2[:-1]))


# print(edition_rec('abc', 'adcf'))
# t = time.time()
# edition_rec('polynomial', 'polygonal')  # Très lent
# print(time.time()-t)

# 2.

MEMO = {}


def edition_memo(s1: str, s2: str) -> int:
    if (s1, s2) in MEMO:
        return MEMO[(s1, s2)]
    if not s1:
        return len(s2)
    if not s2:
        return len(s1)
    if s1[-1] == s2[-1]:
        MEMO[(s1, s2)] = min(1 + edition_memo(s1[:-1], s2), 1 + edition_memo(s1, s2[:-1]), edition_memo(s1[:-1], s2[:-1]))
        return MEMO[(s1, s2)]
    MEMO[(s1, s2)] = 1 + min(edition_memo(s1[:-1], s2), edition_memo(s1, s2[:-1]), edition_memo(s1[:-1], s2[:-1]))
    return MEMO[(s1, s2)]


# print(edition_memo('abc', 'adcf'))
# t = time.time()
# edition_memo('polynomial', 'polygonal') # INSTANTANE WTF
# print(time.time()-t)

# 3.

def edition_memo_reconst(s1: str, s2: str) -> (int, [int]):
