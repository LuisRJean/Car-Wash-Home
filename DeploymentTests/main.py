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

from datetime import datetime
from datetime import timedelta