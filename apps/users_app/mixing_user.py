from django.shortcuts import redirect


class not_login(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user_app:home')
        return super().dispatch(request, *args, **kwargs)