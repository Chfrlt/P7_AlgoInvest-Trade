import time
import src.reader.csv_reader as csv_reader
import sys


from src.algorithms.recursive import Recursive
from src.algorithms.brute_force import BruteForceAlgorithm
from src.algorithms.greedy import GreedyAlgorithm
from src.algorithms.optimised import OptimisedAlgorithm

BUDGET = 500
MAX_NBR_STOCKS_TO_BUY = 20

def truncate_result_file() -> None:
    '''
    Delete the content in .\results\results.txt
    '''
    with open(r"results\results.txt", 'r+') as f:
        f.seek(0)
        f.truncate()
        f.close()

def write_result_file(string: str)  -> None:
    '''
    Write string into .\results\results.txt
    '''
    with open(r"results\results.txt", 'a') as f:
        f.write(f"{string}\n")
        f.close()

def main():
    truncate_result_file()
    for dataset in sys.argv[1:]:
        write_result_file(dataset)
        path = f"datasets_csv\{dataset}.csv"
        stocks = csv_reader.get_datas(path)
    
        if len(stocks) <= 20:
            # BruteForce:
            start_time = time.time()
            r = BruteForceAlgorithm(stocks, BUDGET, MAX_NBR_STOCKS_TO_BUY)
            r.resolve()
            time_spend = f"Execution time: {(time.time() - start_time)}s"
            result = f"Brute force:\n{r}\n{time_spend}"
            print(result)
            write_result_file(result)

            # Recursive:
            start_time = time.time()
            r = Recursive(stocks, BUDGET, MAX_NBR_STOCKS_TO_BUY)
            r.resolve()
            time_spend = f"Execution time: {(time.time() - start_time)}s"
            result = f"Recursive method:\n{r}\n{time_spend}"
            print(result)
            write_result_file(result)

        # Greedy:
        start_time = time.time()
        r = GreedyAlgorithm(stocks, BUDGET, MAX_NBR_STOCKS_TO_BUY)
        r.resolve()
        time_spend = f"Execution time: {(time.time() - start_time)}s"
        result = f"Greedy:\n{r}\n{time_spend}"
        print(result)
        write_result_file(result)

        # Optimised:
        start_time = time.time()
        r = OptimisedAlgorithm(stocks, BUDGET, MAX_NBR_STOCKS_TO_BUY)
        r.resolve()
        time_spend = f"Execution time: {(time.time() - start_time)}s"
        result = f"Optimised:\n{r}\n{time_spend}\n"
        print(result)
        write_result_file(result)

if __name__ == "__main__":
    main()
