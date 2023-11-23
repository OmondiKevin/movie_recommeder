"""
This main module runs the whole program and is the entry point for the whole program
"""
import json
import logging
from datetime import datetime

from tabulate import tabulate

import recommendation_engine
import tasks

DATA_SOURCE = 'data_source/'
OUTPUT_DIR = 'output/'
LOGS = 'logs/'
CLEAN_DATA = 'clean_data/'

logging.basicConfig(filename=f'{LOGS}code_labs_logging.log', level=logging.INFO)


def compiler() -> None:
    """The call below reads csv file and saves the output as a json in {OUTPUT_DIR}"""
    tasks.save_json_data(f'{OUTPUT_DIR}data.json', f'{DATA_SOURCE}data.csv')

    logging.info(f'CSV to JSON conversion was completed successfully at {datetime.now()}')

    """
        The solution below reads a json data and cleans the "Rating" values provided.
        """
    temp_json_file = tasks.read_json_from_file(f'{OUTPUT_DIR}data.json')

    """The solution below cleans the "Rating" values by converting the numbers to integers where possible and saves 
    it to the output directory"""
    cleaned_data_list = [tasks.clean_rating(entry) for entry in temp_json_file]
    with open(f'{CLEAN_DATA}cleaned_data.json', 'w') as output_file:
        json.dump(cleaned_data_list, output_file, indent=2)

    logging.info(f'JSON file data cleaning was completed successfully at {datetime.now()}')


if __name__ == '__main__':
    """
    This section runs the recommender engine to predict movies based on ratings
    """
    print("Welcome to Movie Recommender Application. Use the choices below to get what fits you best\n\n1. You will "
          "need to key in your name to see get personalized recommendations.\n2. Press 0 to Exit the "
          "Application\n\n.")

    username = str(input('What is your First Name? ')).replace(" ", "")
    movies_recommended = int(input('\nHow many movies to you want to list? '))

    top_user_recommendations_with_names = recommendation_engine.recommend_movies_with_names("username",
                                                                                            top_n=movies_recommended)
    print('\n\nBelow are your recommendations in a Table, Enjoy:\n',
          tabulate(top_user_recommendations_with_names, headers='keys', tablefmt='fancy_grid'))
