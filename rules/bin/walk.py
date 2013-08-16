#!/usr/bin/env python

import os, sys

from optparse import OptionParser

Parser = OptionParser( usage="%prog [options]\ntype \"%prog -h\" for help", version="%prog 1.0")

Parser.add_option('-p', '--path',    dest='path',       type  ='string',     default='',
	help='Path')
Parser.add_option('-V', '--verbose', dest='verbose',    action='store_true', default=False,
	help='Verbose mode.')
Parser.add_option('-D', '--debug',   dest='debug',      action='store_true', default=False,
	help='Debug mode.')

(Options, Args) = Parser.parse_args()

if Options.path == '':
	print('ERROR: path is not specified.')
	sys.exit(1)

if Options.verbose:
	print('Path = "%s"' % Options.path)

if not os.path.isdir( Options.path):
	print('ERROR: path does not exist:')
	print( Options.path)
	sys.exit(1)

for root, dirs, files in os.walk( Options.path):
	print( root)

