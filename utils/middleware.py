from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.http import HttpResponseRedirect

from user.models import Admin


class LoginMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        path = request.path
        if path in ['/user/register/','/user/login/']:
            return None
        try:
            admin_id = request.session['admin_id']
            admin = Admin.objects.filter(id=admin_id)
            admin.username = request.user
            return None
        except Exception as e:
            return HttpResponseRedirect(reverse('user:login'))


    def process_response(self,request,response):
        return response