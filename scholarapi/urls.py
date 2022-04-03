from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("api/getcolleges", CollegeViewSet, basename="getcolleges")
router.register("api/getcourses", CourseViewSet, basename="getcourses")
router.register("api/getcandidate", CandidateViewSet, basename="getcandidates")
router.register("api/getcarousels", CarouselViewSet, basename="getcarousels")
# router.register("api/search", SearchViewSet, basename="search")

urlpatterns = [
    path("", include(router.urls)),
    path("api/search/<str:keyword>/", searchViewSet),
    path("api/getcollegewithcourse/<int:pk>/", getCollegewithCourse)
]
