try:
    import pymysql.cursors
    import pandas as pd
    from abc import (
        ABC
    )
    import sqlalchemy

except (ModuleNotFoundError, ImportError, ImportWarning):
    raise Exception('Não há como importar esses módulos')


from __con__.__sqlalchemy__.connectionBD import CONNECTION
from __con__.__pymysql__.PymysqlBD import __Connection__

from __cons__.__pymysql__.Cons import __Consult__
from __cons__.__sqlalchemy__.__ConsSqlalchemy import CONSULT

from delete.__delete__ import __Delete__
from __atualizacao__.actualize import __Update__
from insert__.__insercao__ import __Insert__



from main import __GRUD__


class __Main__(__GRUD__):
    pass


if __name__ == '__main__':
    __Main__().__BD__
