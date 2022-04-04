import csv
from models.stock import Stock


def get_datas(path):

    def string_into_float_converter(n):
        try:
            n = float(n)
        except ValueError:
            pass
        return n

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


def convert_data(datas):
    names = datas['name']
    price = datas['price']
    percent = datas['profit']
    return [Stock(*args) for args in zip(names, price, percent)]
