import csv
from models.stock import Stock


def get_datas(path) -> list:
    '''
    From path, open csv file.
    Return a list of stock object.
    '''

    def string_into_float_converter(n):
        '''
        Convert a string into float if possible.
        '''
        try:
            n = float(n)
        except ValueError:
            pass
        return n

    def convert_data(datas) -> list:
        '''
        From dict, transform into a list of Stock object.
        Return the list.
        '''
        names = datas['name']
        price = datas['price']
        percent = datas['profit']
        return [Stock(*args) for args in zip(names, price, percent)]

    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        datas = {}
        for row in reader:
            for header, value in row.items():
                value = string_into_float_converter(value)
                if header in datas:
                    datas[header].append(value)
                else:
                    datas[header] = [value]
    converted_datas = convert_data(datas)
    return converted_datas
