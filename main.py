from typing import Generic, TypeVar, Iterator
from collections.abc import Iterator as IteratorABC

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._data: list[T] = []

    def push(self, item: T) -> None:
        self._data.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Stack bo'sh")
        return self._data.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Stack bo'sh")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self) -> Iterator[T]:
        return reversed(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data})"

# int stack
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)
print(int_stack)          # Stack([1, 2, 3])
print(int_stack.peek())   # 3
print(int_stack.pop())    # 3
print(len(int_stack))     # 2
print(list(int_stack))    # [2, 1]

# str stack
str_stack: Stack[str] = Stack()
str_stack.push("salom")
str_stack.push("dunyo")
print(str_stack.pop())    # dunyo
