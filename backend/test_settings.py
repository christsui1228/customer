# test_settings.py
def test_import():
    try:
        from app.core.config import Settings, settings
        print("Settings class imported:", Settings)
        print("settings instance imported:", settings)
        print("PROJECT_NAME:", settings.PROJECT_NAME)
        return True
    except Exception as e:
        print("Import error:", str(e))
        return False

if __name__ == "__main__":
    test_import()