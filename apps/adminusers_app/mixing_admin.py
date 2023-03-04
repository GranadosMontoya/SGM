from django.shortcuts import redirect


class MixingAdmin(object):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super(MixingAdmin, self).dispatch(request, *args, **kwargs)
        return redirect('user_app:home')