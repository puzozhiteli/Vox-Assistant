from vacore import VACore
import webbrowser
import os

def start(core: VACore):
    manifest = {
        "name": "Открытие браузера",
        "version": "1.0",
        "require_online": False,

        "commands": {
            "открой браузер|запусти браузер|браузер": run_browser,
            "открой сайт|открой страницу|перейди на сайт": open_website,
        }
    }
    return manifest

def run_browser(core: VACore, phrase: str):
    # Открытие браузера по умолчанию
    webbrowser.open_new("")
    return "Открываю браузер"

def open_website(core: VACore, phrase: str):
    # Извлекаем название сайта из фразы
    if "яндекс" in phrase:
        webbrowser.open_new("https://yandex.ru")
        return "Открываю Яндекс"
    elif "гугл" in phrase or "google" in phrase:
        webbrowser.open_new("https://google.com")
        return "Открываю Гугл"
    elif "ютуб" in phrase or "youtube" in phrase:
        webbrowser.open_new("https://youtube.com")
        return "Открываю Ютуб"
    else:
        return "Какой сайт открыть? Уточните, пожалуйста."
