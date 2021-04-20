'''Find the sum of two numbers without using the addition operator'''
def sum(a, b):
    while b != 0:
        #the carry of each addition step is also found from the AND operator
        #i.e. 1&0=0, 0&1=0, 0&0=0, 1&1=1 carry
        carry = a & b

        #Using XOR operator you can figure out what the last digit of the sum will be without the carry
        #ex 1^0=1, 1^1=0, 0^0=0, 0^1=1
        a = a ^ b

        #shift b over and do it again until no carry is left
        b = carry << 1
    return a

def main():
    assert(sum(3, 4) == 7)
    assert(sum(396, 4) == 400)
    assert(sum(0, 481) == 481)
    assert(sum(6, 0) == 6)
    assert(sum(12, 400000) == 400012)

main()