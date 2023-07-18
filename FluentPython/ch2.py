from random import random
from array import array
import unicodedata
import re


if __name__ == "__main__":
    re_digit = re.compile(r'\d')

    sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

    for char in sample:
        print(f'U+{ord(char):04x}',
              char.center(6),
              're_dg' if re_digit.match(char) else '_',
              'isdig' if char.isdigit() else '_',
              'isnum' if char.isnumeric() else '_',
              f'{unicodedata.numeric(char):5.2f}',
              unicodedata.name(char),
              sep='\t'
              )

    # values = (random() for i in range(10**7))
    # for count, value in enumerate(values):
    #     print('count is ' + str(count) + ' value is ' + str(value))
    # octests = array('B', range(6))
    # m1 = memoryview(octests)
    #
    # print(m1.tolist())
    #
    # m2 = m1.cast('B', [2, 3])
    # print(m2.tolist())
    #
    # m3 = m1.cast('B', [3, 2])
    # print(m3.tolist())

    # a = (random() for i in range(10**7))
    #
    # print(len(a))ccx x
    # # for i in a:
    # #     print(i)


    # symbols = '$¢£¥€¤'
    # codes = [ord(s) for s in symbols]
    # print(codes)
    #
    # x = 'ABC'
    #
    # codes = [ord(c) for c in x]
    # print('codes is ' + str(codes))
    #
    # print("x is " + x)
    #
    # items = range(100)
    #
    # data = [item for item in items if item % 2 == 0]
    # print(data)
    #
    # colors = ('black', 'white')
    # sizes = ('S', 'M', 'L')
    # tshirts = [(color, size) for color in colors for size in sizes]
    #
    # print(tshirts)
    #
    # for tshirt in ((c, s) for c in colors for s in sizes):
    #     print(str(tshirt))
