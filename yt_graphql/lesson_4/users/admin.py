from django.apps import apps
from django.contrib import admin

from users.models import User

admin.site.register(User)

app = apps.get_app_config("graphql_auth")
for model_name, model in app.models.items():
    admin.site.register(model)
