from django.contrib import admin
from person.models import Participant, Mentor, Hobbie, Language, Nationality

# Register your models here.
admin.site.register(Participant)
admin.site.register(Mentor)
admin.site.register(Hobbie)
admin.site.register(Language)
admin.site.register(Nationality)
