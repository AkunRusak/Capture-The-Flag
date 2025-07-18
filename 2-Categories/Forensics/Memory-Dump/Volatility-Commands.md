# Volatility Commands Reference

## Info Dasar

volatility -f memory-dump.raw imageinfo
volatility -f memory-dump.raw --profile=Win7SP1x64 pslist
volatility -f memory-dump.raw --profile=Win7SP1x64 pstree
volatility -f memory-dump.raw --profile=Win7SP1x64 netscan


## Dump & Analisis

volatility -f memory-dump.raw --profile=Win7SP1x64 cmdline
volatility -f memory-dump.raw --profile=Win7SP1x64 filescan
volatility -f memory-dump.raw --profile=Win7SP1x64 dumpfiles -Q 0xADDRESS -D output/
volatility -f memory-dump.raw --profile=Win7SP1x64 hashdump


## Malware Analysis

volatility -f memory-dump.raw --profile=Win7SP1x64 malfind
volatility -f memory-dump.raw --profile=Win7SP1x64 apihooks
volatility -f memory-dump.raw --profile=Win7SP1x64 dlllist -p <pid>
