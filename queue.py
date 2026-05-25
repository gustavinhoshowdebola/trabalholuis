from typing import Any, List

class Queue:

    def __init__(self, max_size: int = None) -> None:
        self.__data: List[Any] = []
        self.__max_size = max_size

    def __repr__(self) -> str:
        return str(self.__data)

    def is_full(self) -> bool:
        if self.__max_size is None:
            return False
        if len(self.__data) >= self.__max_size:
            return True
        else:
            return False

    def is_empty(self) -> bool:
        if len(self.__data) == 0:
            return True
        else:
            return False

    def enqueue(self, elemento: Any) -> None:
        if self.is_full():
            print("fila cheia, nao foi possivel adicionar ")
        else:
            self.__data.append(elemento)

    def dequeue(self) -> Any:
        if self.is_empty():
            print("fila vazia")
        else:
            print("item removido:", self.__data.pop(0))

    def peek(self) -> Any:
        if self.is_empty():
            print("Fila vazia")
        else:
            print("primeiro item:" , self.__data[0])

    def size(self) -> int:
        print("tamanho da fila: ", len(self.__data))
        return len(self.__data)

    def clear(self) -> None:
        self.__data.clear()
        print("fila limpa")
