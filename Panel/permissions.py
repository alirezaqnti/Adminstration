from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class LoginRequiredPermission(LoginRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):
        try:
            print("USER:",request.user.has_usable_password())
            if request.user.has_usable_password():
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('SetLoginInfo')
        except:
            return self.handle_no_permission()

    
