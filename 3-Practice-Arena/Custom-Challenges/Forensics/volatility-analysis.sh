#!/bin/bash
# Volatility analysis for memory-ctf.raw

VOL_PROFILE="Win10x64_19041"
MEM_FILE="memory-ctf.raw"

vol.py -f $MEM_FILE --profile=$VOL_PROFILE imageinfo
vol.py -f $MEM_FILE --profile=$VOL_PROFILE pslist
vol.py -f $MEM_FILE --profile=$VOL_PROFILE filescan
vol.py -f $MEM_FILE --profile=$VOL_PROFILE dumpfiles -Q 0x00000000abcd1234 -D output/