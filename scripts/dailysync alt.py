#!/usr/bin/python3

from multiprocessing import Pool
import multiprocessing
import subprocess
import os


"""Short description for CLI
"""


def main():
  # 1 - Set SRC
  src = os.path.join(os.path.expanduser("~"), "data", "prod")
  dest = os.path.join(os.path.expanduser("~"), "data", "prod_backup")
  # Create a pool of specific number of CPUs
  pool = Pool(multiprocessing.cpu_count())
  # Start each task within the pool
  pool.apply(subprocess.call, args=(["rsync", "-arq", src, dest],))
 
if __name__ == "__main__":
  main()