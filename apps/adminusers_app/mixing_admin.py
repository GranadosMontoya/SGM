from django.shortcuts import redirect


class SoloAdmin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(SoloAdmin, self).dispatch(request, *args, **kwargs)
        return redirect('user_app:home')