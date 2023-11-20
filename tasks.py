"""
This module handles all functions that will be used in the rest of the program
"""

import csv
import json
from typing import List


def csv_file_to_json(file_path: str) -> List[str]:
    """
    :param file_path: This is the data source in csv
    :return: the output of this function is a json data
    """
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    return data


def save_json_data(output: str, data_source: str) -> None:
    """
    :rtype: object
    :param output: this is the directory where the output data is saved
    :param data_source: this is the directory where the input data is saved
    :return: None
    """
    with open(output, 'w') as json_file:
        json.dump(csv_file_to_json(data_source), json_file, indent=2)


def data_cleaner(json_data: List[str]) -> List[str]:
    """
    :param json_data: input file in json
    :return: cleaned data in json
    """
    filtered_records = []
    for record in json_data:
        try:
            filtered_records.append(int(record["Rating"]))
        except ValueError:
            pass
    return filtered_records
