from typing import Mapping
from csv_operator import CSV_Operator

if __name__ == '__main__':
    op = CSV_Operator(top='history')
    op.add('test.csv', content=[1, 'ihoahg', 'gaeroihyhhiouhrea'])
    op.create('test_new.csv', headers=['date', 'target'], exist_ok=True, verbose=1)