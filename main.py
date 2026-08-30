from math import gcd

q = int(input())

for _ in range(q):

    n = int(input())

    tree = [[] for _ in range(n + 1)]

    # Read n-1 edges
    for i in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    # Read number of guesses and required score
    g, k = map(int, input().split())

    guesses = set()

    # Read guesses
    for i in range(g):
        u, v = map(int, input().split())
        guesses.add((u, v))

    # Root the tree at node 1
    parent = [0] * (n + 1)
    order = [1]
    parent[1] = -1

    correct = 0

    # Build parent array
    index = 0

    while index < len(order):
        u = order[index]
        index += 1

        for v in tree[u]:

            if v == parent[u]:
                continue

            parent[v] = u
            order.append(v)

            # Check if u -> v is a correct guess
            if (u, v) in guesses:
                correct += 1

    # Score for each possible root
    score = [0] * (n + 1)
    score[1] = correct

    # Reroot the tree
    for u in order:

        for v in tree[u]:

            if parent[v] != u:
                continue

            score[v] = score[u]

            # u -> v becomes incorrect
            if (u, v) in guesses:
                score[v] -= 1

            # v -> u becomes correct
            if (v, u) in guesses:
                score[v] += 1

    # Count winning roots
    winning_roots = 0

    for root in range(1, n + 1):
        if score[root] >= k:
            winning_roots += 1

    # Probability
    numerator = winning_roots
    denominator = n

    # Reduce fraction
    common = gcd(numerator, denominator)

    numerator //= common
    denominator //= common

    print(str(numerator) + "/" + str(denominator))