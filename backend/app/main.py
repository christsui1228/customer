from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.models.customer import Base
from app.api.v1.customer import router as customer_router
from app.core.database import engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时执行
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # 关闭时执行
    await engine.dispose()

app = FastAPI(
    title="客户管理系统",
    description="客户管理系统API接口文档",
    version="1.0.0",
    lifespan=lifespan
)

# 引入路由
app.include_router(customer_router, prefix="/api/v1/customers", tags=["customers"])

@app.get("/")
async def root():
    return {"message": "客户管理系统API"}