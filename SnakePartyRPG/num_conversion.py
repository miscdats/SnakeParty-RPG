def bin_to_dec(bnum):
    new_num = []

    for j in range(len(bnum)):
        z = int(bnum[j]) * (8 ** (len(bnum) - (j + 1)))
        new_num.append(z)

    total = sum(new_num)
    return total


def dec_to_bin(dnum):
    new_num = []

    if dnum > 1:
        num = dec_to_bin(dnum // 2)
        num = num % 2
        new_num.append(num)

    total = sum(new_num)
    return total


