import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32" or sys.platform == "win64":
    base = "Win32GUI"  # Use Win32GUI for Windows applications

setup(
    name="Jiandan",
    version="1.0",
    description="Приложение для конвертации вокабуляров из pdf файлов в колоды для Anki ",
    executables=[Executable("main.py", base=base)]
)
