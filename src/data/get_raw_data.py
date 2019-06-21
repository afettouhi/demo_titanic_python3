# -*- coding: utf-8 -*-
import os
from dotenv import find_dotenv, load_dotenv
from requests import session
import logging

                
def main(project_dir):
    '''
    main method
    '''
    # get logger
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')

    # extract data
    os.system('kaggle competitions download -c titanic -f test.csv -p ../data/raw')
    os.system('kaggle competitions download -c titanic -f train.csv -p ../data/raw')
    logger.info('downloaded raw training and test data')

if __name__ == '__main__':
    # getting root directory
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    
    # setup logger
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # find .env automatically by walking up directories until it's found
    dotenv_path = find_dotenv()
    # load up the entries as environment variables
    load_dotenv(dotenv_path)

    # call the main
    main(project_dir)
