from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
import contextlib


@dataclass
class Post:
    id: Optional[str]
    title: str


class IModel[T](ABC):
    @abstractmethod
    def get(self, id: int) -> T:
        raise NotImplemented

    @abstractmethod
    def get_all(self) -> list[T]:
        raise NotImplemented

    @abstractmethod
    def add(self, **kwargs: object) -> None:
        raise NotImplemented

    @abstractmethod
    def update(self, id, **kwargs: object) -> None:
        raise NotImplemented

    @abstractmethod
    def delete(self, id) -> None:
        raise NotImplemented


class Model[T](IModel[T]):
    def __init__(self, model: T) -> None:
        super().__init__()
        self._Table = model

    @contextlib.contextmanager
    def connect(self):
        with sqlite3.connect("hello.db") as conn:
            yield conn.cursor()

    def create_table(self) -> None:
        """Table Created"""

    def get(self, id: int) -> T:
        # get a model and return it
        return self._Table(id=2, title="hello")

    def get_all(self) -> list[T]:
        # get all model and return it
        return [self._Table(id=2, title="hello")]

    def add(self, title: str) -> T:
        # add a model to a database
        return self._Table(id=2, title=title)

    def update(self, id, title: str) -> T:
        # update model
        return self._Table(id=2, title=title)

    def delete(self, id) -> None:
        # delete model
        pass


if __name__ == "__main__":
    model = Model[Post](Post)
    model.add(title="hey")
    model.add(title="hey")
    p = model.get(7)
    for post in model.get_all():
        print(post)
