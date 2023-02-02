from django.shortcuts import redirect


class Loguin_null(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('admin_app:list_user')
        return super().dispatch(request, *args, **kwargs)