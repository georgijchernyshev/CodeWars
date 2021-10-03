import re
def solution(string,markers):
    str = string.split('\n')
    if markers:
        str = [re.sub(r'\s*?[' + re.escape(''.join(markers)) + '].*', '', i) for i in str]
    return '\n'.join(str)
