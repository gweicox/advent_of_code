import os
import sys


def create_and_update_file(template_path, new_file_path, year, day):
    with open(template_path, 'r') as template_file:
        content = template_file.read()
    updated_content = content.replace("20xx", year).replace("dxx", f"d{day}")

    with open(new_file_path, 'w') as new_file:
        new_file.write(updated_content)


if len(sys.argv) != 2:
    print("Используйте команду: python create_next_challenge.py <год>")
    sys.exit(1)

year = sys.argv[1]

if year not in map(str, range(2015, 2024)):
    print("Год должен быть в диапазоне 2015-2023")
    sys.exit(1)

base_dir = os.path.dirname(os.path.realpath(__file__)) #os.getcwd()
template_file = "20xx_dxx.py"
template_path = os.path.join(base_dir, template_file)

year_dir = os.path.join(base_dir, year)

if not os.path.exists(year_dir):
    os.makedirs(year_dir)

day_num = 1

while True:
    day = str(day_num).zfill(2)
    new_file_path = os.path.join(year_dir, f"{year}_d{day}.py")

    if not os.path.isfile(new_file_path):
        create_and_update_file(template_path, new_file_path, year, day)
        print(f"Создан файл: {new_file_path}")
        break

    day_num += 1
    if day_num == 26:
        print(f"Все 25 файлов за {year} год уже есть")
        sys.exit(1)
