import pymysql.cursors
import pandas as pd
from abc import (
    ABC
)
import sqlalchemy

try:

    from __con__.__sqlalchemy__.connectionBD import CONNECTION
    from __con__.__pymysql__.PymysqlBD import __Connection__

    from __cons__.__pymysql__.Cons import __Consult__
    from __cons__.__sqlalchemy__.__ConsSqlalchemy import CONSULT

    from delete.__delete__ import __Delete__
    from __atualizacao__.actualize import __Update__
    from insert__.__insercao__ import __Insert__

except (ModuleNotFoundError, ImportError, ImportWarning):
    raise Exception('Não há como importar esses módulos')


class __GRUD__(ABC):
    @property
    def __BD__(self):
        while True:
            print('[1] Consultar:')
            print('[2] Insert:')
            print('[3] Update:')
            print('[4] Dell:')
            print('[5] Sair:')

            try:
                __op__ = int(input('Digite a sua opção: '))
            except ValueError:
                print("Houve um erro de tipo, tente novamente")

            if (__op__ > 5 or __op__ < 1):
                print('Tente uma opção dentre as quais estão disponíveis')
            else:
                if (__op__ == 1):
                    print('\n')
                    # __Consult__().__cnst__
                    CONSULT().__c__
                    print('\n')
                elif (__op__ == 2):
                    __Insert__().__inst__('pepsi', 1.90)
                elif (__op__ == 3):
                    __Update__().__updat__(2.20, 3, 1)
                elif (__op__ == 4):
                    __Delete__().__dell__(1)
                elif (__op__ == 5):
                    break


class __Main__(__GRUD__):
    pass


if __name__ == '__main__':
    __Main__().__BD__
