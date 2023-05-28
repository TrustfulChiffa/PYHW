# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def change_record():
    if all_data:
        name = input("Enter the name or surname of the record to change: ")
        found_records = []
        for record in all_data:
            if name.lower() in record.lower():
                found_records.append(record)

        if found_records:
            print("Found records:")
            for idx, record in enumerate(found_records):
                print(f"{idx + 1}. {record}")

            choice = input("Enter the number of the record to change: ")
            if choice.isdigit() and 1 <= int(choice) <= len(found_records):
                record_index = int(choice) - 1
                record_data = found_records[record_index].split()
                new_data = input("Enter the new data: ")
                updated_record = " ".join([new_data] + record_data[1:])
                all_data[all_data.index(found_records[record_index])] = updated_record
                with open(file_base, "w", encoding="utf-8") as f:
                    f.write("\n".join(all_data))
                print("Record changed successfully!")
            else:
                print("Invalid choice!")
        else:
            print("No records found.")
    else:
        print("Empty data")


def delete_record():
    if all_data:
        name = input("Enter the name or surname of the record to delete: ")
        found_records = []
        for record in all_data:
            if name.lower() in record.lower():
                found_records.append(record)

        if found_records:
            print("Found records:")
            for idx, record in enumerate(found_records):
                print(f"{idx + 1}. {record}")

            choice = input("Enter the number of the record to delete: ")
            if choice.isdigit() and 1 <= int(choice) <= len(found_records):
                record_index = int(choice) - 1
                del found_records[record_index]
                with open(file_base, "w", encoding="utf-8") as f:
                    f.write("\n".join(all_data))
                print("Record deleted successfully!")
            else:
                print("Invalid choice!")
        else:
            print("No records found.")
    else:
        print("Empty data")


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                pass
            case "3":
                pass
            case "4":
                change_record()
            case "5":
                delete_record()
            case "6":
                pass
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()