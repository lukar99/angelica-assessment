def computePolkadotScore():
    """Compute and return the Polkadot score."""
    lips = '~~~~~~\''
    lips_start = None
    lips_end = None
    polka_dot_count = 0
    with open('angelica.txt', 'r') as file:
        for line in file:
            if lips in line:
                lips_start = line.find(lips)
                lips_end = lips_start + len(lips) - 2

            if lips_start is not None and lips_end is not None:
                for i, char in enumerate(line):
                    if char == 'O':
                        if lips_start <= i <= lips_end:
                            polka_dot_count += 2
                        else:
                            polka_dot_count += 1

    return polka_dot_count


print(computePolkadotScore())
