def next_bigger(n):
    s_num = list(map(int, str(n)))
    if s_num == sorted(s_num, reverse=True):
        return -1
    for i in range(len(s_num)-1,0,-1):
        if s_num[i] > s_num[i-1]:
            s_num[i:] = sorted(s_num[i:])
            for j in range(len(s_num[i:])):
                if s_num[i+j] > s_num[i-1]:
                    temp = s_num[i-1]
                    s_num[i-1] = s_num[i+j]
                    s_num[i+j] = temp
                    break
            break
    return int(''.join(str(i) for i in s_num))
