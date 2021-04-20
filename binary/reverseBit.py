def reverse(num):
    '''
    :param num: an integer
    :return: the reversed binary representation of the given num, i.e. given 4 (100) return 1 (001)
    '''
    power = 31
    result = 0
    while num:
        result += (num % 2) << power
        power -= 1
        num >>= 1
    return result

def main():
    assert(reverse(4) == 536870912)#100 -> 100000000000000000000000000000
    assert(reverse(10) == 1342177280)
    assert(reverse(41) == 2483027968)

main()
