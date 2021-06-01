from baseq import base10, baseQ, getHash
from wallet import initWallets, distribution, mixing
from deterministic import mining, trading, check, pairs, number_reduction
from randomized import rand_string

def run():
    """
    Run the main function.
    """
    print('\nSTARTING\n')

    # Parameters
    N = 10
    print('Players: ', N, '\n')
    block_number = 0
    buyin = 1000000 # lovelaces
    tokens = 2
    mining_rate = 1000
    halving = 1000
    miners = len(baseQ(base10(getHash(N)), N))+2
    mining_pool = miners*mining_rate*halving*2
    # unique_string = 'This is a unique string to start the chain.'
    unique_string = rand_string(32)

    # Initialize the wallets
    wallets = initWallets(N, buyin, tokens)
    block_string = str(block_number) + unique_string
    dw = distribution(wallets)
    print(dw)

    # Start Chain
    while True:

        # Create the block hash
        block_hash = getHash(block_string)

        # Mining
        number = base10(block_hash)
        mining_list = baseQ(number, N)
        miner_tokens = baseQ(number, tokens)
        wallets, mining_pool = mining(mining_list, wallets, mining_rate, mining_pool)

        # Trading
        number_hash = getHash(number)
        number = base10(number_hash)
        amount = number_reduction(number)
        transaction_list = baseQ(number, N)
        traders_tokens = baseQ(number, tokens) # Trading is betwen pairs.
        trading_pairs = pairs(transaction_list, mining_list)
        token_pairs = pairs(traders_tokens, miner_tokens)
        if len(trading_pairs) >= len(token_pairs):
            trading_pairs = trading_pairs[:len(token_pairs)]
        else:
            token_pairs = token_pairs[:len(trading_pairs)]
        wallets, flag = trading(trading_pairs, token_pairs, wallets, tokens, amount)

        # Check
        outcome, mining_rate, mining_pool = check(block_number, halving, mining_rate, mining_pool, flag)
        if outcome is False:
            print('\nEND at block number: ', block_number, '\n')
            dw = distribution(wallets)
            print(dw)
            print("\nWinner: ", dw.index(max(dw)))
            break
        wallets = mixing(wallets, N) # mix the wallets up

        # Increment block number
        block_number += 1
        block_string = str(block_number) + block_hash


if "__main__" == __name__:
    run()