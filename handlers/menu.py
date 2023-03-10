import json
import asyncio
from functools import partial
from pywebio.output import *
import pywebio.input as inp
from pywebio.session import run_js


class TaskHandler:
    def __init__(self):
        self.__coins = ["BTC", "ETH"]

    @staticmethod
    def read_task_file(self):
        with open("tasks.json", encoding="utf-8") as file:
            return json.load(file)

    def add_task_to_file(data: dict):
        last_changes = TaskHandler.read_task_file()
        last_changes[data["name"]] = data["price to alert"]
        with open('tasks.json', 'w', encoding='utf-8') as file:
            json.dump(last_changes, file, indent=4)

    @staticmethod
    def delete_task_in_file(coin_name, update=True):
        last_changes = TaskHandler.read_task_file()
        try:
            del last_changes[coin_name]
            with open('tasks.json','w', encoding='utf-8') as file:
                json.dump(last_changes, file, indent=4)


        except KeyError:
            print("Ключ отсутствует в спискезаданий")
        if update:
            run_js('location.reload()')
"wqweqweqweqwe"