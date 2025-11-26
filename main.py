import pytest
import sys
import os

def main():
    test_file = "Only_tests.py"
    if not os.path.exists(test_file):
        print(f"Файл {test_file} не найден. Убедитесь, что он находится рядом с main.py")
        sys.exit(1)
    print("Запуск тестов Playwright...\n")

    exit_code = pytest.main([
        test_file,
        "-v",               # подробный вывод
        "--disable-warnings",
        "--maxfail=1"
    ])

    # Выход с кодом выполнения
    sys.exit(exit_code)

if __name__ == "__main__":
    main()