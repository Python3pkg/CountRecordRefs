CountRecordRefs
===============

|License|

``CountRecordRefs`` is a command-line tool for counting
records that refer to a database table in MySQL. The program
outputs the number of records for each foreign key column.

Source repository: `<https://github.com/jmenglund/CountRecordRefs>`_

--------------------------------

.. contents:: Table of contents
   :depth: 2
   :backlinks: none
   :local:


Prerequisites
-------------

Apart from `MySQL <https://www.mysql.com>`_ itself, you only need 
to have the python package `PyMySQL <https://github.com/PyMySQL/PyMySQL>`_ 
installed. If you install ``CountRecordRefs`` following the instructions
below, PyMySQL will be installed automatically for you.


Installation
------------

The project is hosted at https://github.com/jmenglund/CountRecordRefs
and can be installed using git:

.. code-block::

    $ git clone https://github.com/jmenglund/CountRecordRefs.git
    $ cd CountRecordRefs
    $ python setup.py install

You may consider installing ``CountRecordRefs`` within a virtual 
environment in order to avoid cluttering your system's Python path. 
See for example the environment management system  
`conda <http://conda.pydata.org>`_ or the package 
`virtualenv <https://virtualenv.pypa.io/en/latest/>`_.

This project is basically a self-contained single-module (single-file) 
executable script that also can be called as such.


Usage
-----

.. code-block::

    usage: CountRecordRefs.py [-h] [-V] [--user USER] [--password PASSWORD]
                              [--host HOST] [-z]
                              database_name table_name id
    
    Command-line utility for counting related records in a MySQL database. Output
    is written to <stdout>.
    
    positional arguments:
      database_name        MySQL database name
      table_name           table name
      id                   primary key value to look up
    
    optional arguments:
      -h, --help           show this help message and exit
      -V, --version        show program's version number and exit
      --user USER          MySQL user (default: "root")
      --password PASSWORD  MySQL password
      --host HOST          database host (default: "localhost")
      -z, --zero-counts    include zero-counts in output


License
-------

``CountRecordRefs`` is distributed under the 
`GNU General Public License, version 3 (GPL-3.0) <https://opensource.org/licenses/GPL-3.0>`_.


Author
------

Markus Englund, `orcid.org/0000-0003-1688-7112 <http://orcid.org/0000-0003-1688-7112>`_

.. |License| image:: https://img.shields.io/badge/license-GNU%20GPL%20version%203-blue.svg
   :target: https://raw.githubusercontent.com/jmenglund/CountRecordRefs/master/LICENSE.txt