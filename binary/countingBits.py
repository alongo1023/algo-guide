def count(num):
    '''
    :param num: an int
    :return: array of the number of 1's in the binary representation of every number in range [0, num]
    '''
    result = [0] * (num + 1)
    power = 1
    indexToAdd = 1
    for i in range(1, num + 1):
        #number is power of 2
        if (i == power):
            result[i] = 1
            power <<= 1#set new power
            indexToAdd = 1
        else:
            #Use previous result plus one
            result[i] = result[indexToAdd] + 1
            indexToAdd = indexToAdd + 1
    return result

def main():
    assert(count(7) == [0, 1, 1, 2, 1, 2, 2, 3])
    assert(count(10) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2])
    assert(count(10) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 4, 3, 3, 4, 1])

main()