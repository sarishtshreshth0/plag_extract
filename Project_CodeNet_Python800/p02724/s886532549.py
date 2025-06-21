def change(X, coin):
    """ exchange
    :param X: total money
    :param coin: 500 or 5
    :return: reduced X and num of coins
    """
    num = X // coin
    X -= coin * num
    return X, num

if __name__ == '__main__':
    X = int(input())
    ans = 0
    X, num = change(X, 500)
    ans += 1000 * num
    X, num = change(X, 5)
    ans += 5 * num
    print(ans)
