from cx_Freeze import setup, Executable

setup(
    name="Jiandan",
    version="1.0",
    description="Приложение для конвертации вокабуляров из pdf файлов в колоды для Anki ",
    executables=[Executable("your_script.py")]
)
