import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import json

all_players = []

sess = {}
RUNA_ID = 202706139
RUNA_TOKEN = 'b0d92af4223aaa0659a63f7638e34804ad1db6784be516c3e446571ed55b94b31c7d6cfad129f7cbd2454'
with open("moneys.json", "r", encoding='utf8') as re:
    mmm = json.load(re)
    moneys = {}
    for i in mmm:
        moneys[int(i)] = mmm[i]
with open("names0.json", "r", encoding='utf8') as re:
    nnn = json.load(re)
    names = {}
    for i in nnn:
        names[int(i)] = nnn[i]
with open("keys.json", "r", encoding='utf8') as re:
    keys = json.load(re)
with open("names1.json", "r", encoding='utf8') as re:
    names1 = json.load(re)

name = 'руна'


class perudo():
    def __init__(self):
        with open("keys_perudo.json", "r", encoding='utf8') as re:
            self.keys = json.load(re)
        self.move_player = 0
        self.count = 0
        self.nominal = 0
        self.is_maputo = False
        self.fase = 0
        self.vab, self.players_0, self.cubes_of_players, self.steps = [], [], [], []
        self.rules = 'пу пу пу чекните правила в википедии по запросу "перудо"'
        self.hello = 'Океей! А теперь начинаем нашу игру в пиратские кости!'
        self.chat_of_game = event.obj.message['peer_id']
        self.players = []
        self.lol = []
        self.variants1 = 'единица единицы единиц'
        self.variants2 = 'двойка двойки двоек'
        self.variants3 = 'тройка тройки троек'
        self.variants4 = 'четверка четверки четверок'
        self.variants5 = 'пятерка пятерки пятерок'
        self.variants6 = 'шестерка шестерки шестерок'
        vk.messages.send(
            peer_id=self.chat_of_game,
            message=f'''Все участники игры должны написать в чат "{self.keys["im_player"]}"
        Когда будете готовы начать, напишите "{self.keys["game_start"]}"''',
            random_id=random.randint(0, 2 ** 64))

    def move(self, event):
        t = event.obj.message['text']
        if self.fase == -1:
            vk.messages.send(
                peer_id=event.obj.message['peer_id'],
                message=f'Игра уже закончилась, используйте код резкого окончания',
                random_id=random.randint(0, 2 ** 64))
        if self.keys['im_player'] == t.lower():
            if self.fase == 0:
                i = event.obj.message['from_id']
                if i in all_players:
                    vk.messages.send(
                        peer_id=i,
                        message=f'Вы уже принимаете участие в игре в другом чате.',
                        random_id=random.randint(0, 2 ** 64))
                    return
                if i not in self.players and len(self.players) < 10:
                    if i not in names:
                        if i in self.lol:
                            vk.messages.send(
                                peer_id=i,
                                message='Руна рада приветствовать Вас! Вы еще не играли с нами? У Вас сейчас 1000 фишек'
                                        ', которые вы можете тратить в различных играх) Если Вы проиграетесь, Вы можете'
                                        ' попросить другого игрока перевести Вам деньги командой "перевод [ИМЯ] [ФАМИЛИ'
                                        'Я] [ЧИСЛО ФИШЕК]. Переводить деньги можно в любое время, даже на середине раун'
                                        'да! Удачных игр!',
                                random_id=random.randint(0, 2 ** 64))
                            self.lol.remove(i)
                            response = vk.users.get(user_ids=i)
                            first_name = response[0]['first_name']
                            second_name = response[0]['last_name']
                            names[i] = first_name + ' ' + second_name
                            names1[(first_name + ' ' + second_name).lower()] = i
                            with open("names0.json", "w") as wr:
                                json.dump(names, wr)
                            with open("names1.json", "w") as wr:
                                json.dump(names1, wr)
                            moneys[i] = 1000
                            with open("moneys.json", "w") as wr:
                                json.dump(moneys, wr)
                        else:
                            vk.messages.send(
                                peer_id=event.obj.message['peer_id'],
                                message=f'Напишите что-нибудь мне в ЛС (чтобы я могла писать Вам Ваши кубы), после чего попробуйте написать "участвую" снова',
                                random_id=random.randint(0, 2 ** 64))
                            self.lol.append(i)
                            return
                    else:
                        vk.messages.send(
                            peer_id=i,
                            message=f'Вы участник! Начинайте игру или ожидайте остальных игроков.',
                            random_id=random.randint(0, 2 ** 64))
                    self.players.append(i)
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message='Игрок ' + names[i] + ' присоединился к игре.',
                        random_id=random.randint(0, 2 ** 64))
                    if len(self.players) == 6:
                        s1 = 'Количество игроков достигло максимума (6), теперь вы можете лишь начать'
                        vk.messages.send(
                            peer_id=self.chat_of_game,
                            message=s1 + ' игру командой "старт".',
                            random_id=random.randint(0, 2 ** 64))
                    all_players.append(i)
                    sess[self.chat_of_game][2].append(i)
        elif self.keys['rule'] == t.lower():
            vk.messages.send(
                peer_id=self.chat_of_game,
                message=self.rules,
                random_id=random.randint(0, 2 ** 64))
        elif self.keys['game_start'] == t.lower():
            if self.fase == 0:
                if event.obj.message['from_id'] not in self.players:
                    return
                if len(self.players) == 1:
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message='Нельзя начать игру в одиночку.',
                        random_id=random.randint(0, 2 ** 64))
                    return
                self.fase = 1
                random.shuffle(self.players)
                self.players_0 = self.players[:]
                self.cubes_of_players = {}
                self.count_of_cubes = {}
                for i in self.players:
                    cubes = [random.randint(1, 6) for i in range(5)]
                    vk.messages.send(
                        peer_id=i,
                        message='Ваши кубы: ' + ', '.join([str(x) for x in cubes]) + '.',
                        random_id=random.randint(0, 2 ** 64))
                    self.cubes_of_players[i] = cubes
                    self.count_of_cubes[i] = 5
                vk.messages.send(
                    peer_id=self.chat_of_game,
                    message=self.hello,
                    random_id=random.randint(0, 2 ** 64))
                self.steps = [names[i] for i in self.players]
                x = "\n* ".join(self.steps)
                vk.messages.send(
                    peer_id=self.chat_of_game,
                    message=f'Порядок ходов:\n* {x}',
                    random_id=random.randint(0, 2 ** 64))
                self.move_player = 0
                self.count = 0
                self.nominal = 0
                self.is_maputo = False
                vk.messages.send(
                    peer_id=self.chat_of_game,
                    message=f'Первый ход игрока {self.steps[self.move_player]}. Напишите свою ставку в чат в формате "ставка [количество(числом)] [номинал]" (например, "ставка 2 тройки")',
                    random_id=random.randint(0, 2 ** 64))
        elif self.keys['info_game'] == t.lower():
            if self.fase == -1:
                vk.messages.send(
                    peer_id=event.obj.message['peer_id'],
                    message=f'Игра не начата ("руна перудо" для старта)',
                    random_id=random.randint(0, 2 ** 64))
            elif self.fase == 0:
                s = "диниться)\nУже присоединившиеся:\n"
                for i in self.players:
                    s += f'* {names[i]}\n'
                vk.messages.send(
                    peer_id=event.obj.message['peer_id'],
                    message=f'Идет набор игроков ("старт" для начала игры, "участвую" в чат, чтобы присое' + s,
                    random_id=random.randint(0, 2 ** 64))
            elif self.fase == 1:
                vk.messages.send(
                    peer_id=event.obj.message['peer_id'],
                    message=f'Идет игра! Ход игрока {names[self.players[self.move_player]]}. Число кубов на столе: {sum([i for i in self.count_of_cubes.values()])}.',
                    random_id=random.randint(0, 2 ** 64))
        elif self.keys['cubes'] in t.lower():
            if self.keys['cubes'] == t.lower().split()[0]:
                if self.fase == 1:
                    i = event.obj.message['from_id']
                    if i != self.players[self.move_player]:
                        return
                    if len(t.split()) != 3:
                        return
                    count, nominal = t.split()[1:]
                    if not count.isdigit():
                        vk.messages.send(
                            peer_id=i,
                            message=f'Количество кубов должно быть числом.',
                            random_id=random.randint(0, 2 ** 64))
                        return
                    count = int(count)
                    if nominal not in self.variants1 + self.variants2 + self.variants3 + self.variants4 + self.variants5 + self.variants6:
                        vk.messages.send(
                            peer_id=i,
                            message=f'Я не знаю такого номинала кубов. Проверьте, возможно Вы ошиблись.',
                            random_id=random.randint(0, 2 ** 64))
                        return
                    else:
                        if nominal in self.variants1:
                            nominal = 1
                        elif nominal in self.variants2:
                            nominal = 2
                        elif nominal in self.variants3:
                            nominal = 3
                        elif nominal in self.variants4:
                            nominal = 4
                        elif nominal in self.variants5:
                            nominal = 5
                        elif nominal in self.variants6:
                            nominal = 6
                    if not self.is_maputo:
                        if self.nominal == 0:
                            if nominal == 1:
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Нельзя начинать игру с единиц.',
                                    random_id=random.randint(0, 2 ** 64))
                                return
                            self.count = count
                            self.nominal = nominal
                            self.move_player = (self.move_player + 1) % len(self.players)
                            vk.messages.send(
                                peer_id=self.chat_of_game,
                                message=f'Ход игрока {self.steps[self.move_player]}.',
                                random_id=random.randint(0, 2 ** 64))
                            return
                        if count < self.count and nominal != 1:
                            if self.nominal == 1:
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Нельзя понижать число кубов.',
                                    random_id=random.randint(0, 2 ** 64))
                            else:
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Нельзя понижать число кубов (если не уходишь в единицы).',
                                    random_id=random.randint(0, 2 ** 64))
                            return
                        if count <= self.count and nominal == 1:
                            if count != self.count // 2 + int(bool(self.count % 2)):
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Когда уходишь в единицы, число кубов становится в два раза меньше (с округлением в большую сторону).',
                                    random_id=random.randint(0, 2 ** 64))
                                return
                            else:
                                self.count = count
                                self.nominal = nominal
                                self.move_player = (self.move_player + 1) % len(self.players)
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Ход игрока {self.steps[self.move_player]}.',
                                    random_id=random.randint(0, 2 ** 64))
                                return
                        if count == self.count:
                            if nominal < self.nominal:
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Нельзя понижать номинал, если не увеличиваешь количество.',
                                    random_id=random.randint(0, 2 ** 64))
                                return
                            elif nominal == self.nominal:
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Это же просто дублирование ставки прошлого игрока, так нельзя)',
                                    random_id=random.randint(0, 2 ** 64))
                                return
                            else:
                                self.count = count
                                self.nominal = nominal
                                self.move_player = (self.move_player + 1) % len(self.players)
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Ход игрока {self.steps[self.move_player]}.',
                                    random_id=random.randint(0, 2 ** 64))
                                return
                        if count > self.count and self.nominal == 1 and nominal == 1:
                            self.count = count
                            self.nominal = nominal
                            self.move_player = (self.move_player + 1) % len(self.players)
                            vk.messages.send(
                                peer_id=self.chat_of_game,
                                message=f'Ход игрока {self.steps[self.move_player]}.',
                                random_id=random.randint(0, 2 ** 64))
                            return
                        if count > self.count and self.nominal == 1 and nominal != 1:
                            if count != self.count * 2 + 1:
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Когда выходишь из единиц, число кубов становится в два раза больше плюс один.',
                                    random_id=random.randint(0, 2 ** 64))
                                return
                            else:
                                self.count = count
                                self.nominal = nominal
                                self.move_player = (self.move_player + 1) % len(self.players)
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Ход игрока {self.steps[self.move_player]}.',
                                    random_id=random.randint(0, 2 ** 64))
                                return
                        if count > self.count and self.nominal != 1 and nominal == 1:
                            vk.messages.send(
                                peer_id=self.chat_of_game,
                                message=f'В единицы можно уйти, лишь уменьшив число кубов.',
                                random_id=random.randint(0, 2 ** 64))
                            return
                        elif count > self.count and self.nominal != 1 and nominal != 1:
                            self.count = count
                            self.nominal = nominal
                            self.move_player = (self.move_player + 1) % len(self.players)
                            vk.messages.send(
                                peer_id=self.chat_of_game,
                                message=f'Ход игрока {self.steps[self.move_player]}.',
                                random_id=random.randint(0, 2 ** 64))
                            return
                    else:
                        if self.nominal == 0:
                            self.count = count
                            self.nominal = nominal
                            self.move_player = (self.move_player + 1) % len(self.players)
                            vk.messages.send(
                                peer_id=self.chat_of_game,
                                message=f'Ход игрока {self.steps[self.move_player]}.',
                                random_id=random.randint(0, 2 ** 64))
                            return
                        if count < self.count:
                            vk.messages.send(
                                peer_id=self.chat_of_game,
                                message=f'Во время Мапуто нельзя понижать число кубов никаким образом.',
                                random_id=random.randint(0, 2 ** 64))
                            return
                        if count == self.count:
                            if nominal < self.nominal:
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Нельзя понижать номинал.',
                                    random_id=random.randint(0, 2 ** 64))
                                return
                            elif nominal == self.nominal:
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Это же просто дублирование ставки прошлого игрока, так нельзя)',
                                    random_id=random.randint(0, 2 ** 64))
                                return
                            else:
                                self.count = count
                                self.nominal = nominal
                                self.move_player = (self.move_player + 1) % len(self.players)
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Ход игрока {self.steps[self.move_player]}.',
                                    random_id=random.randint(0, 2 ** 64))
                                return
                        if count > self.count:
                            if nominal < self.nominal:
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Во время Мапуто нельзя понижать номинал даже при увеличении количества.',
                                    random_id=random.randint(0, 2 ** 64))
                                return
                            else:
                                self.count = count
                                self.nominal = nominal
                                self.move_player = (self.move_player + 1) % len(self.players)
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Ход игрока {self.steps[self.move_player]}.',
                                    random_id=random.randint(0, 2 ** 64))
        elif self.keys['lie'] == t.lower():
            if self.fase == 1:
                i = event.obj.message['from_id']
                if i != self.players[self.move_player]:
                    return
                if self.nominal == 0:
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'Ваш ход первый, кому Вы собираетесь не верить? Делайте ставку.',
                        random_id=random.randint(0, 2 ** 64))
                    return
                coco = 0
                s = 'Кубы всех игроков:\n'
                for j in self.players:
                    s += f'{names[j]}: {", ".join([str(x) for x in self.cubes_of_players[j]])};\n'
                    for k in self.cubes_of_players[j]:
                        if (not self.is_maputo and k == 1) or k == self.nominal:
                            coco += 1
                if self.is_maputo:
                    self.is_maputo = False
                vk.messages.send(
                    peer_id=self.chat_of_game,
                    message=s,
                    random_id=random.randint(0, 2 ** 64))
                if coco < self.count:
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'На столе лишь {coco} кубов этого номинала. Вы оказались правы! Предыдущий игрок сбрасывает куб.',
                        random_id=random.randint(0, 2 ** 64))
                    self.move_player -= 1
                    if self.move_player == -1:
                        self.move_player = len(self.players) - 1
                else:
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'На столе целых {coco} кубов этого номинала! Вы ошиблись и лишаетесь одного куба.',
                        random_id=random.randint(0, 2 ** 64))
                mo = self.move_player
                imo = names1[self.steps[mo].lower()]
                self.count_of_cubes[imo] -= 1
                if self.count_of_cubes[imo] == 1:
                    self.is_maputo = True
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'У одного из игроков остался один куб. Объявляется специальный раунд МАПУТО!!!',
                        random_id=random.randint(0, 2 ** 64))
                if self.count_of_cubes[imo] == 0:
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'У игрока {self.steps[mo]} не осталось кубов. Он выбывает(',
                        random_id=random.randint(0, 2 ** 64))
                    self.steps.remove(names[imo])
                    self.players.remove(imo)
                    if self.move_player == len(self.players):
                        self.move_player = 0
                    if len(self.players) == 1:
                        vk.messages.send(
                            peer_id=self.chat_of_game,
                            message=f'Остался лишь один игрок с кубами! Побеждает {names[self.players[0]]}! Игра окончена. Введите код резкого окончания игры.',
                            random_id=random.randint(0, 2 ** 64))
                        self.fase = -1
                        return
                for i in self.players:
                    cubes = [random.randint(1, 6) for i in range(self.count_of_cubes[i])]
                    vk.messages.send(
                        peer_id=i,
                        message='Ваши кубы: ' + ', '.join([str(x) for x in cubes]) + '.',
                        random_id=random.randint(0, 2 ** 64))
                    self.cubes_of_players[i] = cubes
                self.count = 0
                self.nominal = 0
                vk.messages.send(
                    peer_id=self.chat_of_game,
                    message=f'Ход игрока {self.steps[self.move_player]}.',
                    random_id=random.randint(0, 2 ** 64))


