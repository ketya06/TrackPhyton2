class Book:
    def __init__(self, name: str, author: str):
        """
        Базовый класс для всех типов книг

        :param name: Название книги
        :param author: Автор книги
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Свойство для получения названия книги (только для чтения)"""
        return self._name

    @property
    def author(self) -> str:
        """Свойство для получения автора книги (только для чтения)"""
        return self._author

    def __str__(self) -> str:
        """Строковое представление для пользователей"""
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        """Официальное строковое представление для разработчиков"""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для бумажных книг"""

    def __init__(self, name: str, author: str, pages: int):
        """
        Создание бумажной книги

        :param name: Название книги
        :param author: Автор книги
        :param pages: Количество страниц
        """
        super().__init__(name, author)
        self.pages = pages  # Используем setter для валидации

    @property
    def pages(self) -> int:
        """Свойство для получения количества страниц"""
        return self._pages

    @pages.setter
    def pages(self, value: int) -> None:
        """
        Свойство для установки количества страниц с валидацией

        :param value: Количество страниц
        :raise TypeError: Если значение не целое число
        :raise ValueError: Если значение не положительное
        """
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self) -> str:
        """Переопределяем строковое представление для бумажной книги"""
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"

    # __repr__ наследуется от Book, так как полностью подходит


class AudioBook(Book):
    """Класс для аудиокниг"""

    def __init__(self, name: str, author: str, duration: float):
        """
        Создание аудиокниги

        :param name: Название книги
        :param author: Автор книги
        :param duration: Продолжительность в часах
        """
        super().__init__(name, author)
        self.duration = duration  # Используем setter для валидации

    @property
    def duration(self) -> float:
        """Свойство для получения продолжительности"""
        return self._duration

    @duration.setter
    def duration(self, value: float) -> None:
        """
        Свойство для установки продолжительности с валидацией

        :param value: Продолжительность в часах
        :raise TypeError: Если значение не число с плавающей запятой
        :raise ValueError: Если значение не положительное
        """
        if not isinstance(value, float):
            raise TypeError("Продолжительность должна быть числом с плавающей запятой")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = value

    def __str__(self) -> str:
        """Переопределяем строковое представление для аудиокниги"""
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность: {self.duration} ч."


if __name__ == "__main__":

    paper_book = PaperBook("Война и мир", "Лев Толстой", 1300)
    audio_book = AudioBook("Мастер и Маргарита", "Михаил Булгаков", 8.5)

    print(paper_book)  # Бумажная книга Война и мир. Автор Лев Толстой. Страниц: 1300
    print(audio_book)  # Аудиокнига Мастер и Маргарита. Автор Михаил Булгаков. Длительность: 8.5 ч.

    print(repr(paper_book))  # PaperBook(name='Война и мир', author='Лев Толстой')
    print(repr(audio_book))