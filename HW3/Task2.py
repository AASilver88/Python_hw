# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.


from re import findall
from collections import Counter


def ten_most_common_words(_text: str) -> list[tuple]:

    _PATTERN = r'\b\w+\b'
    _words = findall(_PATTERN, _text.lower())

    _TEN_WORDS = 10

    return Counter(_words).most_common(_TEN_WORDS)


TEXT = """List, список является самой часто используемой коллекцией в Python. Прежде чем
говорить о списках, я напомню, что такое массив в информатике. Массив - это
непрерывная область в оперативной памяти компьютера, поделённая на ячейки
одинакового размера хранящие данные одного типа. Массивы могут быть
статическими, то есть размер массива нельзя изменить, и динамическими, когда
размер массива изменяется при добавлении или удалении элементов. Один из
самых больших плюсов в работе с массивами — это доступ к любой из его ячеек за
константное время.
Массив — упорядоченный набор элементов, каждый из которых хранит одно
значение, идентифицируемое с помощью одного или нескольких индексов. В
простейшем случае массив имеет постоянную длину и хранит единицы данных
одного и того же типа, а в качестве индексов выступают целые числа.
В информатике, список (англ. list) — это абстрактный тип данных, представляющий
собой упорядоченный набор значений, в котором некоторое значение может
встречаться более одного раза. Экземпляр списка является компьютерной
реализацией математического понятия конечной последовательности. Экземпляры
значений, находящихся в списке, называются элементами списка (англ. item, entry
либо element); если значение встречается несколько раз, каждое вхождение
считается отдельным элементом.
При работе со списками важно помнить, что сам список как хранитель указателей
на объекты занимает место в памяти. Дополнительно занимают память и сами
объекты, на которые список указывает. Создание копии приводит к новым затратам
памяти, ведь мы создаём новый объект список. Если вы работает с большими
данными, создание копии может быть не лучшей идеей - может не хватить памяти
ПК. Кроме того каждая копия требует временных ресурсов на копирование. Прежде
чем использовать срезы, копии задумайтесь можно ли решить задачу иначе,
экономя время и память.
С другой стороны небольшие списки быстро копируются. И если в вашей задаче
важно сохранить оригинал, но нужно модифицировать список для получения
результата — копирование вполне допустимо."""

print(ten_most_common_words(TEXT))