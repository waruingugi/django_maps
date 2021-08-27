import csv
import os
from pathlib import Path
from ast import literal_eval


def load_csv_coordinates():
    BASE_DIR = Path(__file__).resolve().parent.parent
    data_file_path = os.path.join(BASE_DIR, 'data/coordinates.csv')

    data_file = open(data_file_path, 'r')
    data_csv_reader = csv.reader(data_file, delimiter=',')

    response = {}

    for row in data_csv_reader:
        plot_number = row[0]
        plot_coordinates = literal_eval(row[1])

        response[plot_number] = plot_coordinates

    data_file.close()

    return response
