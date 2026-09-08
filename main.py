import pickle

l = 600  # внутренняя длина в мм
w = 400  # внутренняя ширина в мм
h = 300  # внутренняя высота в мм
tsten = 15  # толщина стены в мм
tosnov = 20  # толщина дна в мм
totbort = 100  # толщина отбортовки в мм
tobl = 5  # толщина облицовки бандажа в мм
oone = 3  # количество поясов бандажа
uone = 2  # вертикальные ребра по длине ванны
utwo = 1  # вертикальные ребра по ширине ванны
tfut = 4  # толщина футеровки в мм
kone = 1.28  # учет потерь при раскрое



def checkint(a):
    """Функция запрашивает ввод и проверяет, что это целое число"""
    while True:
        try:
            b = int(a)
            return b
        except ValueError:
            print(f"Ошибка ввода, попробуйте еще раз")
            a = input(f"Введите значение еще раз: ")


def checkfloat(a):
    """Функция запрашивает ввод и проверяет, что это дробное число"""
    while True:
        try:
            b = float(a)
            return b
        except ValueError:
            print(f"Ошибка ввода, попробуйте еще раз")
            a = input(f"Введите значение еще раз: ")


def save():
    materialfile = open("material.dat", "wb")
    pickle.dump(profileplsts, materialfile)
    pickle.dump(profilemetls, materialfile)
    materialfile.close()


class Matterial:  # материал
    def __init__(self, name, density=None, price=None):
        self.name = name
        self.density = density
        self.price = price

    def greet(self):
        print(f"Материал {self.name}, test2, test3 {self.price}.")


print(l, w, h)


class Plast(Matterial):
    def __init__(self, name, density, price):
        super().__init__(name, density, price)

    def plst(self):
        print(f"Материал {self.name}, плотность {self.density} г/см3, стоимость {self.price} руб/кг.")


class Metal(Matterial):
    def __init__(self, name, price, sidea, sideb, thickness, length):
        super().__init__(name, None, price)
        self.density = 7850
        self.sidea = sidea
        self.sideb = sideb
        self.thickness = thickness
        self.length = length

    def weightmetl(self):
        wemet = round(0.0157 * self.thickness * (self.sidea + self.sideb - 2.86 * self.thickness), 2)
        return wemet

    def metl(self):
        print(
            f"Профиль стальной {self.name}, стоимость за 1 тонну {self.price} руб., Высота: {self.sidea} мм., Ширина: {self.sideb} мм., толщина {self.thickness} мм, длина профиля {self.length} мм.")


# блок списка материалов ванн
profileplsts = []

# блок списка металлических профилей
profilemetls = []

# Модуль сохранения и чтения из файла
try:
    materialfile = open("material.dat", "rb")
    profileplsts = pickle.load(materialfile)
    profilemetls = pickle.load(materialfile)
    materialfile.close()
except (FileNotFoundError, EOFError):
    test1 = Plast('PP-H', 0.92, 300)
    test2 = Plast('PVDF', 1.796, 5200)
    profileplsts.append(test1)
    profileplsts.append(test2)
    test3 = Metal('60*40*4', 77, 60, 40, 4, 6000)
    test4 = Metal('120*80*3', 77, 120, 80, 3, 6000)
    profilemetls.append(test3)
    profilemetls.append(test4)
    save()

# блок списка результатов
resultvan = []

# Модуль сохранения и чтения результата
try:
    resultvanfile = open("resultvan.dat", "rb")
    resultvan = pickle.load(resultvanfile)
    resultvanfile.close()
except (FileNotFoundError, EOFError):
    resultvanfile = open("resultvan.dat", "wb")
    resultvanfile.close()

