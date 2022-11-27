lst = open('input.txt').read().split('\n')


def get_final_lst_element(original_lst, by_most=True):
    lst = original_lst[:]

    for idx in range(0, len(lst[0])):
        # determine if the number to keep is a 1 or a 0
        balance = 0
        for el in lst:
            if el[idx] == '0':
                balance -= 1
            else:
                balance += 1
        keep = 1 if balance >= 0 else 0
        if not by_most:
            keep ^= 1
        
        # only keep elements that have the correct number in the current idx
        new_lst  = []
        for el in lst:
            if el[idx] == str(keep):
                new_lst.append(el)
        lst = new_lst

        if len(lst) == 1:
            return lst[0]


oxygen_generator = get_final_lst_element(lst, by_most=True)
co2_scrubber = get_final_lst_element(lst, by_most=False)
print(int(oxygen_generator, 2) * int(co2_scrubber, 2))
