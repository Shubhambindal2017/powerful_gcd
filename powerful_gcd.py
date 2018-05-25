def gcd( x, y ):
    """Computes greatest common divisor of two values"""
    
    while y:
        z = x
        x = y
        y = z % y
    return x
    
list_=map(int ,raw_input("ENTER TWO NUMBERS:\t").split())
print "YOUR GCD IS \t %d" % gcd(list_[0],list_[1])
