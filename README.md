# CSVZero2Min
# Language: Python
# Input: CSV (with zero entries)
# Output: CSV (with zero entries mapped to minimum value, no rescaling)
# Tested with: PluMA 1.0, Python 2.7

PluMA plugin to change all zeroes in a CSV file to the minimum value in the same file.
This can be useful particularly when the potential error for measurement is relatively high,
i.e. higher than the difference between the minimum value and zero, and they need to be
treated the same in downstream analysis.  Note this plugin closely relates to the CSVScale
(https://github.com/movingpictures83/CSVScale) plugin, however unlike that plugin there is no rescaling.

The plugin accepts as input the CSV file with zero values, records the minimum value in that same file,
and produces as output the equivalent CSV file with the zero values mapped to that minimum value.

