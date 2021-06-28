#!/usr/bin/python3

import os
import subprocess
from multiprocessing import Pool
import multiprocessing


"""Short description for CLI
"""

def run(folder):
  # Do something with task here
    print("Handling rsync in: {}".format(folder))
    dest = os.path.join(os.path.expanduser("~"), "data", "prod_backup")
    subprocess.call(["rsync", "-arq", folder, dest])


def main():
  # 1 - Set SRC
  src = os.path.join(os.path.expanduser("~"), "data", "prod")
  print(src)
  folders = []
  for root, _dir, files in os.walk(src):
    for name in _dir:
      folders.append(os.path.join(root, name))
  if len(folders)>0:
    # Create a pool of specific number of CPUs
    p = Pool(multiprocessing.cpu_count())
    # Start each task within the pool
    p.map(run, folders)
  else:
      print("Empty {}".format(folders))
 
if __name__ == "__main__":
  main()