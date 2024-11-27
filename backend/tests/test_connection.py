import asyncio
from app.core.database import engine
from app.core.config import settings

async def test_database_connection():
    try:
        # 测试数据库连接
        async with engine.connect() as conn:
            await conn.execute("SELECT 1")
        print("✅ Database connection successful!")
    except Exception as e:
        print("❌ Database connection failed!")
        print(f"Error: {str(e)}")

async def test_settings():
    try:
        # 测试配置加载
        assert settings.DATABASE_URL is not None
        assert settings.API_V1_STR == "/api/v1"
        print("✅ Settings loaded successfully!")
    except AssertionError:
        print("❌ Settings loading failed!")

if __name__ == "__main__":
    asyncio.run(test_database_connection())
    asyncio.run(test_settings())