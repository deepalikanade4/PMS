from django.contrib import admin
from .models import User,Login,Kra,PlanOfAction

# Register your models here.
@admin.register(Login)
class LoginAdmin(admin.ModelAdmin):
    list_display=['login_id','username','password','department','designation','emp_code','is_active']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['user_id','emp_code','poa_id','answer','user_rating','year','is_active','primary_reviewer_id','secondary_reviewer_id']
    filter_horizontal = ('kra_id',)
@admin.register(Kra)
class KraAdmin(admin.ModelAdmin):
    list_display=['id','kra_id','kra_questions','answer_type','activate','added_on','created_by']

@admin.register(PlanOfAction)
class POAAdmin(admin.ModelAdmin):
    list_display=['id','user_id','poa','poa_points','start_date','end_date','year','created_on','created_by']