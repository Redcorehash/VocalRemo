# Vocal Remover

![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)
![Flask Version](https://img.shields.io/badge/Flask-2.3.2-green)
![Spleeter Version](https://img.shields.io/badge/Spleeter-2.4.0-orange)
![License](https://img.shields.io/badge/license-MIT-brightgreen)

Vocal Remover — это веб-приложение для удаления вокала из аудиофайлов. Проект использует библиотеку `spleeter` от Deezer для разделения аудио на вокал и аккомпанемент и `Flask` для создания веб-интерфейса.

## Функциональность

- Загрузка аудиофайлов (поддерживаются форматы MP3 и WAV).
- Автоматическое удаление вокала из загруженного аудио.
- Сохранение результата (инструментальная версия) в папку `uploads`.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-username/vocal-remover.git
   cd vocal-remover
