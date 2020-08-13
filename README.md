
# Архитектура 

В основе проекта лежит идея хранения в хэш таблице адреса к данным.
Адрес - это диапазон, в котором находятся данные, в байтах от начала файла, в котором они хранятся. (ключ: [адрес начала данных, адрес конца данных])
Hash table

| Key  |   address(bytes)  |
|------|:-----------------:|
| key1 |  [1010, 323324]   |
| key2 |    [12, 4343]     |
| key3 |    [10, 11]       |


![alt text](https://github.com/vladkiriyak/nimble_test/blob/master/presentation_sorce/photo_2020-08-12_20-51-41.jpg?raw=true)


Нода держит хэш таблицу в оперативной памяти, данные пишет в файл. Когда файл превышает определенный размер он и хэш таблица заливаются на AWS S3.

Когда приходит GET запрос надо смотрит есть ли ключ в временном локальном файле, если нет то смотрит в файлах на S3. Смотрит она в хэш таблицах в оперативной памяти, а если ключ имеется, то она делает запрос к файлам на S3, передавай адрес в файле в байтах.


## Как устроено масштабирование?
![alt text](https://github.com/vladkiriyak/nimble_test/blob/master/presentation_sorce/photo_2020-08-12_20-56-34.jpg?raw=true)

Допустим появляется ещё один инстанс ноды. До этого момента все запросы шли в контроллер, а тот опрашивал ноду на наличие ключа. Теперь запрос идет в контроллер, от ключа берется хэш, запросы хэш ключа которых меньше макс.знач.ключа/2 идут на одну ноду, а которые больше на другую ноду.
Это работает для PUT запросов, но для GET нет, так как пока была одна нода все значения записывались в нее и никаких разделений не было. Для того чтобы это решить, сервер проходится по всем ключам и копирует данные на новую ноду, хэш ключа которых больше половины максимального. А пока этот процесс происходит все GET запросы приходят на обе ноды. Данные именно копируются, а не перебрасываются, что повышает отказоустойчивость. Если одна из нод упадет, то запрос редиректится к всем остальным.

![alt text](https://github.com/vladkiriyak/nimble_test/blob/master/presentation_sorce/photo_2020-08-12_22-01-20.jpg?raw=true)






