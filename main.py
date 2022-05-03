import time
import src.reader.csv_reader as csv_reader
import sys


from src.algorithms.recursive import Recursive
from src.algorithms.brute_force import BruteForceAlgorithm
from src.algorithms.greedy import GreedyAlgorithm
from src.algorithms.optimised import OptimisedAlgorithm

BUDGET = 500
MAX_NBR_STOCKS_TO_BUY = 20

def main():
    paths = []
    for dataset in sys.argv[1:]:
        paths.append(f"datasets_csv\{dataset}.csv")
    for path in paths:
        stocks = csv_reader.get_datas(path)

        if len(stocks) <= 20:
            # BruteForce:
            start_time = time.time()
            r = BruteForceAlgorithm(stocks, BUDGET, MAX_NBR_STOCKS_TO_BUY)
            r.resolve()
            print(f"\nBrute force:\n{r}")
            print(f"Execution time: {(time.time() - start_time)}s")

            # Recursive:
            start_time = time.time()
            r = Recursive(stocks, BUDGET, MAX_NBR_STOCKS_TO_BUY)
            r.resolve()
            print(f"\nRecursive method:\n{r}")
            print(f"Execution time: {(time.time() - start_time)}s")

        # Greedy:
        start_time = time.time()
        r = GreedyAlgorithm(stocks, BUDGET, MAX_NBR_STOCKS_TO_BUY)
        r.resolve()
        print(f"\nGreedy:\n{r}")
        print(f"Execution time: {(time.time() - start_time)}s")

        # Optimised:
        start_time = time.time()
        r = OptimisedAlgorithm(stocks, BUDGET, MAX_NBR_STOCKS_TO_BUY)
        r.resolve()
        print(f"\nOptimised:\n{r}")
        print(f"Execution time: {(time.time() - start_time)}s")


if __name__ == "__main__":
    main()