class kakegurui():
    def __init__(self):
        with open("keys_kakegurui.json", "r", encoding='utf8') as re:
            self.keys = json.load(re)
        self.fase = 0
        self.name_of_game = 'kakegurui'
        self.big_st, self.summ, self.nuls, self.move_player, self.chat_of_game = 0, 0, 0, 0, 0
        self.last_st = {}
        self.vab, self.dolgers, self.bank, self.players_0, self.cards_of_players, self.steps = [], [], [], [], [], []
        self.rules = '''Ну что, приступим! В игре используются четыре карты: 0, 1, 2, 3, по десять карт каждого типа. Игрокам раздается по четыре карты. По очереди каждый играет по одной карте. Если карта игрока дает общую сумму больше заданной, он выбывает. Просто же? Чтобы игра не зависела только от удачи, вы будете делать ставки, как в покере. Даже если на руках плохие карты, можно заставить противника сдаться. Мы будем играть, пока не останется единственный не-банкрот. Фишки проигравшего уйдут к оставшимся участникам в игре.'''
        self.hello = 'Океей! А теперь начинаем нашу игру "По нулям"! Делайте ваши ставки, начальная сумма ставки - 10 ф'
        self.hello += f'ишек. Если хотите сделать ставку, напишите в чат "{self.keys["reiz"]} [число]".'
        self.chat_of_game = event.obj.message['peer_id']
        self.players = []
        self.lol = []
        vk.messages.send(
            peer_id=self.chat_of_game,
            message=f'''Все участники игры должны написать в чат "{self.keys["im_player"]}"
        Когда будете готовы начать, напишите "{self.keys["game_start"]}"''',
            random_id=random.randint(0, 2 ** 64))

    def new_cards(self):
        x = ['0' for _ in range(10)] + ['1' for _ in range(10)] + ['2' for _ in range(10)] + ['3' for _ in range(10)]
        random.shuffle(x)
        return x

    def move(self, event):
        t = event.obj.message['text']
        if self.fase == -1:
            vk.messages.send(
                peer_id=event.obj.message['peer_id'],
                message=f'Игра уже закончилась, используйте код резкого окончания',
                random_id=random.randint(0, 2 ** 64))
        if self.keys['im_player'] == t.lower():
            if self.fase == 0:
                i = event.obj.message['from_id']
                if i in all_players:
                    vk.messages.send(
                        peer_id=i,
                        message=f'Вы уже принимаете участие в игре в другом чате.',
                        random_id=random.randint(0, 2 ** 64))
                    return
                if i not in self.players and len(self.players) < 10:
                    if i not in names:
                        if i in self.lol:
                            vk.messages.send(
                                peer_id=i,
                                message='Руна рада приветствовать Вас! Вы еще не играли с нами? У Вас сейчас 1000 фишек,'
                                        ' постарайтесь не проиграть всё в первых же играх) Если Вы всё же проиграетесь, Вы можете попросить другого игрока перевести Вам деньги командой "перевод [ИМЯ] [ФАМИЛИЯ] [ЧИСЛО ФИШЕК]. Переводить деньги можно в любое время, даже на середине раунда! Удачных игр!',
                                random_id=random.randint(0, 2 ** 64))
                            self.lol.remove(i)
                            response = vk.users.get(user_ids=i)
                            first_name = response[0]['first_name']
                            second_name = response[0]['last_name']
                            names[i] = first_name + ' ' + second_name
                            names1[(first_name + ' ' + second_name).lower()] = i
                            with open("names0.json", "w") as wr:
                                json.dump(names, wr)
                            with open("names1.json", "w") as wr:
                                json.dump(names1, wr)
                            moneys[i] = 1000
                            with open("moneys.json", "w") as wr:
                                json.dump(moneys, wr)
                        else:
                            vk.messages.send(
                                peer_id=event.obj.message['peer_id'],
                                message=f'Напишите что-нибудь мне в ЛС (чтобы я могла писать Вам Ваши карты), после чего попробуйте написать "участвую" снова',
                                random_id=random.randint(0, 2 ** 64))
                            self.lol.append(i)
                            return
                    else:
                        vk.messages.send(
                            peer_id=i,
                            message=f'Вы участник! Начинайте игру или ожидайте остальных игроков.',
                            random_id=random.randint(0, 2 ** 64))
                    self.players.append(i)
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message='Игрок ' + names[i] + ' присоединился к игре.',
                        random_id=random.randint(0, 2 ** 64))
                    if len(self.players) == 10:
                        s1 = 'Количество игроков достигло максимума (10), теперь вы можете лишь начать'
                        vk.messages.send(
                            peer_id=self.chat_of_game,
                            message=s1 + ' игру командой "старт".',
                            random_id=random.randint(0, 2 ** 64))
                    if moneys[i] <= 0:
                        vk.messages.send(
                            peer_id=i,
                            message=f'Сначала найди денег, а потом уже играй. Можешь попросить кого-то перевести их тебе.',
                            random_id=random.randint(0, 2 ** 64))
                        return
                    all_players.append(i)
                    sess[self.chat_of_game][2].append(i)
        elif self.keys['game_start'] == t.lower():
            if self.fase == 0:
                if event.obj.message['from_id'] not in self.players:
                    return
                if len(self.players) == 1:
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message='Нельзя начать игру в одиночку.',
                        random_id=random.randint(0, 2 ** 64))
                    return
                self.fase = 1
                self.players_0 = self.players[:]
                cards = self.new_cards()
                self.cards_of_players = {}
                for i in self.players:
                    card = cards[:4]
                    vk.messages.send(
                        peer_id=i,
                        message='Ваши карты: ' + ', '.join(card) + '.',
                        random_id=random.randint(0, 2 ** 64))
                    self.cards_of_players[i] = card
                    del cards[:4]
                vk.messages.send(
                    peer_id=self.chat_of_game,
                    message=self.hello,
                    random_id=random.randint(0, 2 ** 64))
                self.dolgers = self.players[:]
                self.vab = []
                self.bank = 0
                self.last_st = {i: 10 for i in self.players}
                self.big_st = 10
        elif self.keys['rule'] == t.lower():
            vk.messages.send(
                peer_id=self.chat_of_game,
                message=self.rules,
                random_id=random.randint(0, 2 ** 64))
        elif self.keys['reiz'] in t.lower():
            if t.lower().split()[0] != self.keys['reiz']:
                return
            if self.fase == 1 or self.fase == 2:
                self.fase = 1
                i = event.obj.message['from_id']
                if i not in self.players:
                    return
                if len(t.split()) != 2:
                    return
                if self.big_st > moneys[i]:
                    s = 'Текущая ставка слишком велика для вас. Вы можете либо идти "ва-банк" (поставить все),'
                    s += ' либо сделать "пас" (выйти из игры и остаться ни с чем).'
                    vk.messages.send(
                        peer_id=i,
                        message=s,
                        random_id=random.randint(0, 2 ** 64))
                    return
                st = t.split()[1]
                if not st.isdigit():
                    vk.messages.send(
                        peer_id=i,
                        message=f'Ставка должна быть числом :)',
                        random_id=random.randint(0, 2 ** 64))
                    return
                st = int(st)
                if st <= self.big_st:
                    vk.messages.send(
                        peer_id=i,
                        message=f'Вы не можете поставить что-то меньшее, чем предложенная ставка.',
                        random_id=random.randint(0, 2 ** 64))
                    return
                if st == moneys[i]:
                    vk.messages.send(
                        peer_id=i,
                        message=f'Это называется "ва-банк", пожалуйста, напишите мне это.',
                        random_id=random.randint(0, 2 ** 64))
                    return
                if st > moneys[i]:
                    vk.messages.send(
                        peer_id=i,
                        message=f'У вас слишком мало денег, чтобы предлагать такую ставку.',
                        random_id=random.randint(0, 2 ** 64))
                    return
                self.big_st = st
                self.last_st[i] = st
                vk.messages.send(
                    peer_id=self.chat_of_game,
                    message=f'Игрок {names[i]} повышает ставку до {self.big_st}. Остальные должны либо "поддержать" ставку, либо сделать "пас" (выйти из игры и остаться ни с чем), либо сделать новую ставку (аналогично "ставка [число]").',
                    random_id=random.randint(0, 2 ** 64))
                self.dolgers = self.players[:]
                self.dolgers.remove(i)
                for i in self.vab:
                    self.dolgers.remove(i)
                if len(self.dolgers) == 0:
                    self.fase = 2
                    self.losters = []
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'Текущая ставка утверждена - {self.big_st}. Вы можете повысить ставку все той же командой "ставка [число]" или подтвердить готовность начать командой "потрачено".',
                        random_id=random.randint(0, 2 ** 64))
        elif self.keys['coll'] == t.lower():
            if self.fase == 1:
                i = event.obj.message['from_id']
                if i not in self.dolgers:
                    return
                if self.big_st >= moneys[i]:
                    vk.messages.send(
                        peer_id=i,
                        message=f'Текущая ставка слишком велика для вас. Вы можете либо идти "ва-банк" (поставить все), либо сделать "пас" (выйти из игры и остаться ни с чем).',
                        random_id=random.randint(0, 2 ** 64))
                    return
                self.last_st[i] = self.big_st
                vk.messages.send(
                    peer_id=self.chat_of_game,
                    message=f'Игрок {names[i]} поддерживает ставку.',
                    random_id=random.randint(0, 2 ** 64))
                self.dolgers.remove(i)
                if len(self.dolgers) == 0:
                    self.fase = 2
                    self.losters = []
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'Текущая ставка утверждена - {self.big_st}. Вы можете повысить ставку все той же командой "ставка [число]" или подтвердить готовность начать командой "потрачено".',
                        random_id=random.randint(0, 2 ** 64))
        elif self.keys['pas'] == t.lower():
            if self.fase == 1 or self.fase == 2:
                i = event.obj.message['from_id']
                if i not in self.players:
                    return
                if i in self.vab:
                    vk.messages.send(
                        peer_id=i,
                        message=f'Вы пошли ва-банк, так что уже не можете спасовать.',
                        random_id=random.randint(0, 2 ** 64))
                    return
                self.bank += self.last_st[i]
                moneys[i] -= self.last_st[i]
                with open("moneys.json", "w") as wr:
                    json.dump(moneys, wr)
                vk.messages.send(
                    peer_id=self.chat_of_game,
                    message=f'Игрок {names[i]} решил спасовать. Он не принимает участие в игре до следующего раунда, а его последняя ставка будет поделена между победителями.',
                    random_id=random.randint(0, 2 ** 64))
                if i in self.dolgers:
                    self.dolgers.remove(i)
                self.players.remove(i)
                self.last_st[i] = 0
                if len(self.players) == 1:
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'Все спасовали, кроме игрока {names[self.players[0]]}! Он выигрывает и получает {self.bank} фишек!',
                        random_id=random.randint(0, 2 ** 64))
                    moneys[self.players[0]] += self.bank
                    with open("moneys.json", "w") as wr:
                        json.dump(moneys, wr)
                    cards = self.new_cards()
                    self.dolgers = self.players[:]
                    self.players = self.players_0[:]
                    self.cards_of_players = {}
                    for i in self.players:
                        card = cards[:4]
                        vk.messages.send(
                            peer_id=i,
                            message='Ваши карты: ' + ', '.join(card) + '.',
                            random_id=random.randint(0, 2 ** 64))
                        self.cards_of_players[i] = card
                        del cards[:4]
                    dop = ''
                    self.vab = []
                    self.bank = 0
                    self.last_st = {i: 10 for i in self.players}
                    self.big_st = 10
                    self.fase = 1
                    for i in self.players:
                        dop += f'* {names[i]}: {moneys[i]}\n'
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'Новый раунд! Делайте свои ставки!\nЧисло фишек каждого участника:\n{dop}',
                        random_id=random.randint(0, 2 ** 64))
                    self.players = self.players[1:] + [self.players[0]]
                    self.move_player = 0
                    return
                if len(self.dolgers) == 0:
                    self.fase = 2
                    self.losters = []
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'Текущая ставка утверждена - {self.big_st}. Вы можете повысить ставку все той же командой "ставка [число]" или подтвердить готовность начать командой "потрачено".',
                        random_id=random.randint(0, 2 ** 64))
        elif self.keys['all-in'] == t.lower():
            if self.fase == 1 or self.fase == 2:
                i = event.obj.message['from_id']
                '''if i == 391780092 and self.big_st < moneys[i]:
                    vk.messages.send(
                        peer_id=i,
                        message=f'Викачбка пошла нафиг тебе нельзя вабанк.',
                        random_id=random.randint(0, 2 ** 64))
                    return'''
                self.vab.append(i)
                self.fase = 1
                dop = ''
                self.last_st[i] = moneys[i]
                if moneys[i] >= self.big_st:
                    self.big_st = moneys[i]
                    dop = f' Ставка становится равной {self.big_st}.'
                vk.messages.send(
                    peer_id=self.chat_of_game,
                    message=f'Игрок {names[i]} пошел ва-банк.' + dop,
                    random_id=random.randint(0, 2 ** 64))
                self.dolgers = []
                for i in self.players:
                    if i not in self.vab and self.last_st[i] < self.big_st:
                        self.dolgers.append(i)
                vk.messages.send(
                    peer_id=self.chat_of_game,
                    message=f'Все, чья ставка меньше {self.big_st} должны "поддержать" или сделать "пас".',
                    random_id=random.randint(0, 2 ** 64))
                if len(self.dolgers) == 0:
                    self.fase = 2
                    self.losters = []
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'Текущая ставка утверждена - {self.big_st}. Вы можете повысить ставку все той же командой "ставка [число]" или подтвердить готовность начать командой "потрачено".',
                        random_id=random.randint(0, 2 ** 64))
        elif self.keys['lost'] in t.lower():
            if t.lower().split()[0] != self.keys['lost']:
                return
            if self.fase == 2:
                i = event.obj.message['from_id']
                if i not in self.players:
                    return
                if i not in self.losters:
                    self.losters.append(i)
                else:
                    vk.messages.send(
                        peer_id=i,
                        message=f'Вы уже подтвердили свою готовность начать. Ожидайте остальных игроков или делайте новую ставку.',
                        random_id=random.randint(0, 2 ** 64))
                    return
                if len(self.losters) == len(self.players):
                    self.fase = 3
                    self.summ = 0
                    self.nuls = 0
                    for i in self.vab:
                        self.bank += moneys[i]
                    self.bank += self.big_st * (len(self.players) - len(self.vab))
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'Со ставками разобрались! Пора приступать к игре! Банк игры - {self.bank}. Для проигрыша необходимо выложить карту так, чтобы сумма на столе стала больше {(len(self.players) - 1) * 3}',
                        random_id=random.randint(0, 2 ** 64))
                    self.steps = [names[i] for i in self.players]
                    x = "\n* ".join(self.steps)
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'Порядок ходов:\n* {x}',
                        random_id=random.randint(0, 2 ** 64))
                    self.move_player = 0
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'Первый ход игрока {self.steps[self.move_player]}. Напишите свою карту в чат в формате "карта [число]"',
                        random_id=random.randint(0, 2 ** 64))
        elif self.keys['cart'] in t.lower():
            if self.keys['cart'] == t.lower().split()[0]:
                if self.fase == 3:
                    i = event.obj.message['from_id']
                    if i != self.players[self.move_player]:
                        return
                    if len(t.split()) != 2:
                        return
                    cart = t.split()[1]
                    if not cart.isdigit():
                        vk.messages.send(
                            peer_id=i,
                            message=f'Карта должна быть числом от 0 до 3.',
                            random_id=random.randint(0, 2 ** 64))
                        return
                    if cart not in self.cards_of_players[i]:
                        vk.messages.send(
                            peer_id=i,
                            message=f'У вас нет такой карты. Оставшиеся ваши карты - {", ".join(self.cards_of_players[i])}.',
                            random_id=random.randint(0, 2 ** 64))
                        return
                    self.cards_of_players[i].remove(cart)
                    cart = int(cart)
                    self.summ += cart
                    if not self.cards_of_players[i]:
                        self.nuls += 1
                    self.move_player = (self.move_player + 1) % len(self.players)
                    vk.messages.send(
                        peer_id=self.chat_of_game,
                        message=f'Игрок {names[i]} выложил карту {cart}. Общая сумма {self.summ}.',
                        random_id=random.randint(0, 2 ** 64))
                    if self.summ > (len(self.players) - 1) * 3:
                        dop = ''
                        if i in self.vab:
                            dop = f'Игрок {names[i]} поставил все и проиграл. Он обанкрочен :D\n'
                            self.players_0.remove(i)
                            self.last_st[i] = 0
                            if len(self.players_0) == 1:
                                moneys[self.players_0[0]] += moneys[i]
                                moneys[i] = 0
                                vk.messages.send(
                                    peer_id=self.chat_of_game,
                                    message=f'Выиграл игрок {names[self.players_0[0]]}!!! КОНЕЦ ИГРЫ.',
                                    random_id=random.randint(0, 2 ** 64))
                                self.fase = -1
                                return
                        self.players.remove(i)
                        self.last_st[i] = 0
                        moneys[i] -= self.big_st
                        dolz = self.bank // len(self.players)
                        dop += f'Каждый игрок, кроме спасовавших и проигравшего, получает ({dolz} минус его сумма ставки) фишек.'
                        for j in self.players:
                            moneys[j] += dolz - self.last_st[j]
                        with open("moneys.json", "w") as wr:
                            json.dump(moneys, wr)
                        vk.messages.send(
                            peer_id=self.chat_of_game,
                            message=f'Сумма на столе превысила максимальную, этот раунд окончен! ' + dop,
                            random_id=random.randint(0, 2 ** 64))
                        cards = self.new_cards()
                        random.shuffle(cards)
                        self.players = self.players_0[:]
                        self.cards_of_players = {}
                        for i in self.players:
                            card = cards[:4]
                            vk.messages.send(
                                peer_id=i,
                                message='Ваши карты: ' + ', '.join(card) + '.',
                                random_id=random.randint(0, 2 ** 64))
                            self.cards_of_players[i] = card
                            del cards[:4]
                        dop = ''
                        self.vab = []
                        self.bank = 0
                        self.last_st = {i: 10 for i in self.players}
                        self.big_st = 10
                        self.fase = 1
                        self.dolgers = self.players[:]
                        for i in self.players:
                            dop += f'* {names[i]}: {moneys[i]}\n'
                        vk.messages.send(
                            peer_id=self.chat_of_game,
                            message=f'Делайте свои ставки!\nЧисло фишек каждого участника:\n{dop}',
                            random_id=random.randint(0, 2 ** 64))
                        self.players_0 = self.players_0[1:] + [self.players_0[0]]
                    elif self.nuls == len(self.players):
                        dolz = self.bank // len(self.players) * len(self.players)
                        vk.messages.send(
                            peer_id=self.chat_of_game,
                            message=f'Ни у кого нет карт. Все, кроме спасовавших, получают свою долю ({dolz} - его сумма ставки) фишек.',
                            random_id=random.randint(0, 2 ** 64))
                        for j in self.players:
                            moneys[j] += dolz - self.last_st[j]
                        with open("moneys.json", "w") as wr:
                            json.dump(moneys, wr)
                        cards = self.new_cards()
                        random.shuffle(cards)
                        self.players = self.players_0[:]
                        self.cards_of_players = {}
                        for i in self.players:
                            card = cards[:4]
                            vk.messages.send(
                                peer_id=i,
                                message='Ваши карты: ' + ', '.join(card) + '.',
                                random_id=random.randint(0, 2 ** 64))
                            self.cards_of_players[i] = card
                            del cards[:4]
                        dop = ''
                        self.vab = []
                        self.bank = 0
                        self.last_st = {i: 10 for i in self.players}
                        self.big_st = 10
                        self.fase = 1
                        self.dolgers = self.players[:]
                        for i in self.players:
                            dop += f'* {names[i]}: {moneys[i]}\n'
                        vk.messages.send(
                            peer_id=self.chat_of_game,
                            message=f'Новый раунд! Делайте свои ставки!\nЧисло фишек каждого участника:\n{dop}',
                            random_id=random.randint(0, 2 ** 64))
                        self.players = self.players[1:] + [self.players[0]]
                    else:
                        vk.messages.send(
                            peer_id=self.chat_of_game,
                            message=f'Ход игрока {self.steps[self.move_player]}.',
                            random_id=random.randint(0, 2 ** 64))
        elif self.keys['info_me'] == t.lower():
            i = event.obj.message['from_id']
            if i not in names:
                vk.messages.send(
                    peer_id=event.obj.message['peer_id'],
                    message='Вы ни разу не играли, я ничего не знаю о вас',
                    random_id=random.randint(0, 2 ** 64))
            else:
                dop = ''
                if self.fase > 0:
                    if i in self.players_0 and i not in self.players:
                        dop = 'В этом раунде ты спасовал(а).'
                    elif i in self.players:
                        dop = f'В этом раунде твоя ставка {self.last_st[i]}.'
                vk.messages.send(
                    peer_id=event.obj.message['peer_id'],
                    message=f'{names[i]}, у тебя на счету {moneys[i]} монет. ' + dop,
                    random_id=random.randint(0, 2 ** 64))
        elif self.keys['info_game'] == t.lower():
            if self.fase == -1:
                vk.messages.send(
                    peer_id=event.obj.message['peer_id'],
                    message=f'Игра не начата ("руна по нулям" для старта)',
                    random_id=random.randint(0, 2 ** 64))
            elif self.fase == 0:
                s = "диниться)\nУже присоединившиеся:\n"
                for i in self.players:
                    s += f'* {names[i]}\n'
                vk.messages.send(
                    peer_id=event.obj.message['peer_id'],
                    message=f'Идет набор игроков ("старт" для начала игры, "участвую" в чат, чтобы присое' + s,
                    random_id=random.randint(0, 2 ** 64))
            elif self.fase == 1:
                s = "Текущие ставки:\n"
                for i in self.players:
                    s += f'* {names[i]} - {self.last_st[i]}\n'
                s += f'Все, чья ставка меньше {self.big_st}, должны написать мне в чат "поддержать" или'
                s += ' спасовать командой "пас". '
                vk.messages.send(
                    peer_id=event.obj.message['peer_id'],
                    message=f'Игрокам в ЛС высланы карты, делайте свои ставки командой "ставка [число]".\n' + s,
                    random_id=random.randint(0, 2 ** 64))
            elif self.fase == 2:
                s = ', должны написать в чат "потрачено". Также вы все ещё можете повысить ставку или спасовать.'
                s += '\nНе потратившиеся игроки:\n'
                for i in self.players:
                    if i not in self.losters:
                        s += f'* {names[i]}\n'
                vk.messages.send(
                    peer_id=event.obj.message['peer_id'],
                    message=f'Все участники этого раунда (не спасовавшие игроки), которые еще этого не сделали' + s,
                    random_id=random.randint(0, 2 ** 64))
            elif self.fase == 3:
                vk.messages.send(
                    peer_id=event.obj.message['peer_id'],
                    message=f'Идет игра! Ход игрока {names[self.players[self.move_player]]}.',
                    random_id=random.randint(0, 2 ** 64))


