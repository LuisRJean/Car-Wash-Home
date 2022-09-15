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

from datetime import datetime
from datetime import timedelta