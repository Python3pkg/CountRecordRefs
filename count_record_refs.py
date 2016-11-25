#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Count all records that refer to a database table in MySQL.
"""

from __future__ import print_function
import argparse
import getpass
import pymysql.cursors
import sys


__author__ = 'Markus Englund'
__license__ = 'GNU GPLv3'
__version__ = '0.1.0'


def get_related_columns(user, host, password, db, table_name):
    connection = pymysql.connect(
        host=host, user=user, password=password, db='information_schema',
        cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = """SELECT TABLE_NAME, COLUMN_NAME
                  FROM KEY_COLUMN_USAGE
                  WHERE
                      TABLE_SCHEMA = '{db}' AND
                      REFERENCED_TABLE_NAME = '{table_name}'
                  """.format(db=db, table_name=table_name)
            cursor.execute(sql)
            related_columns = cursor.fetchall()
    finally:
        connection.close()
    return(related_columns)


def get_used_columns(
        user, host, password, db, related_columns,
        lookup_id, zero_counts=False):
    if related_columns is None:
        raise ValueError('No related columns exists!')
    connection = pymysql.connect(
        host=host, user=user, password=password, db=db,
        cursorclass=pymysql.cursors.DictCursor)
    print('table_name\tcolumn_name\tcount')
    try:
        with connection.cursor() as cursor:
            for row in related_columns:
                sql = """SELECT {column_name}
                      FROM {table_name}
                          WHERE {column_name} = '{lookup_id}'
                      """.format(
                          table_name=row['TABLE_NAME'],
                          column_name=row['COLUMN_NAME'],
                          lookup_id=lookup_id)
                cnt = cursor.execute(sql)
                if (zero_counts and cnt == 0) or cnt > 0:
                    print(
                        row['TABLE_NAME'] + '\t' +
                        row['COLUMN_NAME'] + '\t' +
                        str(cnt))
    finally:
        connection.close()


def parse_args(args):
    parser = argparse.ArgumentParser(
        description=(
            'Command-line utility for counting records '
            'that refer to a database table in MySQL.'))
    parser.add_argument(
        '-V', '--version', action='version',
        version='CountRecordRefs.py ' + __version__)
    parser.add_argument(
        '--user', type=str, action='store', default=None,
        dest='user', help='MySQL user')
    parser.add_argument(
        '--password', type=str, action='store', default=None,
        dest='password', help='MySQL password')
    parser.add_argument(
        '--host', type=str, action='store', default='localhost',
        dest='host', help='database host')
    parser.add_argument(
        '--database', type=str, action='store', required=True,
        dest='database', help='database name')
    parser.add_argument(
        '-z', '--zero-counts', action='store_true',
        dest='zero_counts', help='include zero-counts in output')
    parser.add_argument(
        'table_name', type=str, action='store',
        help='table name')
    parser.add_argument(
        'id', type=int, action='store', help='ID-value to look up')
    return parser.parse_args(args)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = parse_args(args)

    if not parser.password:
        password = getpass.getpass('Password:')
    else:
        password = parser.password

    related_columns = get_related_columns(
        user=parser.user,
        host=parser.host,
        password=password,
        db=parser.database,
        table_name=parser.table_name)

    get_used_columns(
        user=parser.user,
        host=parser.host,
        password=password,
        db=parser.database,
        related_columns=related_columns,
        lookup_id=parser.id,
        zero_counts=parser.zero_counts)

if __name__ == '__main__':
    main()
