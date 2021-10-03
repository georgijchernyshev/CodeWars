def encode_rail_fence_cipher(string, n):
    rails = {i:'' for i in range(n)}
    for i in range(len(string)):
        flag = i // (n-1)
        if flag % 2 == 0:
            rails[i % ((n-1) * 2)] += string[i]
        else:
            rails[(n-1) * 2 - (i % ((n-1) * 2))] += string[i]
    return ''.join([rails[i] for i in range(n)])
        
        
    
def decode_rail_fence_cipher(string, n):
    cnt_in_rails = [0 for i in range(n)]
    cycle = (n-1)*2
    cnt_of_full_cycle = len(string) // cycle
    remainder_of_division = len(string) % cycle
    for i in range(n): 
        if i !=0 and i != n-1:
            cnt_in_rails[i] = cnt_of_full_cycle * 2
        else:
            cnt_in_rails[i] = cnt_of_full_cycle
        if remainder_of_division > i:
            cnt_in_rails[i] += 1
            if cycle - remainder_of_division < i and i != n-1:
                cnt_in_rails[i] += 1
    start_index = [sum(i) for i in [cnt_in_rails[:j] for j in range(n)]]
    res_str = ''
    for i in range(0, len(string), n*2-2):
        for j in range(n):
            if cnt_in_rails[j] > 0:
                res_str += string[start_index[j]]
                start_index[j] += 1
                cnt_in_rails[j] -= 1
        for j in range(n-2, 0, -1):
            if cnt_in_rails[j] > 0:
                res_str += string[start_index[j]]
                start_index[j] += 1
                cnt_in_rails[j] -= 1
    return res_str
