def find_base_label(lookup_table, label):
    base_label = label
    while lookup_table[base_label] != base_label:
        base_label = lookup_table[base_label]
    return base_label


def main():
    n, m = map(int, input().split())

    lookup_table = list(range(n))
    for _ in range(m):
        x, y, z = map(int, input().split())

        base_label_1 = find_base_label(lookup_table, x - 1)
        base_label_2 = find_base_label(lookup_table, y - 1)

        if base_label_1 < base_label_2:
            lookup_table[base_label_2] = base_label_1
        elif base_label_2 < base_label_1:
            lookup_table[base_label_1] = base_label_2

    for i in range(n):
        lookup_table[i] = lookup_table[lookup_table[i]]

    print(len(set(lookup_table)))


main()
