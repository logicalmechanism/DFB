import hashlib


def base10(obj):
    """
    Converts some hash into base 10.
    """
    target = int(obj, 16)
    return target


def baseQ(n, b):
    """
    Convert base 10 into base b.
    """
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def getHash(ctr):
    """
    Stringify ctr and sha3 512 hash then hexdigest.
    """
    m = hashlib.sha3_512()
    string = str(ctr).encode('utf-8')
    m.update(bytes(string))
    ctr_hash = m.hexdigest()
    return ctr_hash


if "__main__" == __name__:
    string = "Hello, World!"
    h = getHash(string)
    b10 = base10(h)
    b23 = baseQ(b10, 23)
    print(string)
    print(h)
    print(b10)
    print(b23)