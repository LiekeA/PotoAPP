from django.urls import path
from shop import views
from django.conf import settings
"""from django.conf.urls.static import static"""


app_name = 'shop'

urlpatterns = [
    path('poto-shop/', views.potoShop, name='potoShop'),
]

"""if settings.DEBUG:"""
"""urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""