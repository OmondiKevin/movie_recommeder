"""
This main module runs the whole program and is the entry point for the whole program
"""
import json
import logging
from datetime import datetime

import tasks

DATA_SOURCE = 'data_source/'
OUTPUT_DIR = 'output/'
LOGS = 'logs/'
CLEAN_DATA = 'clean_data'

if __name__ == '__main__':
    tasks.save_json_data(f'{OUTPUT_DIR}data.json', f'{DATA_SOURCE}data.csv')

    tasks.data_cleaner(f'{OUTPUT_DIR}data.json')

    logging.basicConfig(filename=f'{LOGS}code_labs_logging.log', level=logging.INFO)
    logging.info(f'This operation was completed successfully at {datetime.now()}')
