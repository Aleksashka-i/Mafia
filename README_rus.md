# Service-Oriented Architectures Homework

## Описание
В данном репозитории gRPC веб-сервис **«SOA-мафия»** (практика 2), клиент-серверный чат для пользователей игры с помощью системы очередей сообщений RabbitMQ (практика 3) и REST веб-сервис для сбора и предоставление клиентам возможностей работы с ресурсами игры «SOA-мафия» (практика 4).

## Конфигурация
Для запуска сервера gRPC, сервера REST и RabbitMQ нужно выполнить следующую команду.
```
docker-compose up
```
После того, как все сервера были запущены нужно запустить **4 клиента** в разных окнах терминала:
```
python3 client.py
```
Каждому клиенту будет предложено ввести юзернейм и выбрать между ```start session```, ```join session```. Один из клиентов должен выбрать ```start session```, определить кол-во игроков (по дефолту 4, но можно ввести больше, но тогда и окон терминалов нужно) и ввести ```session_id```. Все остальные игроки соответственно должны будут ввести данный ```session_id```.

<details>
  <summary><b>Примечание</b></summary>
Возможно потребуется установить локально зависимости для клиентов: <code>grpcio</code>, <code>pika</code>, <code>protobuf</code>, <code>tk</code>.
В целом это можно сделать с помощью <code>pip install -r requirements.txt</code>.
Единственное с чем могут возникнуть сложности это <code>tkinter</code>. <code>Tkinter</code> нужен для минимального графического интерфейса в чате, чтобы можно было сообщения отправлять.
</details>

## Как играть?
После того, как все игроки добавяться в сессию автоматически запуститься игра. Все игроки — боты, т.к. в условии вроде явно не требуется добавление ручного управления. Понятно, что его не сложно добавить в текущую имплементация. Игра запуститься, сразу начнётся ночь, так как в первый день ничего не происходит.

### Ночь
Далее мафии (в случае 4 игроков она одна) будет предложено "початиться". При выборе ```YES``` откроется маленькое окно. В него можно набирать сообщени и отправлять с помощью кнопки ```send```. Сообщения будут появляться в чате. Как уже ранее упомяналось чат реализован с помощью брокера сообщений ```RabbitMQ```. При закрытии графического интерфейса чат завершается. На данном шаге (с 4 игроками) можно выбрать ```NO```, так как мафия всего одна, но можно зайти посмотреть, что сообщения будут выводиться только в консоль мафии.

Комиссар (```Detective```) рандомно проверяет из ещё живых игроков (за исключением себя) и рандомно решает хочет ли он опубликовать данные, если определил Мафию. 

После закрытия чата мафия сделает "свой выбор" — любой игрок кроме себя (если мафий несколько, то жертву будут выбирать рандомно, что технически означает, что мафия может убить мафию, но что уж поделать). Мафиия и Комиссар отсылают на сервер сообщения, что для них ночь завершена. После получения сообщения от всех бодрствующих сервер отправляет всем собобщение о том, что день завершился.

### День
Игроку убитому этой ночью отправляется сообщение, о том, что он превратился в духа. Далее этот игрок будет получать только сообщения о том, за кого игроки проголосовали днём и кого убили ночью (т.е. приведение продолжает следить за ходом игры). Днём каждому ещё живому игроку тоже будет предложено "початиться". Для проверки можно выбрать двоих и посмотреть, что сообщения приходят только тем, кто сейчас в чатике (в папке ```pics``` есть картинка-пример того, как должна выглядеть мини-интерфейс мини-чата).

Игра продолжается до тех пор, пока мафий не станет 0 (**CIVILIANS WON**), или их не станет столько же, сколько игроков (**MAFIA WON**).

<details>
<summary><b>Пример консоли мафии + чат после 1 ночи </b></summary>
  <pre>
    Enter your username: W
    Enter your session id: 1
    --------> You joined session "1". Waiting for players to join.
    --------> Q joined session "1".
    --------> W joined session "1".
    --------> E joined session "1".
    --------> R joined session "1".

    -------------------------------------------------
    All players has joined session "1".

    Let's start the game. Your role: MAFIA.
    -------------------------------------------------

    ------------------------------------------------- NIGHT 1
    ☆ The city goes into the night. ☆
    ☆ You will not see in windows light. ☆

    ✝ Killers have no time for sleep. ✝
    ✝ Tell us, who's the slaughtered sheep? ✝

    Vote for player to be killed. Your options: "Q", "E", "R"
    You voted for "R" murder.
    -------------------------------------------------  NIGHT 1

    ------------------------------------------------- DAY 1
    ☆ The city rises from its slumber. ☆
    ☆ What happened through the night, we wonder. ☆

    "R" was killed last night. They were a DETECTIVE.
    Start listening

    [W] Hi!

    [Q] How are you?

    [W] I had a weird dream...

    [Q] Hm, wanna share?

    [W] Sorry, have to run, bye!


    Vote for player to be eliminated. Your options: "Q", "E", or skip the vote.
    You voted for "Q" elimination.


    "Q" was voted out. They were a CIVILLIAN.
    ALIVE: ['W', 'E']
    GHOSTS: ['R', 'Q']
    ------------------------------------------------- DAY 1


    -------------------------------------------------
    ☆ For now, my friends, the chaos wins. ☆
    ☆ The mafia triumphant kings! ☆
    ☆ MAFIA WON ☆
    -------------------------------------------------
  </pre>
</details>
  
## REST API
REST сервис реализован с помощью Flask и Sqlite базы данных.

Вывод информации обо всех пользователях игры (текущий запуск сервера)
```
curl --location --request GET 'http://127.0.0.1:57015/api/players' --header 'Content-Type:application/json'  | python3 -m json.tool
```
Вывод информации об одном игроке по username'у:
```
curl --location --request GET 'http://127.0.0.1:57015/api/players/{username}' --header 'Content-Type:application/json' | python3 -m json.tool
```
Добавление пользователя в базу данных. Можно указать ```name: str```, ```gender: str```, ```email: str```, ```avatar: str```, ```games: int```, ```wins: int```, ```time_in_game: int```:
```
curl --location --request POST 'http://127.0.0.1:57015/api/players/insert' --header 'Content-Type:application/json' --data-raw '{"name": "new_player"}' | python3 -m json.tool
```
Обновление данных о пользователе:
```
curl --location --request PUT 'http://127.0.0.1:57015/api/players/update' --header 'Content-Type:application/json' --data-raw '{"name": "new_player", "email": "new_player@gmail.com"}' | python3 -m json.tool
```
Загрузка картинки (по дефолту default.jpg из rest/images):
```
curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@/Users/{name}/new_player.jpg" http://127.0.0.1:57015/api/players/images/new_player
```
Статистика генерируется по асинхронному запросу (с помощью rabbitMQ) по запросу, пдфка генерируется с помощью ```reportlab``` в папке ```pics``` есть картинка-пример того, как должна выглядеть пдфка статистики):
```
curl --location --request POST 'http://127.0.0.1:57015/api/players/statistics/new_player' --header 'Content-Type:application/json'
```
Удаление пользователя:
```
curl --location --request DELETE 'http://127.0.0.1:57015/api/players/delete/new_player' --header 'Content-Type:application/json' | python3 -m json.tool
```
## Итого
По моим подсчётам я полностью выполнила практику №2, №3 и №4.
