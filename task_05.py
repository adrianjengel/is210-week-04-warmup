#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05 WK4 warmup - My bloodpressure"""


BP_INPUT = int(raw_input('What is your blood pressure? '))

if BP_INPUT <= 89:
    BP_INPUT = 'Low'

elif BP_INPUT >= 90 and BP_INPUT <= 119:
    BP_INPUT = 'Ideal'

elif BP_INPUT >= 120 and BP_INPUT <= 139:
    BP_INPUT = 'Warning'

elif BP_INPUT >= 140 and BP_INPUT <= 159:
    BP_INPUT = 'High'

else: BP_INPUT = 'Emergency'

BP_STATUS = 'The level of your status is currently: {}'.format(BP_INPUT)

print BP_STATUS
