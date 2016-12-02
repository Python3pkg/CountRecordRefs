#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Count related records in a MySQL database.
"""

import argparse
import getpass
import sys

import pymysql.cursors


__author__ = 'Markus Englund'
__license__ = 'GNU GPLv3'
__version__ = '0.2.1'


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


def print_ref_counts(
        user, host, password, db, related_columns,
        lookup_id, zero_counts=False):
    if related_columns is None:
        raise ValueError('No related columns exists!')
    connection = pymysql.connect(
        host=host, user=user, password=password, db=db,
        cursorclass=pymysql.cursors.DictCursor)
    sys.stdout.write('table_name\tcolumn_name\tcount\n')
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
                    sys.stdout.write(
                        row['TABLE_NAME'] + '\t' +
                        row['COLUMN_NAME'] + '\t' +
                        str(cnt) + '\n')
    finally:
        connection.close()


def parse_args(args):
    parser = argparse.ArgumentParser(
        description=(
            'Command-line utility for counting  '
            'related records in a MySQL database. '
            'Output is written to <stdout>.'))
    parser.add_argument(
        '-V', '--version', action='version',
        version='CountRecordRefs.py ' + __version__)
    parser.add_argument(
        '--user', type=str, action='store', default='root',
        dest='user', help='MySQL user (default: "root")')
    parser.add_argument(
        '--password', type=str, action='store', default=None,
        dest='password', help='MySQL password')
    parser.add_argument(
        '--host', type=str, action='store', default='localhost',
        dest='host', help='database host (default: "localhost")')
    parser.add_argument(
        '-z', '--zero-counts', action='store_true',
        dest='zero_counts', help='include counts of zero in output')
    parser.add_argument(
        'database_name', type=str, action='store', help='MySQL database name')
    parser.add_argument(
        'table_name', type=str, action='store',
        help='table name')
    parser.add_argument(
        'id', type=str, action='store', help='primary key value to look up')
    return parser.parse_args(args)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = parse_args(args)

    if not parser.password:
        password = getpass.getpass('MySQL password:')
    else:
        password = parser.password

    related_columns = get_related_columns(
        user=parser.user,
        host=parser.host,
        password=password,
        db=parser.database_name,
        table_name=parser.table_name)

    print_ref_counts(
        user=parser.user,
        host=parser.host,
        password=password,
        db=parser.database_name,
        related_columns=related_columns,
        lookup_id=parser.id,
        zero_counts=parser.zero_counts)

if __name__ == '__main__':
    main()
