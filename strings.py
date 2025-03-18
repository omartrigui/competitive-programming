def is_plalindrome(string):
    string = list(string)
    length = len(string)
    left = 0
    right = length - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


def manacher(preS):
    s = '#' + '#'.join(preS) + '#'
    l = len(s)
    RL = [0] * l
    maxRight = pos = maxLen = 0
    for i in range(l):
        if i < maxRight:
            RL[i] = min(RL[2 * pos - i], maxRight - i)
        else:
            RL[i] = 1
        while i - RL[i] >= 0 and i + RL[i] < l and s[i - RL[i]] == s[i + RL[i]]:
            RL[i] += 1
        if i + RL[i] - 1 > maxRight:
            maxRight = i + RL[i] - 1
            pos = i
    maxLen = max(RL)
    idx = RL.index(maxLen)
    sub = s[idx - maxLen + 1: idx + maxLen]
    return sub.replace('#', '')


def longest_palindrome_prefix(s):
    if not s:
        return 0
    s = s + '#' + s[::-1] + '$'
    i = 0
    j = -1
    nt = [0] * len(s)
    nt[0] = -1
    while i < len(s) - 1:
        if j == -1 or s[i] == s[j]:
            i += 1
            j += 1
            nt[i] = j
        else:
            j = nt[j]
    return nt[len(s) - 1]
