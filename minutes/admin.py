from django.contrib import admin

# Register your models here.
from .models import User
from .models import Organization
from .models import MtgMinutes
from .models import MtgMinutesItem


class UserAdmin(admin.ModelAdmin):
    list_display =  [ "__unicode__"
                    , "password"
                    , "email"]

    class Meta:
        model = User

# lolcool

class UserInline(admin.StackedInline):
    model = User

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]
    # inlines = [UserInline]
    class Meta:
        model = Organization

class MtgMinutesAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]

    class Meta:
        model = MtgMinutes

class MtgMinutesItemAdmin(admin.ModelAdmin):
    list_display = ["__unicode__"]

    class Meta:
        model = MtgMinutesItem

admin.site.register(User, UserAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(MtgMinutes, MtgMinutesAdmin)
admin.site.register(MtgMinutesItem, MtgMinutesItemAdmin)


