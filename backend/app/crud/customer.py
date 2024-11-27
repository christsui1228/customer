from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.models.customer import Customer  # 从 models 导入 Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate  # 从 schemas 只导入这些

async def create_customer(db: AsyncSession, customer: CustomerCreate):
    db_customer = Customer(**customer.model_dump())
    db.add(db_customer)
    await db.commit()
    await db.refresh(db_customer)
    return db_customer

async def get_customer(db: AsyncSession, customer_id: int):
    result = await db.execute(select(Customer).filter(Customer.id == customer_id))
    return result.scalars().first()

async def get_customers(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Customer).offset(skip).limit(limit))
    return result.scalars().all()

async def update_customer(db: AsyncSession, customer_id: int, customer: CustomerUpdate):
    stmt = update(Customer).where(Customer.id == customer_id).values(**customer.model_dump(exclude_unset=True))
    result = await db.execute(stmt)
    await db.commit()
    return await get_customer(db, customer_id)

async def delete_customer(db: AsyncSession, customer_id: int):
    stmt = delete(Customer).where(Customer.id == customer_id)
    result = await db.execute(stmt)
    await db.commit()
    return result.rowcount > 0