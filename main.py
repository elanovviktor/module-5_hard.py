import hashlib
import time


class User:
    def __init__(self, nickname, password, age):# иницилизируем юзера
        self. nickname = nickname
        self. password = password
        self. age = age

class Video:
    def __init__(self, title, duration,  adult_mode=False):#  title(заголовок, строка),
    # duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
    # adult_mode(ограничение по возрасту, bool (False по умолчанию))
        self. title = title
        self. duration = duration
        self. time_now = 0
        self. adult_mode = adult_mode

class UrTube:
    def __init__(self):# users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
        self. users = [] # [] список коллекции юзера
        self. videos = [] # здесь список , поэтому добавляем s.
        self. current_user = None # атрибут текущий пользователь и что с ним делать???

    def log_in(self, nickname, password):# задаем логин и пароль
        hashed_password = hashlib.sha256(password. encode()).hexdigest()#Хеш-пароль в Python создаётся с помощью модуля
        # hashlib и алгоритма SHA-256. Вот пример кода:  В этом примере пользователь вводит пароль, который
        # преобразуется в хеш с помощью функции hashlib.sha211(). Затем полученный хеш выводится на экран.
        for user in self.users:# задаем пользователя
            if user.nickname == nickname and user.password == hashed_password:# сравниваем или ищем совпадения
                self.current_user = user
                return# если нет то возвращаем
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):#пользователь уже существует
            print(f"Пользователь {nickname} уже существует.")#После регистрации, вход выполняется автоматически.
        new_user = User(nickname, password, age)
        self. users.append(new_user)
        self. current_user = new_user
    def log_out(self):
        self. current_user = None# сброс текущего пользователя на None

    def add(self, *new_videos):#принимаем видео,много
        for new_video in new_videos:# проходим по списку нью видео
            if not any(video. title == new_video. title for video in self.videos):#проверяем на совпадения
                self.videos. append(new_video)#усли совпадений нет то добавляем в конец списка

    def get_videos(self, search_word):# задаем поисковое слово, ищем в списке названий независимо от  регистра
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]
    def watch_video(self, title):
        if self. current_user is None:#если не находит точного совпадения(вплоть до пробела), то ничего не воспроизводится
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self. videos:
            if video. title == title:
                if video. adult_mode and self. current_user. age < 18:# проверяем ограничение по возрасту
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for second in range(video.duration):# пауза между выводами видео зададим 1 секунду
                    print(f"секунда {second}")
                    time.sleep(1)
                video. time_now = 0
                print("конец видео")
                return


        print("видео не найдено")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


