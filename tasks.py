"""
This module handles all functions that will be used in the rest of the program
"""

import csv
import json
import re
from typing import List, Any


def csv_file_to_json(file_path: str) -> List[str]:
    """
    :param file_path: This is the data source in csv
    :return: the output of this function is a json data
    """
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    return data


def read_json_from_file(file_path: str) -> List[Any]:
    """
    :param file_path: json file loaded from a directory
    :return: json data that can be used to perform tasks
    """
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    return json_data


def save_json_data(output: str, data_source: str) -> None:
    """
    :param output: this is the directory where the output data is saved
    :param data_source: this is the directory where the input data is saved
    :return: None
    """
    with open(output, 'w') as json_file:
        json.dump(csv_file_to_json(data_source), json_file, indent=2)


def convert_rating_to_int(rating):
    numeric_part = re.search(r'\d+', rating)
    return int(numeric_part.group()) if numeric_part else None


def clean_rating(entry):
    entry["Rating"] = convert_rating_to_int(entry["Rating"])
    return entry
