CountRecordRefs.py
==================

|License|

``CountRecordRefs.py`` is a command-line tool for counting
records that refer to a database table in MySQL.

Source repository: `<https://github.com/jmenglund/CountRecordRefs>`_

--------------------------------

.. contents:: Table of contents
   :backlinks: top
   :local:


Installation
------------

The project is hosted at https://github.com/jmenglund/CountRecordRefs
and can be installed using git:

.. code-block::

    $ git clone https://github.com/jmenglund/CountRecordRefs.git
    $ cd CountRecordRefs
    $ python setup.py install

You may consider installing ``CountRecordRefs`` and its required
package ``PyMySQL`` within a virtual environment in order to avoid 
cluttering your system's Python path. See for example the 
environment management system  `conda <http://conda.pydata.org>`_ 
or the package `virtualenv <https://virtualenv.pypa.io/en/latest/>`_.


Usage
-----

.. code-block::
    
    CountRecordRefs.py --help
    usage: CountRecordRefs.py [-h] [-V] [--user USER] [--password PASSWORD]
                              [--host HOST] --database DATABASE [-z]
                              table_name id

    Command-line utility for counting records that refer to a database 
    table in MySQL.

    positional arguments:
      table_name           table name
      id                   ID-value to look up

    optional arguments:
    -h, --help           show this help message and exit
    -V, --version        show program's version number and exit
    --user USER          MySQL user
    --password PASSWORD  MySQL password
    --host HOST          database host
    --database DATABASE  database name
    -z, --zero-counts    include zero-counts in output


License
-------

``CountRecordRefs`` is distributed under the 
`GNU General Public License, version 3 (GPL-3.0) <https://opensource.org/licenses/GPL-3.0>`_.


Author
------

Markus Englund, `orcid.org/0000-0003-1688-7112 <http://orcid.org/0000-0003-1688-7112>`_

.. |License| image:: https://img.shields.io/badge/license-GNU%20GPL%20version%203-blue.svg
   :target: https://raw.githubusercontent.com/jmenglund/predsim/master/LICENSE.txt