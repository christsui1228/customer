from datetime import datetime, timezone
from enum import Enum as PyEnum
from sqlalchemy import Column, Integer, String, Float, Text, Enum, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CustomerSourceEnum(str, PyEnum):
    NATURAL_FLOW = "自然流量"
    RECOMMENDED = "推荐"

class CustomerTypeEnum(str, PyEnum):
    NEW = "新客户"
    OLD = "老客户"
    CHANGED_NUMBER = "换号"

class CustomerStatusEnum(str, PyEnum):
    CONSULTING = "咨询"
    SAMPLE = "样品"
    PREPARING_ORDER = "准备下单"
    DEAD = "死了"

class ShopBrandEnum(str, PyEnum):
    YI = "依"
    LI = "丽"
    MO = "末"

class Customer(Base):
    __tablename__ = "t_customer"

    id = Column(Integer, primary_key=True, index=True)
    c_shop_brand = Column('c_shop_brand', Enum(ShopBrandEnum), nullable=False)
    c_customer_id = Column('c_customer_id', String(50), unique=True, nullable=False)
    c_source = Column('c_source', Enum(CustomerSourceEnum), nullable=False)
    c_customer_type = Column('c_customer_type', Enum(CustomerTypeEnum), nullable=False)
    c_customer_demand = Column('c_customer_demand', Integer, nullable=False)
    c_core_demand = Column('c_core_demand', Text)
    c_current_status = Column('c_current_status', Enum(CustomerStatusEnum), nullable=False)
    c_expected_order_date = Column('c_expected_order_date', DateTime(timezone=True))
    c_expected_order_amount = Column('c_expected_order_amount', Float)
    c_last_modified_date = Column(
        'c_last_modified_date', 
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc), 
        onupdate=lambda: datetime.now(timezone.utc)
    )
    c_creation_date = Column(
        'c_creation_date', 
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc)
    )