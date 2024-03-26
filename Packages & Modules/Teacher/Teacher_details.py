import os, sys
from os.path import dirname, join, abspath
abc = abspath(join(dirname(__file__),'..'))
sys.path.insert(0, abc)

from Student import Student_details

def teacher():
    print(f'Hi, I am Jose Mourhino : The teacher !!!')


#calling function of student script in teacher script.
Student_details.student()


