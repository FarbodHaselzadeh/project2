from django.contrib import admin
from second_app.models import Topic, AccessRecord, webpage
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(webpage)

# Register your models here.
