import webley as wb

class SiteConfig(wb.AppConfig):
    DEBUG = True
    ALLOWED_HOSTS = [
        "127.0.0.1", "localhost"
    ]

app = wb.Webley(config=SiteConfig())

app.run()
