from typing import Iterable, List, NoReturn, Optional, Tuple, Union
import os
import sys
import re

class CSV_Operator:
    def __init__(self, top: str='.') -> NoReturn:
        self.top = top[:-1] if top[-1] == '/' else  top
        if not self.top == '.':
            if os.path.exists(self.top) and os.path.isdir(self.top):
                pass
            else:
                os.makedirs(self.top, exist_ok=False)

    def _load(self, filename: str, mode: str='r') -> list:
        with open(f'{self.top}/{filename}', mode=mode) as f:
            contents = f.readlines()

        return contents

    def create(self, filename: str, headers: Optional[List[str]]=None, exist_ok: bool=False,
                verbose: int=0) -> NoReturn:
        if os.path.exists(f'{self.top}/{filename}'):
            if exist_ok:
                if verbose <= 0:
                    sys.stdout.write(f'Warnig: The file {self.top}/{filename} already exists.\n')
            else:
                raise ValueError(f'The file {self.top}/{filename} already exists.')
        else:
            with open(f'{self.top}/{filename}', 'w') as f:
                if headers is not None:
                    f.write(','.join(headers)+'\n')

    def add(self, filename: str, content: Union[str, List[str], Tuple[str]]) -> NoReturn:
        if isinstance(content, (list, tuple)):
            content = [str(c) for c in content]
            content = ','.join(content)
        if not content[-2:] == '\n':
            content += '\n'

        with open(f'{self.top}/{filename}', mode='a') as f:
            f.write(content)
