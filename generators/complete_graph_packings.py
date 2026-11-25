#!/usr/bin/env python3
"""Packings of connected edge sets in the complete graph K_n.

T(n, k) counts unordered sets of k vertex-disjoint, nonempty, connected edge sets in K_n,
each with at most `cap` edges; unused vertices are allowed and distinct edge sets on the
same support count separately.  Conditioning on the piece containing vertex n gives

    C_n = C_{n-1} + t * sum_{r=2}^{min(n, cap+1)} w_r * binomial(n-1, r-1) * C_{n-r},

where w_r is the number of connected spanning edge sets with at most `cap` edges on r
labelled vertices.  Prints the flattened rows n = 0..max_n, k = 0..floor(n/2).
Source: RealRooted issue #2646 (public).
"""
import argparse
from math import comb

WEIGHTS = {4: (1, 4, 31, 125), 5: (1, 4, 37, 347, 1296)}


def rows(cap, max_n):
    weights = WEIGHTS[cap]
    out = [[1]]
    for n in range(1, max_n + 1):
        row = out[-1] + [0] * (n // 2 + 1 - len(out[-1]))
        for r, weight in enumerate(weights, start=2):
            if r > n:
                break
            ways = weight * comb(n - 1, r - 1)
            for k, count in enumerate(out[n - r]):
                row[k + 1] += ways * count
        out.append(row)
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--cap", type=int, choices=sorted(WEIGHTS), required=True)
    parser.add_argument("--max-n", type=int, default=12)
    args = parser.parse_args()
    print(", ".join(str(x) for row in rows(args.cap, args.max_n) for x in row))


if __name__ == "__main__":
    main()
