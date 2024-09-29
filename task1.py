from queue import Queue 
from faker import Faker

queue = Queue()
faker = Faker()

def generate_request():
    inquiry = faker.text(max_nb_chars=50)
    queue.put(inquiry)
    print(f"\nЗаявку '{inquiry}' згенеровано\n")


def process_request():
    if not queue.empty():
        inquiry = queue.get()
        print(f"\nзаявка '{inquiry}' оброблена\n")
    else:
        print("\nЧерга пуста. Заявок на даний момент немає.\n")

def main():
    while True:
        command = input("Нажміть Enter щоб згенерувати заявку. \nКоманда process - обробити заявку. \nАбо введіть exit щоб вийти.\n")
        
        if command == '':
            generate_request()
        elif command == 'process':
            process_request()
        elif command == 'exit':
            print("Вихід із програми")
            break
        else:
            print("\nТакої кманди не існує.\n")

if __name__ == "__main__":
    main()