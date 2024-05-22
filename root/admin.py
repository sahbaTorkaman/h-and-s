from django.contrib import admin
from .models import Services,Team,Skill,Portfolio



class SkillAdmin(admin.ModelAdmin):
    list_display = ['title','percent']


admin.site.register(Services)
admin.site.register(Team)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Portfolio)
