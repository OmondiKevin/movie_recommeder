"""
This main module runs the whole program and is the entry point for the whole program
"""
import json
import logging
import re
from datetime import datetime

import tasks

DATA_SOURCE = 'data_source/'
OUTPUT_DIR = 'output/'
LOGS = 'logs/'
CLEAN_DATA = 'clean_data'


def compiler() -> None:
    """The call below reads csv file and saves the output as a json in {OUTPUT_DIR}"""
    tasks.save_json_data(f'{OUTPUT_DIR}data.json', f'{DATA_SOURCE}data.csv')

    logging.basicConfig(filename=f'{LOGS}code_labs_logging.log', level=logging.INFO)
    logging.info(f'This operation was completed successfully at {datetime.now()}')


if __name__ == '__main__':
    """
    The solution below reads a json data and cleans the "Rating" values provided.
    """
    temp_json_file = tasks.read_json_from_file(f'{OUTPUT_DIR}data.json')
    print(temp_json_file)

    tasks.clean_rating(temp_json_file)

    cleaned_data_list = [tasks.clean_rating(temp_json_file) for entry in temp_json_file]

    print (cleaned_data_list)

    # cleaned_data_list = [tasks.clean_rating(temp_json_file) for te]
