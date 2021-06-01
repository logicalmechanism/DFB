from baseq import getHash, base10, baseQ

def initWallets(N, buyin, tokens):
    """
    """
    wallets = {}
    for i in range(N):
        wallets[i] = {}
        for t in range(tokens):
            if t == 0:
                wallets[i][t] = buyin
            else:
                wallets[i][t] = 0
    return wallets


def mixing(wallets, N):
    """
    """
    mix = baseQ(base10(getHash(wallets)), N)[:N]
    play = [i for i in range(N)]
    for x,y in zip(play, mix):
        old = wallets[x]
        wallets[x] = wallets[y]
        wallets[y] = old
    return wallets


def distribution(wallets):
    """
    """
    total = []
    for user in wallets:
        total.append(wallets[user][0])
    return total


if "__main__" == __name__:
    wallets = {0: {0: 784, 1: 34166784.5}, 1: {0: 5229008, 1: 29181822.0}, 2: {0: 179677, 1: 30994907.0}, 3: {0: 235292, 1: 31459332.0}, 4: {0: 789509, 1: 32089218.25}, 5: {0: 741395, 1: 27345680.25}, 6: {0: 880991, 1: 27632916.75}, 7: {0: 220713, 1: 33116516.375}, 8: {0: 735496, 1: 29486552.5}, 9: {0: 987135, 1: 30526270.375}}
    print(wallets)
    mix = baseQ(base10(getHash(wallets)), 10)[:10]
    play = [i for i in range(10)]
    for x,y in zip(play, mix):
        wallets[x] = wallets[y]
    print(wallets)
    # w = mixing(wallets, 10, 2)