name_of_game = ''
vk_session = vk_api.VkApi(token=RUNA_TOKEN)
longpoll = VkBotLongPoll(vk_session, RUNA_ID)
for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        vk = vk_session.get_api()
        t = event.obj.message['text']
        if name == t.lower():
            vk.messages.send(
                peer_id=event.obj.message['peer_id'],
                message='я.',
                random_id=random.randint(0, 2 ** 64))
        elif t and t.split()[0].lower() == name:
            t = ' '.join(t.split()[1:])
            if keys['kakegurui'] == t.lower() and name_of_game == '':
                if event.obj.message['peer_id'] not in sess or sess[event.obj.message['peer_id']] == []:
                    key_stop_game = str(random.randint(1, 1000))
                    sess[event.obj.message['peer_id']] = [kakegurui(), key_stop_game, []]
                    vk.messages.send(
                        peer_id=event.obj.message['peer_id'],
                        message=f'Код для резкого окончания игры: {key_stop_game}',
                        random_id=random.randint(0, 2 ** 64))

            elif keys['perudo'] == t.lower() and name_of_game == '':
                if event.obj.message['peer_id'] not in sess or sess[event.obj.message['peer_id']] == []:
                    key_stop_game = str(random.randint(1, 1000))
                    sess[event.obj.message['peer_id']] = [perudo(), key_stop_game, []]
                    vk.messages.send(
                        peer_id=event.obj.message['peer_id'],
                        message=f'Код для резкого окончания игры: {key_stop_game}',
                        random_id=random.randint(0, 2 ** 64))

        elif keys['trade'] in t.lower():
            if t.lower().split()[0] != keys['trade']:
                continue
            i1 = event.obj.message['from_id']
            if i1 in names:
                t = t.split()
                i2_name = (' '.join(t[keys['trade'].count(' ') + 1:-1])).lower()
                if i2_name not in names1:
                    vk.messages.send(
                        peer_id=i1,
                        message='Это кто :\\\nЯ не знаю игрока, которому вы хотите перевести деньги (',
                        random_id=random.randint(0, 2 ** 64))
                    continue
                i2 = names1[i2_name]
                if i2 == i1:
                    vk.messages.send(
                        peer_id=i1,
                        message='Кринж чел',
                        random_id=random.randint(0, 2 ** 64))
                    continue
                try:
                    money_tr = int(t[-1])
                except ValueError:
                    vk.messages.send(
                        peer_id=i1,
                        message='Мне кажется это не цифра',
                        random_id=random.randint(0, 2 ** 64))
                    continue
                if money_tr <= 0 and i1 != 466260834:
                    vk.messages.send(
                        peer_id=i1,
                        message='А ты шутник)',
                        random_id=random.randint(0, 2 ** 64))
                    continue
                dop = ''
                if event.obj.message['peer_id'] in sess and sess[event.obj.message['peer_id']] != [] and \
                        sess[event.obj.message['peer_id']][0].name_of_game == 'kakegurui':
                    game = sess[event.obj.message['peer_id']][0]
                    if i1 not in game.last_st:
                        game.last_st[i1] = 0
                    if game.last_st[i1] != 0:
                        dop = ' Ты не можешь распоряжаться деньгами своей ставки, если что.'
                    xxx = moneys[i1] - game.last_st[i1]
                else:
                    xxx = moneys[i1]
                if xxx < money_tr:
                    vk.messages.send(
                        peer_id=i1,
                        message='У тебя даже денег столько нет :)' + dop,
                        random_id=random.randint(0, 2 ** 64))
                elif xxx == money_tr:
                    vk.messages.send(
                        peer_id=i1,
                        message='Вау щедрила отдаешь все деньги' + dop,
                        random_id=random.randint(0, 2 ** 64))
                    moneys[i1] -= xxx
                    moneys[i2] += xxx
                    vk.messages.send(
                        peer_id=i2,
                        message=f'Игрок {names[i1]} перевел тебе все свои деньги! {xxx} фишек зачислены на твой счет. '
                                f'Ваш баланс - {moneys[i2]}',
                        random_id=random.randint(0, 2 ** 64))
                else:
                    moneys[i1] -= money_tr
                    moneys[i2] += money_tr
                    vk.messages.send(
                        peer_id=i1,
                        message=f'Вы перевели {money_tr} игроку {names[i2]}. Ваш счёт - {moneys[i1]}.',
                        random_id=random.randint(0, 2 ** 64))
                    vk.messages.send(
                        peer_id=i2,
                        message=f'Игрок {names[i1]} перевел Вам {money_tr} фишек. Ваш счёт - {moneys[i2]}.',
                        random_id=random.randint(0, 2 ** 64))
                with open("moneys.json", "w") as wr:
                    json.dump(moneys, wr)
            else:
                vk.messages.send(
                    peer_id=i1,
                    message='Вам надо сыграть хотя бы одну игру, чтобы иметь баланс.',
                    random_id=random.randint(0, 2 ** 64))
        elif keys["add_moneys"] == t.lower() and event.obj.message['from_id'] == 466260834:
            if 466260834 in moneys:
                moneys[466260834] += 100
                with open("moneys.json", "w") as wr:
                    json.dump(moneys, wr)
        elif keys['chit_kakegurui'] in t.lower():
            i = event.obj.message['from_id']
            t = t.split()
            print(t)
            for j in sess:
                if i in sess[j][2]:
                    sess[j][0].cards_of_players[i] = t[len(keys['chit_kakegurui'].split()):]
                    vk.messages.send(
                        peer_id=i,
                        message='Ваши карты: ' + ', '.join(sess[j][0].cards_of_players[i]) + '.',
                        random_id=random.randint(0, 2 ** 64))
                    break
        elif keys['chit_perudo'] in t.lower():
            i = event.obj.message['from_id']
            t = t.split()
            print(t)
            for j in sess:
                if i in sess[j][2]:
                    sess[j][0].cubes_of_players[i] = [int(x) for x in t[len(keys['chit_perudo'].split()):]]
                    vk.messages.send(
                        peer_id=i,
                        message='Ваши кубы: ' + ', '.join(t[len(keys['chit_perudo'].split()):]) + '.',
                        random_id=random.randint(0, 2 ** 64))
                    break
        else:
            if event.obj.message['peer_id'] in sess and sess[event.obj.message['peer_id']] != []:
                game, code, players = sess[event.obj.message['peer_id']]
                if t.lower() == code:
                    sess[event.obj.message['peer_id']] = []
                    vk.messages.send(
                        peer_id=game.chat_of_game,
                        message='Игра была резко окончена.',
                        random_id=random.randint(0, 2 ** 64))
                    for i in players:
                        all_players.remove(i)
                else:
                    game.move(event)
