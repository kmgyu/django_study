from django.apps import AppConfig

# apps(config)는 앱의 설정을 관리하는 파일.
# 특별한 일 없으면 수정할 일이 없다.
class PyboConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pybo"
