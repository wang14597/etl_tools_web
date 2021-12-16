import os
import sys

getcwd_ = os.getcwd()
listdir = os.listdir(getcwd_)
for i in listdir:
    sys.path.append(os.path.join(getcwd_, i))

