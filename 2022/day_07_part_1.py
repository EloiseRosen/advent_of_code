from collections import defaultdict
lst = [line for line in open('input.txt').read().split('\n')]

curr_path = []
direct_size_by_dir = defaultdict(lambda: 0)  # dir (full path to it): size of files directly underneath it
total_size_by_dir = defaultdict(lambda: 0)  # dir (full path to it): size of ALL files underneath it, including nested
child_dirs_by_dir = defaultdict(lambda: [])  # dir (full path to it): [list of full paths of all its child directories]

idx = 0
while idx < len(lst):
    line = lst[idx]

    if line.startswith('$ cd '):
        cd_loc = line[len('$ cd '):]
        if cd_loc == '..':
            curr_path.pop()
        else:
            curr_path.append(cd_loc)
            idx += 1  # we don't need the ls line
    elif line.startswith('dir '):
        ls_dir = line[len('dir '):]
        curr_loc_str = '/'.join(curr_path)
        child_dirs_by_dir[curr_loc_str].append(curr_loc_str+'/'+ls_dir)
        direct_size_by_dir[curr_loc_str+'/'+ls_dir] += 0  # make sure present in direct_size_by_dir
    else:  # file
        file_size, _ = line.split(' ')
        direct_size_by_dir['/'.join(curr_path)] += int(file_size)

    idx += 1


def recursive(dir_path):
    if dir_path in total_size_by_dir:  # entries in total_size_by_dir are final answer for that path, don't need to calculate again
        return total_size_by_dir[dir_path]
    total_size = direct_size_by_dir[dir_path]
    if dir_path in child_dirs_by_dir:
        for child_dir_path in child_dirs_by_dir[dir_path]:
            total_size += recursive(child_dir_path)
    total_size_by_dir[dir_path] = total_size
    return total_size

ans = 0
for dir_path in direct_size_by_dir.keys():
    total_size = recursive(dir_path)
    if total_size <= 100000:
        ans += total_size
print(ans)
