from django.apps import AppConfig
#app config seems to be a registry for models within django 

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
