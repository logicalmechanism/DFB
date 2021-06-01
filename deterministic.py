from amm import calculate_amount

def pairs(x, y):
    """
    """
    z = zip(x,y)
    return [(i,j) for i,j in z if i != j]


def mining(mining_list, wallets, mining_rate, mining_pool):
    """
    """
    for m in mining_list:
        if mining_pool <= 0:
            mining_pool = 0
            break
        wallets[m][1] += mining_rate
        mining_pool -= mining_rate
    return wallets, mining_pool


def reserves(wallets, tokens):
    """
    """
    reserve = {}
    for t in range(tokens):
        reserve[t] = 0
    for user in wallets:
        for token in wallets[user]:
            reserve[token] += wallets[user][token]
    return reserve


def trading(trading_pairs, token_pairs, wallets, tokens, amount):
    """
    """
    flag = False
    for trade, token in zip(trading_pairs, token_pairs):
        A = wallets[trade[0]][token[0]]
        B = wallets[trade[1]][token[1]]
        reserve = reserves(wallets, tokens)
        deltaB = calculate_amount(reserve[0], reserve[1], amount, 1)
        deltaB = int(deltaB)+1
        if (A-amount > 0) and (B - deltaB > 0) and (deltaB > 0):
            flag = True
            wallets[trade[0]][token[0]] = A - amount
            wallets[trade[0]][token[1]] += deltaB
            wallets[trade[1]][token[1]] = B - deltaB
            wallets[trade[1]][token[0]] += amount
    return wallets, flag


def number_reduction(n):
    """
    """
    counter = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1
            # divide out highest prime power
            for p in [2, 3, 5, 9, 11, 13, 17, 19]:
                while n % p == 0:
                    n = n // p
        counter += 1
    return counter


def check(block_number, halving, mining_rate, mining_pool, flag):
    """
    """
    if block_number % halving == 0 and block_number != 0:
        if mining_rate > 1:
            mining_rate = mining_rate / 2
        return True, mining_rate, mining_pool
    if mining_pool <= 0:
        print("\nMining Pool is Empty")
        return False, mining_rate, mining_pool
    if flag is False:
        print("\nNo Trading is Allowed")
        return False, mining_rate, mining_pool
    return True, mining_rate, mining_pool


if "__main__" == __name__:
    pass