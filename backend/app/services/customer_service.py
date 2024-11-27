from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate
from app.core.exceptions import CustomerNotFoundError

class CustomerService:
    @staticmethod
    def create_customer(db: Session, customer_data: CustomerCreate):
        """
        创建客户
        """
        try:
            db_customer = Customer(**customer_data.dict())
            db.add(db_customer)
            db.commit()
            db.refresh(db_customer)
            return db_customer
        except Exception as e:
            db.rollback()
            raise

    @staticmethod
    def get_customer_by_id(db: Session, customer_id: str) -> Optional[Customer]:
        """
        根据客户ID获取客户
        """
        customer = db.query(Customer).filter(Customer.c_customer_id == customer_id).first()
        if not customer:
            raise CustomerNotFoundError(f"未找到ID为 {customer_id} 的客户")
        return customer

    @staticmethod
    def update_customer(
        db: Session, 
        customer_id: str, 
        update_data: CustomerUpdate
    ):
        """
        更新客户信息
        """
        try:
            customer = CustomerService.get_customer_by_id(db, customer_id)
            
            # 更新非空字段
            update_dict = update_data.dict(exclude_unset=True)
            for key, value in update_dict.items():
                setattr(customer, f"c_{key}", value)
            
            db.commit()
            db.refresh(customer)
            return customer
        except Exception as e:
            db.rollback()
            raise

    @staticmethod
    def list_customers(db: Session, skip: int = 0, limit: int = 100):
        """
        分页获取客户列表
        """
        return db.query(Customer).offset(skip).limit(limit).all()