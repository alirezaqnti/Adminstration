from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class LoginRequiredPermission(LoginRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):
        try:
            if request.user.has_usable_password():
                perm = request.user.get_all_permissions()
                if len(perm) == 0 :
                    request.session['INACTIVE'] = True
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect('SetLoginInfo')
        except:
            return self.handle_no_permission()

    
