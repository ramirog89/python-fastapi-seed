from typing import List, Generic, TypeVar
from pydantic.generics import GenericModel


T = TypeVar('T')


class PaginationSchema(GenericModel, Generic[T]):
    page: int
    limit: int
    total: int
    items: List[T]
