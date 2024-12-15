from tastypie.resources import ModelResource
from shop.models import Category, Course

class CaregoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'caregories'
        allowed_methods = ['get']

class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']

