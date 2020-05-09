import pymysql.cursors
import pandas as pd
from abc import (
    ABC
)
import sqlalchemy

from __con__.__sqlalchemy__.connectionBD import CONNECTION
from __con__.__pymysql__.PymysqlBD import __Connection__

from __cons__.__pymysql__.Cons import __Consult__
from __cons__.__sqlalchemy__.__ConsSqlalchemy import CONSULT


class __Delete__(ABC):
    @staticmethod
    def __dell__(id: int) -> any:
        try:
            with __Connection__().__cnn__.cursor() as cursor:
                try:
                    cursor.execute(
                        f'DELETE FROM mercado WHERE id = {id}')
                    __Connection__().__cnn__.commit()
                except:
                    print("Houve um erro inesperado")
        except:
            print("Houve um erro ao deletar dados do BD")
        else:
            print("Deleteção realizada com sucesso")
