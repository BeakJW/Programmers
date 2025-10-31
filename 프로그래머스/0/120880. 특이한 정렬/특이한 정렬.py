def solution(numlist, n):
    length = len(numlist)
    for i in range(length - 1):
        min_idx = i
        for j in range(i + 1, length):
            if (abs(numlist[j] - n), -numlist[j]) < (abs(numlist[min_idx] - n), -numlist[min_idx]):
                min_idx = j
        numlist[i], numlist[min_idx] = numlist[min_idx], numlist[i]
    return numlist
