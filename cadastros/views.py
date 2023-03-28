# Create your views here.

from .models import Usuario, Fazenda, Animal

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView

class FazendaCreate(CreateView):
    model = Fazenda
    fields = ["nome", "cpf_cnpj"]
    template_name = "cadastros/form.html"
    sucess_url = reverse_lazy("pagina-inicial")


class FazendaCreate(CreateView):
    model = Usuario
    fields = ["nome"]
    template_name = "cadastros/form.html"
    sucess_url = reverse_lazy("pagina-inicial")

###############################################################


class FazendaUpdate(UpdateView):
    model = Fazenda
    fields = ["nome", "cpf_cnpj"]
    template_name = "cadastros/form.html"
    sucess_url = reverse_lazy("pagina-inicial")


class UsuarioUpdate(UpdateView):
    model = Fazenda
    fields = ["nome"]
    template_name = "cadastros/form.html"
    sucess_url = reverse_lazy("pagina-inicial")