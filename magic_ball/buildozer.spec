[app]
# Название вашего приложения
title = MagicBall

# Имя пакета
package.name = magicball

# Версия приложения
version = 1.0

# (обязательно) Используемый файл .kv (если есть)
source.dir = .

# (опционально) Дополнительные файлы / папки, необходимые во время выполнения приложения
source.include_exts = py
source.include_patterns = main.py

# (обязательно) Зависимости пакетов Python, необходимых во время выполнения вашего приложения
requirements = kivy

[buildozer]
# (обязательно) Настройки для сборки APK
# Поменяйте 'android' на 'ios' для сборки приложения под iOS
target = android
