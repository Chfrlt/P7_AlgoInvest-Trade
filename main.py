import time
import sys
import os
import logging

import src.reader.csv_reader as csv_reader
from src.algorithms.recursive import Recursive
from src.algorithms.brute_force import BruteForceAlgorithm
from src.algorithms.greedy import GreedyAlgorithm
from src.algorithms.optimised import OptimisedAlgorithm

BUDGET = 500
MAX_NBR_STOCKS_TO_BUY = 20

def create_log_file():
    try:
        os.makedirs(r'results', exist_ok= True)
        if not os.path.isfile('results\\results_log.txt'):
            open('results\\results_log.txt', "w")
    except FileExistsError:
        pass

def clear_result_logs() -> None:
    '''
    Delete the content in .\\results\\results_log.txt
    '''
    try:
        with open(r"results\\results_log.txt", 'r+') as f:
            f.seek(0)
            f.truncate()
            f.close()
    except FileNotFoundError:
        exit()


def argv_handler() -> list:
    for arg in sys.argv[1:]:
        if arg == 'clear_log':
            clear_result_logs()
        paths = []
        file = f"datasets_csv\\{arg}.csv"
        if os.path.isfile(file):
            paths.append((file, arg))
    return paths if paths else exit()


def main():
    create_log_file()
    logging.basicConfig(filename=r"results\\results_log.txt", level=logging.INFO)
    for file, name in [i for i in argv_handler()]:
        stocks = csv_reader.get_datas(file)
        logging.info(f"Started process with {name}\n")

        if len(stocks) <= 20:
            # BruteForce:
            start_time = time.time()
            r = BruteForceAlgorithm(stocks, BUDGET, MAX_NBR_STOCKS_TO_BUY)
            r.resolve()
            time_spend = f"Execution time: {(time.time() - start_time)}s"
            result = f"Brute force:\n{r}\n{time_spend}"
            print(result)
            logging.info(result)

            # Recursive:
            start_time = time.time()
            r = Recursive(stocks, BUDGET, MAX_NBR_STOCKS_TO_BUY)
            r.resolve()
            time_spend = f"Execution time: {(time.time() - start_time)}s"
            result = f"Recursive method:\n{r}\n{time_spend}"
            print(result)
            logging.info(result)

        # Greedy:
        start_time = time.time()
        r = GreedyAlgorithm(stocks, BUDGET, MAX_NBR_STOCKS_TO_BUY)
        r.resolve()
        time_spend = f"Execution time: {(time.time() - start_time)}s"
        result = f"Greedy:\n{r}\n{time_spend}"
        print(result)
        logging.info(result)

        # Optimised:
        start_time = time.time()
        r = OptimisedAlgorithm(stocks, BUDGET, MAX_NBR_STOCKS_TO_BUY)
        r.resolve()
        time_spend = f"Execution time: {(time.time() - start_time)}s"
        result = f"Optimised:\n{r}\n{time_spend}\n"
        print(result)
        logging.info(result)

        logging.info('Ended process\n')


if __name__ == "__main__":
    main()
