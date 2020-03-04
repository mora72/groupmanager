from django.urls import path
from . import views

urlpatterns = [
    path('', views.grupo_list),
    path('grupo/<int:idgrupo>', views.grupo_view),
    path('grupo/delete/<int:idgrupo>', views.grupo_delete),
    path('gruponew/', views.grupo_new),
    path('grupo/edit/<int:idgrupo>', views.grupo_edit),

    path('integrantes/', views.integrante_list),
    path('integrante/<int:idintegrante>', views.integrante_view),
    path('integrante/delete/<int:idintegrante>', views.integrante_delete),
    path('integrantenew/', views.integrante_new),
    path('integrante/edit/<int:idintegrante>', views.integrante_edit),

    path('distancias/', views.distancias)
]
