#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'short'

STORYLEN = len(MYINPUT)

if STORYLEN > MAX_LENGTH:
    LONGSTR = 'long'

OUTPUT = 'That certainly was a {} story!'.format(LONGSTR)
print OUTPUT
