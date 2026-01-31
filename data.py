class Data:
    valid_login = 'Abram06'
    valid_password = 'qwerty'
    valid_firstname = 'Abram'
    valid_courier_data = {'login': 'Abram06', 'password': 'qwerty', 'firstName': 'Max'}
    courier_data_without_name = {'login': 'Abram06', 'password': '1234'}
    courier_data_with_wrong_password = {'login': 'Abram06', 'password': '123456'}


class OrderData:
    order_data_grey_1 = {
        'firstName': 'Илья',
        'lastName': 'Борисыч',
        'address': 'Зацепский вал, 3',
        'metroStation': 8,
        'phone': '+79085859348',
        'rentTime': 3,
        'deliveryDate': '2024-06-26',
        'comment': 'Погода славная, а это главное.',
        'color': ['GREY']
    }

    order_data_black_2 = {
        'firstName': 'Йеннифэр',
        'lastName': 'изВенгерберга',
        'address': 'Туссент, улица Яблоневая',
        'metroStation': 10,
        'phone': '+78888888888',
        'rentTime': 7,
        'deliveryDate': '2024-06-28',
        'comment': 'Жил я славно в первой трети.',
        'color': ['BLACK']
    }

    order_data_two_colors_3 = {
        'firstName': 'Цирилла Фиона',
        'lastName': 'Рианнон',
        'address': 'Шалфей и Розмарин',
        'metroStation': 15,
        'phone': '+70009991122',
        'rentTime': 1,
        'deliveryDate': '2024-06-30',
        'comment': 'Я вам мозги не пудрю!',
        'color': ['BLACK', 'GREY']
    }

    order_data_no_colors_4 = {
        'firstName': 'Калантэ',
        'lastName': 'ArdRhena',
        'address': 'Замок Цинтры',
        'metroStation': 20,
        'phone': '+77777777777',
        'rentTime': 2,
        'deliveryDate': '2024-06-27',
        'comment': 'Спасение утопающих дело рук самих утопающих.',
        'color': []
    }
