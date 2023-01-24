#!/usr/bin/python3

""" 5. LFU Caching
"""

from enum import Enum
from heapq import heappush, heappop
from itertools import count

BaseCaching = __import__("base_caching").BaseCaching

class HeapItemStatus(Enum):
