import os
import pywebio
import threading
from pywebio.output import *
import pywebio.input as inp

@pywebio.config(theme="dark")
async def main():
    clear()

    logo_path = os.path.join('data', 'logo.jpg')
    put_image(open(logo_path, 'rb').read())

    method = await inp.select(
        "Выберите нужный вариант",
        [
            "Добавить задание",
            "Список заданий"
        ]
    )

    if "Добавить заданий" == method:
        ...
    elif "Список заданий" == method:
        ...

if __name__ =="__main__":
    pywebio.start_server(main, host="0.0.0.0", port=4444)