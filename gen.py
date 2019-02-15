#!/usr/bin/env python
# encoding: utf-8

import os, subprocess, sys, base64

TMPL_NAME = 'unittestt.py'
DEST_NAME = 'unittest_gtest.py'
TARBALL_NAME = 'fused-gtest.tar.bz2'
GTEST_DIR = 'gtest-1.8.1/fused-src/gtest'

try:
  if subprocess.call(['tar', 'cjf', TARBALL_NAME, GTEST_DIR]):
    raise

  t = open(TMPL_NAME, 'rb')
  scr = t.read()
  t.close()

  t = open(TARBALL_NAME, 'rb')
  tbz = t.read()
  t.close()

  scr += '#==>\n#'.encode()
  scr += base64.b64encode(tbz)
  scr += '\n#<==\n'.encode()

  t = open(DEST_NAME, 'wb')
  t.write(scr)
  t.close()

  os.unlink(TARBALL_NAME)

except:
  print(sys.exc_info()[1])
