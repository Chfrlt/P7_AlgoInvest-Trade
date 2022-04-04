import time
import src.reader.csv_reader as csv_reader


from src.algorithms.recursive import Recursive
from src.algorithms.brute_force import BruteForceAlgorithm
from src.algorithms.greedy import GreedyAlgorithm
from src.algorithms.optimised import OptimisedAlgorithm

BUDGET = 500
MAX_NBR_STOCKS_TO_BUY = 20
CSV_PATHS = (r"datasets_csv\dataset0.csv", r"datasets_csv\dataset1.csv",
             r"datasets_csv\dataset2.csv")

def choose_dataset():
    dataset_ref = input("[1] Dataset_test\n[2] Dataset_1\n[3] Dataset_2\n>> ")
    if dataset_ref == str(1):
        path = CSV_PATHS[0]
    if dataset_ref == str(2):
        path = CSV_PATHS[1]
    if dataset_ref == str(3):
        path = CSV_PATHS[2]
    try:
        return path
    except UnboundLocalError:
        exit("Invalid input. Pls rerun the script.")


def main():
    path = choose_dataset()
    stocks = csv_reader.get_datas(path)

    if len(stocks) == 20:
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
