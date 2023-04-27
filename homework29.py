#  Գրել MyShows class, որը․
#    - __init__ ում կստանա
#      -- սերիալի անունը (պետք է լինի տեքստ),
#      -- հարթակը, որտեղ ցուցադրվում է սերիալը (պետք է լինի տեքստ),
#      -- առաջին սերիան դուրս գալու տարեթիվը (պետք է լինի ամբողջ թիվ),
# -- սերիայի համարը, որը դիտում է օգտատերը (որ սերիային է հասել) (պետք է լինի ամբողջ թիվ), default արժեքը պետք է լինի 0,
#      -- օգտատիրոջ դրած գնահատականը (պետք է լինի ամբողջ թիվ 1-10 միջակայքում), default արժեքը պետք է լինի None,
#      -- գլխավոր դերասանների ցանկը (պետք է լինի լիստ),
#    - բոլոր ատրիբուտները կլինեն private,
#    - կունենա getter բոլոր ատրիբուտների համար,
#    - միայն սերիայի համարի և գնահատականի համար կունենա նաև setter,
#    - միայն գնահատականի համար կունենա նաև deleter, այնպես պետք է ռեալիզացնել, որ գնահատականը ջնջելուց հետո այն նորից
#     սահմանելու հնարավորություն լինի,
#    - կունենա մեթոդներ դերասանների ցանկը թարմացնելու համար (լիստից անուն ջնջել, լիստում անուն ավելացնել),
#    - կունենա մեթոդ, որը կվերադարձնի սերիալի մասին ամբողջ ինֆորմացիան։

class MyShows:
    def __init__(self, title: str, platform: str, year: int, actors: list, episode: int = 1, rating: (int, None) = None):
        self.is_valid_title_platform(title)
        self.is_valid_title_platform(platform)
        self.is_valid_year_episode(year)
        self.is_valid_year_episode(episode)
        self.is_valid_list(actors)
        self.is_valid_rating(rating)

        self.__title = title
        self.__platform = platform
        self.__year = year
        self.__actors = actors
        self.__episode = episode
        self.__rating = rating

    @staticmethod
    def is_valid_title_platform(title_platform):
        if not isinstance(title_platform, str):
            raise Exception('Must be string (title or platform)')

    @staticmethod
    def is_valid_year_episode(year_episode):
        if not (isinstance(year_episode, int) and year_episode >= 1):
            raise Exception('Must be positive integer (year or episode)')

    @staticmethod
    def is_valid_rating(rating):
        if not (isinstance(rating, int) and 1 <= rating <= 10):
            raise Exception('Must be positive integer from 1 to 10 (rate)')

    @staticmethod
    def is_valid_list(actors):
        if not (isinstance(actors, list) and all(isinstance(i, str) for i in actors)):
            raise Exception('Must be list of strings (actors)')

    @property
    def title(self):
        return self.__title

    @property
    def platform(self):
        return self.__platform

    @property
    def year(self):
        return self.__year

    @property
    def actors(self):
        return self.__actors

    @property
    def episode(self):
        return self.__episode

    @episode.setter
    def episode(self, value):
        self.is_valid_year_episode(value)
        self.__episode = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.is_valid_rating(value)
        self.__rating = value

    @rating.deleter
    def rating(self):
        self.__rating = None

    def update_actors_add(self, changes):
        self.is_valid_title_platform(changes)
        self.__actors.append(changes)
        print('The actors list is updated.', self.__actors)

    def update_actors_remove(self, changes):
        self.is_valid_title_platform(changes)
        self.__actors.remove(changes)
        print('The actors list is updated.', self.__actors)

    def my_shows_description(self):
        return f'Title: {self.__title}\nPlatform: {self.__platform}\nRelease year: {self.__year}\n' \
                f'Actors: {self.__actors}\nEpisode: {self.__episode}\nRating: {self.__rating}'


myshows = MyShows('Game of Thrones', 'HBO', 2011, ['Sean Bean', 'Mark Addy', 'Michelle Fairley'], 5, 8)
print(myshows.title)
print(myshows.platform)
print(myshows.year)
print(myshows.actors)
print(myshows.episode)
print(myshows.rating)
myshows.rating = 9
print(myshows.rating)
print(myshows.update_actors_add('Lena Headey'))
print(myshows.update_actors_remove('Sean Bean'))
print(myshows.my_shows_description())
myshows.series_number = 10
print(myshows.series_number)
del myshows.rating
print(myshows.rating)
myshows.rating = 9
print(myshows.rating)
print(myshows.my_shows_description())
