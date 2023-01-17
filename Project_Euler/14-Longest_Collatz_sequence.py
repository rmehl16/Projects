def collatz(n):
    seq_len = 0
    while n != 1:
        if (n%2) == 0:
            n = n // 2
        else:
            n = int(3*n + 1)
        seq_len += 1

    return seq_len + 1


def getLongestSequence(max_start):
    max_seq_len = 0
    start_num = 1
    for i in range(1, max_start):
        seq_len  = collatz(i)
        #print(i, seq_len)
        if seq_len > max_seq_len:
            max_seq_len = seq_len
            start_num = i
    
    return start_num, max_seq_len


if __name__ == '__main__':
    max_start = 1000000
    res1, res2 = getLongestSequence(max_start)
    print(res1, res2)
