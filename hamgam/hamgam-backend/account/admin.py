from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import Account
from .forms import UserCreationForm, UserChangeForm

class AccountAdmin(BaseUserAdmin):
	form = UserCreationForm
	add_form = UserChangeForm

	list_display =  ('email', 'username', 'phone','avatar', 'is_staff',  'is_superuser')
	list_filter = ('is_superuser',)
	
	fieldsets = (
		(None, {'fields': ('email', 'is_staff', 'is_superuser', 'password')}),
		('Personal info', {'fields': ('username', 'phone', 'avatar')}),
		('Groups', {'fields': ('groups',)}),
		('Permissions', {'fields': ('user_permissions',)}),
	)
	add_fieldsets = (
		(None, {'fields': ('email','password'),}),
		('Personal info', {'fields': ('username', 'phone', 'avatar')}),
		('Groups', {'fields': ('groups',)}),
		('Permissions', {'fields': ('user_permissions',)}),
	)

	search_fields = ('email', 'username', 'phone')
	ordering = ('email',)
	filter_horizontal = ()



admin.site.register(Account, AccountAdmin)

