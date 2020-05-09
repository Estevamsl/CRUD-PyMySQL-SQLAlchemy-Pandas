import pymysql.cursors
from abc import (
    ABC
)

from __con__.__pymysql__.PymysqlBD import __Connection__
# from __cons__.__pymysql__.Cons import __Consult__


class __Insert__(ABC):
    produto = 'refri'
    valor = 5.55
    @staticmethod
    def __inst__(produto: str, valor: int) -> any:
        try:
            with __Connection__().__cnn__.cursor() as cursor:
                try:
                    cursor.execute(
                        f"INSERT INTO mercado (produto, valor)VALUES ('{produto}', {valor})")
                    __Connection__().__cnn__.commit()
                except:
                    print('Houve um erro inesperado')
        except Exception as e:
            print('Não foi possível inserir dados ao BD', e)
