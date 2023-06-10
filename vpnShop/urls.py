from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('irvpnadmin2023/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('api/', include('api.urls')),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('', include('vpn.urls', namespace='vpn')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('payment/', include('payment.urls', namespace='payment'))
]


if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = _('Administrator Control Panel')
admin.site.site_title = _('Administrator Control Panel')
admin.site.index_title = _('Wellcome to Control Panel')


handler404 = 'vpn.views.handler404'
handler500 = 'vpn.views.handler500'
