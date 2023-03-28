from django.urls import path
from views import FazendaCreate, FazendaUpdate
from .views import UsuarioCreate, UsuarioUpdate

urlpatterns = [
    path("cadastrar/fazenda/", FazendaCreate.as_view(), name="cadastro-fazenda"),
    path("cadastrar/usuario/", FazendaCreate.as_view(), name="cadastro-usuario"),

    path("cadastrar/fazenda/<int:pk>/", FazendaUpdate.as_view(), name="cadastro-usuario"),
    path("cadastrar/usuario/<int:pk>/", FazendaUpdate.as_view(), name="cadastro-usuario"),

    #path("caminhp/", View.as_view()),
]
