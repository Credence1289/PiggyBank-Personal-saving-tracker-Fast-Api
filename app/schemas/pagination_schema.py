from typing import List
from pydantic import BaseModel

from app.schemas.transactions_schema import Transaction

class PaginateTransactionOut(BaseModel):
    items: List[Transaction]
    total:int
    offset:int
    limit:int
    has_more: bool