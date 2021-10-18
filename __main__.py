import os
from watcher import Watcher

if __name__ == '__main__':
    typesPath = os.getcwd()
    w = Watcher()
    w.run()