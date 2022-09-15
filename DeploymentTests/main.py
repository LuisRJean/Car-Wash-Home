import imp
import os
import sys
import time
import json
import logging
import argparse
import subprocess
import threading

def get_config():
    """Get config from config.json"""
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

def get_logger():
    """Get logger"""
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

def get_args():
    """Get args"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', help='Test to run', required=True)
    parser.add_argument('-c', '--config', help='Config file', required=False)
    parser.add_argument('-l', '--log', help='Log file', required=False)
    args = parser.parse_args()
    return args

def run_test(test, config, logger):
    """Run test"""
    logger.info('Running test: %s', test)
    test = imp.load_source('test', test)
    test.run(config, logger)

def main():
    """Main"""
    args = get_args()
    config = get_config()
    logger = get_logger()
    run_test(args.test, config, logger)

if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter


from datetime import datetime
from datetime import timedelta