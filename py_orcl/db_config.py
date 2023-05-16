# ------------------------------------------------------------------------------
# Copyright (c) 2021, Oracle and/or its affiliates. All rights reserved.
# ------------------------------------------------------------------------------

import cx_Oracle
import sys
import os
import getpass

######################################################################

#
# Oracle Client library configuration
#

# On Linux this must be None.
# Instead, the Oracle environment must be set before Python starts.
instant_client_dir = None

# On Windows, if your database is on the same machine, comment these lines out
# and let instant_client_dir be None.  Otherwise, set this to your Instant
# Client directory.  Note the use of the raw string r"..."  so backslashes can
# be used as directory separators.
if sys.platform.startswith("win"):
    # instant_client_dir = r"c:\oracle\instantclient_19_10"
    instant_client_dir = r"d:\orcl\instantclient-basic-windows.x64-21.3.0.0.0\instantclient_21_3"
    # dsn = os.environ.get("PYTHON_CONNECT_STRING", "192.168.1.196:1521/helowin")
    dsn = os.environ.get("PYTHON_CONNECT_STRING", "10.1.10.6:1521/helowin")

# On macOS (Intel x86) set the directory to your Instant Client directory
if sys.platform.startswith("darwin"):
    # instant_client_dir = os.environ.get("HOME") + "/Downloads/instantclient_19_8"
    instant_client_dir = "/Users/tianm/docker/oracle/instantclient_19_8"
    dsn = os.environ.get("PYTHON_CONNECT_STRING", "127.0.0.1:1521/helowin")

# This can be called at most once per process.
if instant_client_dir is not None:
    cx_Oracle.init_oracle_client(lib_dir=instant_client_dir)

######################################################################

#
# Tutorial credentials and connection string.
# Environment variable values are used, if they are defined.
#

user = os.environ.get("PYTHON_USER", "major_2020_8_24_1")
pw = os.environ.get("PYTHON_PASSWORD", "nmajor")
if pw is None:
    pw = getpass.getpass("Enter password for %s: " % user)
