<!-- Arquivo main.py -->

import pymysql.cursors
import pandas as pd
from abc import (ABC)
import sqlalchemy
# do (from) Módulo __con__.__sqlalchemy__.connectionBD traz ((importa)(import)) CONNECTION
from __con__.__sqlalchemy__.connectionBD import CONNECTION
from __con__.__pymysql__.PymysqlBD import __Connection__

from __cons__.__pymysql__.Cons import __Consult__
from __cons__.__sqlalchemy__.__ConsSqlalchemy import CONSULT


# class __Sql_Connection(ABC):
#     @property
#     def __CNN__(self):
#         try:
#             engine = sqlalchemy.create_engine(
#                 'mysql+pymysql://root:@localhost:3306/python')
#             return engine
#         except:
#             print('Não foi possível se conectar ao BD')


# class CONNECTION(__Sql_Connection):
#     pass


# class CONSULT:
#     @property
#     def __c__(self):
#         __cnn__ = CONNECTION().__CNN__  # Associação
#         try:
#             df = pd.read_sql_table('mercado', __cnn__)
#             print(df.head())
#         except:
#             print('Não foi possível consultar no BD')


# class GRUD(ABC):
#   class __Connection__:
#     @property
#     def __cnn__(self):
#         try:
#             db = pymysql.connect(
#                 host='localhost',
#                 user='root',
#                 password='',
#                 db='python',
#                 charset='utf8mb4',
#                 cursorclass=pymysql.cursors.DictCursor

#             )
#             return db  # Irá retornar a conexão do BD

#         except:
#             print("Não foi possívele estabelecer a conexão")
#         else:
#             print('Conexão realizada com sucesso')

#   class __Consult__(ABC):
#     @property
#     def __cnst__(self):
#         try:
#             with __Connection__().__cnn__.cursor() as cursor:  # Irá realizar uma associação
#                 cursor.execute('SELECT * FROM MERCADO')
#                 __r__ = cursor.fetchall()
#             print('\n')
#             for r in __r__:
#                 print(r)
#             print('\n')
#         except:
#             print("Não foi possível realizar a consulta no BD")

#   class __Delete__(ABC):
#     id = 1
#     @property
#     def __dell__(self):
#         try:
#             with __Connection__().__cnn__.cursor() as cursor:
#                 try:
#                     cursor.execute(
#                         f'DELETE FROM mercado WHERE id = {self.id}')
#                     __Connection__().__cnn__.commit()
#                 except:
#                     print("Houve um erro inesperado")
#         except:
#             print("Houve um erro ao deletar dados do BD")
#         else:
#             print("Deleteção realizada com sucesso")

#   class __Update__(ABC):
#     @property
#     def __updat__(self):
#         try:
#             with __Connection__().__cnn__.cursor() as cursor:
#                 try:
#                     cursor.execute("")
#                     __Connection__().__cnn__.commit()
#                 except:
#                     print("Houve um erro inesperado")
#         except:
#             print("Não foi possível realizar a atualização de dados do BD")
#         else:
#             print("Atualização realizada com sucesso")

#   class __Insert__(ABC):
#     produto = 'refri'
#     valor = 5.55
#     @property
#     def __inst__(self):
#         try:
#             with __Connection__().__cnn__.cursor() as cursor:
#                 try:
#                     cursor.execute(
#                         f"INSERT INTO mercado (produto, valor)VALUES ('{self.produto}', {self.valor})")
#                     __Connection__().__cnn__.commit()
#                 except:
#                     print('Houve um erro inesperado')
#         except Exception as e:
#             print('Não foi possível inserir dados ao BD', e)