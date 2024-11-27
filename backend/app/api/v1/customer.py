from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.database import get_db
from app.schemas.customer import CustomerCreate, CustomerUpdate, CustomerInDB
from app.crud.customer import create_customer, get_customer, get_customers, update_customer, delete_customer

router = APIRouter()

@router.post("/", response_model=CustomerInDB)
async def create_new_customer(customer: CustomerCreate, db: AsyncSession = Depends(get_db)):
    return await create_customer(db, customer)

@router.get("/{customer_id}", response_model=CustomerInDB)
async def read_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    customer = await get_customer(db, customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@router.get("/", response_model=List[CustomerInDB])
async def read_customers(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    customers = await get_customers(db, skip=skip, limit=limit)
    return customers

@router.put("/{customer_id}", response_model=CustomerInDB)
async def update_existing_customer(customer_id: int, customer: CustomerUpdate, db: AsyncSession = Depends(get_db)):
    updated_customer = await update_customer(db, customer_id, customer)
    if updated_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer

@router.delete("/{customer_id}")
async def remove_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_customer(db, customer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"detail": "Customer deleted successfully"}