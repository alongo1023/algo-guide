'''Find the hamming weight of a binary number (i.e number of 1s)'''

def hammingWeight(n):
    '''
    :param n: int
    :return: int
    number of 1's in binary representation of n
    '''
    mask = 1
    bits = 0
    #32 bits in number
    for i in range(0, 32):
        if((n & mask) != 0):
            bits = bits +1
        mask = mask << 1#shift mask to the left

    return bits

def main():
    assert(hammingWeight(3) == 2)

    assert(hammingWeight(10) == 2)

    assert(hammingWeight(27) == 4)

    assert(hammingWeight(11) == 3)





main()