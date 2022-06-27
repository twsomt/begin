class Contact:
    def __init__(self, name, phone, address, birthday):
        self.name = name
        self.phone = phone
        self.address = address
        self.birthday = birthday
        print(f"Создаём новый контакт {name}")

mike = Contact('Михаил Булгаков', '2-03-27', 'Россия, Москва, Большая Пироговская, дом 35б, кв. 6', '15.05.1891')
vlad = Contact('Владимир Маяковский', '73-88', 'Россия, Москва, Лубянский проезд, д. 3, кв. 12', '19.07.1893')

def print_contact():
    print(f"{mike.name} — адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}")
    print(f"{vlad.name} — адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}")

mike.address = 'Россия, Москва, Нащокинский переулок, дом 3, кв. 44'
mike.phone = '1111111'
vlad.address = 'Россия, Москва, Гендриков переулок, дом 15, кв. 5'
vlad.phone = '2-35-71'

print_contact()