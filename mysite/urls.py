from django.conf.urls import url,include
from django.contrib import admin


# Add new URL pattern for any new url specified


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls'))
]





