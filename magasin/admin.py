from django.contrib import admin
# Register your models here.

# Register your models here.
from .models import equipe
admin.site.register(equipe)
from .models import Project
admin.site.register(Project)
from .models import Personnel
admin.site.register(Personnel)

from .models import Service
admin.site.register(Service)
from .models import Detail
admin.site.register(Detail)
from .models import BlogPost
admin.site.register(BlogPost)

