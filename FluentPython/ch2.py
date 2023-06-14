
if __name__ == "__main__":
    symbols = '$¢£¥€¤'
    codes = [ord(s) for s in symbols]
    print(codes)

    x = 'ABC'

    codes = [ord(c) for c in x]
    print('codes is ' + str(codes))

    print("x is " + x)

    items = range(100)

    data = [item for item in items if item % 2 == 0]
    print(data)

    colors = ('black', 'white')
    sizes = ('S', 'M', 'L')
    tshirts = [(color, size) for color in colors for size in sizes]
    
    print(tshirts)

    for tshirt in ((c, s) for c in colors for s in sizes):
        print(str(tshirt))
