from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from enum import Enum

class CustomerSourceEnum(str, Enum):
    NATURAL_FLOW = "自然流量"
    RECOMMENDED = "推荐"

class CustomerTypeEnum(str, Enum):
    NEW = "新客户"
    OLD = "老客户"
    CHANGED_NUMBER = "换号"

class CustomerStatusEnum(str, Enum):
    CONSULTING = "咨询"
    SAMPLE = "样品"
    PREPARING_ORDER = "准备下单"
    DEAD = "死了"

class ShopBrandEnum(str, Enum):
    YI = "依"
    LI = "丽"
    MO = "末"

class CustomerBase(BaseModel):
    c_shop_brand: ShopBrandEnum
    c_customer_id: str
    c_source: CustomerSourceEnum
    c_customer_type: CustomerTypeEnum
    c_customer_demand: int
    c_core_demand: Optional[str] = None
    c_current_status: CustomerStatusEnum
    c_expected_order_date: Optional[datetime] = None
    c_expected_order_amount: Optional[float] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    c_shop_brand: Optional[ShopBrandEnum] = None
    c_source: Optional[CustomerSourceEnum] = None
    c_customer_type: Optional[CustomerTypeEnum] = None
    c_customer_demand: Optional[int] = None
    c_core_demand: Optional[str] = None
    c_current_status: Optional[CustomerStatusEnum] = None
    c_expected_order_date: Optional[datetime] = None
    c_expected_order_amount: Optional[float] = None

class CustomerInDB(CustomerBase):
    id: int
    c_creation_date: datetime
    c_last_modified_date: datetime

    class Config:
        from_attributes = True