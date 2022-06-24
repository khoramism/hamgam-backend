from rest_framework import routers
from skill import api_views as skill_api_views



router = routers.DefaultRouter()
router.register(r'skills', skill_api_views.SkillViewSet)