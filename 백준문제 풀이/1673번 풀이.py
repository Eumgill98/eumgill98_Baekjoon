while True:
    try:
        n, k = map(int, input().split())
        chicken = n + (n // k)
        while n >= k:
            n = (n // k) + (n % k)
            chicken += n // k
        print(chicken)
    except EOFError:
        break


