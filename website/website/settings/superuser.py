import os
from django.apps import apps
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_admin(sender, **kwargs):
    # pokreći samo kad je env var uključen
    if os.getenv("CREATE_SUPERUSER") != "True":
        return

    # čekamo da auth app postoji
    User = apps.get_model("auth", "User")

    username = os.getenv("DJ_ADMIN_USERNAME", "admin")
    email = os.getenv("DJ_ADMIN_EMAIL", "admin@example.com")
    password = os.getenv("DJ_ADMIN_PASSWORD", "admin123")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
