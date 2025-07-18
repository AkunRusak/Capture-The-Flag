# Ghidra Python Script: Rename dan Comment Otomatis

from ghidra.program.model.symbol import SourceType

func = getGlobalFunctions("main")[0]
func.setName("main_func", SourceType.USER_DEFINED)

entry = func.getEntryPoint()
setEOLComment(entry, "Entry point to main")

print("[+] Renamed main and added comment")