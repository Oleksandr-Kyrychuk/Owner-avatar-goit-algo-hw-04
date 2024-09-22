from pathlib import Path

path = r"C:\Users\ALEX\Desktop\gusak\cats_file.txt"

def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding = "UTF-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts)== 3:
                    cats_info = {"id":parts[0], "name":parts[1], "age":parts[2]}
                    cats.append(cats_info)
                else:
                    print(f"Помилка, неправильний формат данних")
    except FileNotFoundError:
        print(f"Файл не знайдено")
    return cats

cats_info = get_cats_info(path)
print(cats_info)