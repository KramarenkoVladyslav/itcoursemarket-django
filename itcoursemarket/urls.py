from django.contrib import admin
from django.urls import path, include
from tastypie.api import Api

from api.models import CategoryResource, CourseResource

api = Api(api_name='v1')
course_resource = CourseResource()
category_resource = CategoryResource()
api.register(course_resource)
api.register(category_resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('api/', include(api.urls))
]