# Меню
while True:
    print(f"Расчет стоимости гальванической ванны")
    print(f"-" * 40)
    print(
        f"\t 1. Расчет стоимости ванны \n\t 2. Управление материалами ванн\n\t 3. Управление материалами обрешётки\n\t 4. Результаты расчетов \n\t 5. Выход ")
    print(f"-" * 40)
    menu = checkint(input("Введите пункт меню: "))
    if menu == 1:
        print(f"\t Текущие внутренние размеры ванны: \n\t Длина: {l} мм.\n\t Ширина {w} мм.\n\t Высота {h} мм")
        l = checkint(input("Введите длину: "))
        w = checkint(input("Введите ширину: "))
        h = checkint(input("Введите высоту: "))
        tsten = checkint(input("Введите толщину стены в мм.: "))
        tosnov = checkint(input("Введите толщину дна мм.: "))
        totbort = checkint(input("Введите толщину отбортовки мм.: "))
        tfut = checkint(input("Введите толщину футеровки в мм.: "))
        tobl = checkint(input("Введите толщину облицовки бандажа в мм.: "))
        oone = checkint(input("Введите количество поясов бандажа шт.: "))
        uone = checkint(input("Введите количество вертикальных ребр по длине ванны в шт.: "))
        utwo = checkint(input("Введите количество вертикальных ребер по ширине ванны в шт.: "))

        # Выбор материала и футеровки
        for i, profileplst in enumerate(profileplsts, 1):
            print(f"{i}. ", end="")
            profileplst.plst()

        # Выбор материала ванны
        while True:
            print(f"Выберите материал ванны и футеровки")
            choisplst = checkint(input("Укажите номер выбранного пластика для ванны: "))
            if 1 <= choisplst <= len(profileplsts):
                mat1 = profileplsts[choisplst - 1]
                break
            else:
                print(f"Ошибка ввода, попробуйте еще раз")

        # Выбор материала футеровки
        while True:
            choisfut = checkint(
                input("Укажите номер выбранного пластика для футеровки или укажите 0, если не требуется футеровка: "))
            if 1 <= choisfut <= len(profileplsts):
                mat2 = profileplsts[choisfut - 1]
                vfut = (l * w + 2 * l * h + 2 * w * h) * tfut / 1000  # объем футеровки см3
                mfut = round((vfut * mat2.density) / 1000, 2)  # масса футеровки
                print(f"объем футеровки {vfut} , см3")
                print(f"масса футеровки {mfut} , кг")
                pricefut = round(mfut * mat2.price * kone, 0)  # стоимость футеровки
                print(f"стоимость футеровки {pricefut} руб.")
                break
            elif choisfut == 0:
                mat2 = Plast("Без футеровки", 0, 0)
                pricefut = 0
                break
            else:
                print(f"Ошибка ввода, попробуйте еще раз")

        # блок списка металлических профилей
        for i, profilemetl in enumerate(profilemetls, 1):
            print(f"{i}. ", end="")
            profilemetl.metl()

        # Выбор обрешётки
        while True:
            choisobr = checkint(input("Укажите номер выбранного профиля для обрешетки: "))
            if 1 <= choisobr <= len(profilemetls):
                mat3 = profilemetls[choisobr - 1]
                pvnesh = 2 * ((l + tsten) + (w + tsten))  # периметр внешний
                print(f"периметр внешний {pvnesh} мм")
                lenobr = round(((pvnesh + 4 * mat3.sidea) / 1000) * oone + (
                            (2 * (h + tosnov) + w + 2 * mat3.sidea) / 1000) * uone + (
                                           (2 * (h + tosnov) + l + 2 * mat3.sidea) / 1000) * utwo,
                               2)  # длина обрешётки в м
                print(f"длина обрешотки {lenobr} в м")
                mobr = round(lenobr * mat3.weightmetl(), 2)  # масса обрешётки
                print(f"масса обрешётки {mobr} в кг")
                priceobr = round(mobr * mat3.price, 0)  # стоимость обрешотки
                print(f"стоимость обрешотки {priceobr} руб.")
                vplst = ((l + 2 * tsten) * (w + 2 * tsten) * (h + tosnov) / 1000) - ((l * w * h) / 1000) + (
                            (l + 110) * (w + 110) - (l * w)) / 10 ** 2 * totbort / 10 + (lenobr * 1000 * (
                            2 * mat3.sidea + mat3.sideb) * tobl) / 1000  # объем основного пластика см3
                print(f"объем основного {vplst} пластика см3")
                mplst = round((vplst * mat1.density) / 1000, 2)  # масса основного пластика
                print(f"масса основного пластика {mplst} , кг")
                priceplst = round(mplst * mat1.price * kone, 0)  # стоимость основного пластика
                print(f"стоимость основного пластика {priceplst} руб.")
                pricevan = priceplst + pricefut + priceobr  # стоимость ванны
                print(f"стоимость ванны {pricevan} руб.")
                vvan = round(l * w * h / 1000 ** 3, 2)  # объем ванны м3
                print(f"объем ванны {vvan} м3")
                weightvan = round(mobr + mplst, 2)  # Вес ванны нетто, кг
                print(f"Вес ванны нетто {weightvan} кг.")
                break
            else:
                print(f"Ошибка ввода, попробуйте еще раз")
        resultvanredy = [f"Размер {l}x{w}x{h}", f"объем ванны {vvan} м3", f"стоимость ванны {pricevan} руб."]
        resultvan.append(resultvanredy)
        resultvanfile = open("resultvan.dat", "wb")
        pickle.dump(resultvan, resultvanfile)
        resultvanfile.close()
    elif menu == 2:
        print(f"-" * 40)
        print(f"Текущий перечень материалов:")
        print(f"-" * 40)
        for i, profileplst in enumerate(profileplsts, 1):
            print(f"{i}. ", end="")
            profileplst.plst()
        print(f"-" * 40)

        while True:
            print(f"\t 1. Добавить материал\n\t 2. Удалить материал\n\t 3. Изменение материала\n\t 4. Выход")
            menumat = checkint(input("Введите пункт меню: "))
            if menumat == 1:
                namenew = input("Введите название материала: ")
                densitynew = checkfloat(input("Введите плотность материала, г/см3: "))
                pricenew = checkfloat(input("Введите стоимость материала, руб.: "))
                newmat = Plast(namenew, densitynew, pricenew)
                profileplsts.append(newmat)
                print(f"Материал {namenew} добавлен!")
                save()
            elif menumat == 2:
                remname = checkint(input("Введите номер материала для удаления или 0 для отмены: "))
                if remname == 0:
                    break
                elif 1 <= remname <= len(profileplsts):
                    deleted = profileplsts.pop(remname - 1)
                    print(f"Материал {deleted.name} удален!")
                    save()
                else:
                    print("Ошибка! Неверный номер")
            elif menumat == 3:
                print(f"-" * 40)
                print(f"Текущий перечень материалов:")
                print(f"-" * 40)
                for i, profileplst in enumerate(profileplsts, 1):
                    print(f"{i}. ", end="")
                    profileplst.plst()
                print(f"-" * 40)
                while True:
                    choisplst = checkint(input("Укажите номер выбранного материала для изменения: "))
                    if 1 <= choisplst <= len(profileplsts):
                        matx = profileplsts.pop(choisplst - 1)
                        namenew = matx.name
                        densitynew = matx.density
                        pricenew = matx.price

                        while True:
                            properties = checkint(input(
                                "Что нужно изменить: \n\t 1. Название \n\t 2. Плотность г/см3\n\t 3. Стоимость руб/кг \n\t 4. Выход"))
                            if properties == 1:
                                namenew = input("Введите название материала: ")
                                break

                            elif properties == 2:
                                densitynew = checkfloat(input("Введите плотность материала, г/см3: "))
                                break

                            elif properties == 3:
                                pricenew = checkfloat(input("Введите стоимость материала, руб.: "))
                                break

                            elif properties == 4:
                                break
                            else:
                                print(f"Ошибка ввода, попробуйте еще раз")
                        matx = Plast(namenew, densitynew, pricenew)
                        profileplsts.append(matx)
                        save()
                        break
                    else:
                        print(f"Ошибка ввода, попробуйте еще раз")
            elif menumat == 4:
                break
            else:
                print(f"Ошибка ввода, попробуйте еще раз")

    elif menu == 3:
        print(f"-" * 40)
        print(f"Текущий перечень профилей обрешётки:")
        print(f"-" * 40)
        for i, profilemetl in enumerate(profilemetls, 1):
            print(f"{i}. ", end="")
            profilemetl.metl()
        print(f"-" * 40)

        while True:
            print(f"\t 1. Добавить материал\n\t 2. Удалить материал\n\t 3. Список материалов\n\t 4. Выход")
            menumet = checkint(input("Введите пункт меню: "))
            if menumet == 1:
                namenewmet = input("Введите название профиля: ")
                sideanew = checkfloat(input("Введите ширину профиля, мм.: "))
                sidebnew = checkfloat(input("Введите высоту профиля, мм.: "))
                thicknessnew = checkfloat(input("Введите толщину профиля, мм.: "))
                lengthnew = checkfloat(input("Введите длину профиля, мм.: "))

                pricemetnew = checkfloat(input("Введите стоимость материала, руб.: "))
                newmet = Metal(namenewmet, pricemetnew, sideanew, sidebnew, thicknessnew, lengthnew)
                profilemetls.append(newmet)
                print(f"Материал {namenewmet} добавлен!")
                save()
            elif menumet == 2:
                remnamemetl = checkint(input("Введите номер материала для удаления или 0 для отмены: "))
                if remnamemetl == 0:
                    break
                elif 1 <= remnamemetl <= len(profilemetls):
                    deletedmetl = profilemetls.pop(remnamemetl - 1)
                    print(f"Материал {deletedmetl.name} удален!")
                else:
                    print("Ошибка! Неверный номер")
                save()
            elif menumet == 3:
                print(f"-" * 40)
                print(f"Текущий перечень профилей обрешётки:")
                print(f"-" * 40)
                for i, profilemetl in enumerate(profilemetls, 1):
                    print(f"{i}. ", end="")
                    profilemetl.metl()
                print(f"-" * 40)
                choismetl = checkint(input("Укажите номер выбранного профиля для изменения: "))
                if 1 <= choismetl <= len(profilemetls):
                    maty = profilemetls.pop(choismetl - 1)
                    namenew = maty.name
                    pricenew = maty.price
                    sideanew = maty.sidea
                    sidebnew = maty.sideb
                    thicknessnew = maty.thickness
                    lengthnew = maty.length

                    while True:
                        properties = checkint(input(
                            "Что нужно изменить: \n\t 1. Название \n\t 2. Стоимость за 1 тонну г/см3\n\t 3. Высота мм \n\t 4. Ширина мм \n\t 5. Толщина мм \n\t 6. Длина профиля мм \n\t 7. Выход \n\t Введите позицию: "))
                        if properties == 1:
                            namenew = input("Введите название материала: ")
                            break
                        elif properties == 2:
                            pricenew = checkfloat(input("Введите стоимость материала, руб.: "))
                            break
                        elif properties == 3:
                            sideanew = checkint(input("Введите высоту мм.: "))
                            break
                        elif properties == 4:
                            sidebnew = checkint(input("Введите ширину мм.: "))
                            break
                        elif properties == 5:
                            thicknessnew = checkint(input("Введите толщину мм.: "))
                            break
                        elif properties == 6:
                            lengthnew = checkint(input("Введите длину профиля мм.: "))
                            break
                        elif properties == 7:
                            break
                        else:
                            print(f"Ошибка ввода, попробуйте еще раз")
                    maty = Metal(namenew, pricenew, sideanew, sidebnew, thicknessnew, lengthnew)
                    profilemetls.append(maty)
                    save()
                    break
                else:
                    print(f"Ошибка ввода, попробуйте еще раз")
            elif menumet == 4:
                break
            else:
                print(f"Ошибка ввода, попробуйте еще раз")

    elif menu == 4:
        print(f"Список выполненных расчетов ванн: ")
        print(f"-" * 40)
        for i, result in enumerate(resultvan, 1):
            print(f"{i}. {result[0]}, {result[1]}, {result[2]} \n")
        print(f"-" * 40)
        print(f"Меню: \n\t 1. Выход\n\t 2. Очистить список")
        menu3 = checkint(input("Введите позицию: "))
        if menu3 == 1:
            pass
        elif menu3 == 2:
            menu4 = input("Данные будут удалены безвозвратно, если вы уверены введите '0', если нет любой символ: ")
            if menu4 == "0":
                resultvan = []
                resultvanfile = open("resultvan.dat", "wb")
                pickle.dump(resultvan, resultvanfile)
                resultvanfile.close()

            else:
                pass
        else:
            print(f"Ошибка ввода, попробуйте еще раз")

    elif menu == 5:
        break
    else:
        print(f"ошибка ввода")