def get_hash(s):
    curr = 0
    for char in s:
        curr = ((curr + ord(char))*17) % 256
    return curr


ans = 0
steps = open('input.txt').read().replace('\n', '').split(',')
for step in steps:
    ans += get_hash(step)
print(ans)
