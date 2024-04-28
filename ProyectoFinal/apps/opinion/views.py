from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from .models import Opinion, get_model
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from .forms import OpinionForm
from django.http import Http404

class OpinionListView(FormMixin, ListView):
    model = Opinion
    form_class = OpinionForm
    template_name = 'opinion_historica.html'
    context_object_name = 'opiniones'

    def get_queryset(self):
        model_name = self.kwargs['model_name']
        entity_id = self.kwargs['entity_id']
        Model = get_model('app_name', model_name)
        if Model is None:
            raise Http404("Modelo no encontrado")
        content_type = ContentType.objects.get_for_model(Model)
        return Opinion.objects.filter(content_type=content_type, object_id=entity_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Añade el formulario al contexto
        context['model_name'] = self.kwargs['model_name']
        context['entity_id'] = self.kwargs['entity_id']
        return context

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()  # Necesario para que ListView maneje POST
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        model_name = self.kwargs['model_name']
        entity_id = self.kwargs['entity_id']
        Model = get_model('app_name', model_name)
        if Model is None:
            raise Http404("Modelo no encontrado")
        
        # Crear la nueva opinión
        opinion = form.save(commit=False)
        opinion.content_object = Model.objects.get(id=entity_id)
        opinion.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        # Redirige a la misma página para ver la nueva opinión publicada
        return reverse_lazy('opiniones_por_entidad', kwargs={'model_name': self.kwargs['model_name'], 'entity_id': self.kwargs['entity_id']})





























# class OpinionFormView(FormView):
#     template_name = "opinion_historica.html"
#     form_class = OpinionForm
#     success_url = reverse_lazy('/opinion_historica/')

#     def form_valid(self, form):
#         # Esta función se llama cuando el formulario es válido
#         form.save()
#         return super().form_valid(form)

# class OpinionListView(ListView):
#     model = Opinion
#     template_name = 'opinion_historica.html'
#     context_object_name = 'opiniones'

#     # Si necesitas filtrar opiniones por alguna entidad específica, puedes sobrescribir el método get_queryset
#     def get_queryset(self):
#         # Aquí puedes filtrar las opiniones según una condición específica
#         # Por ejemplo, solo opiniones de un cierto tipo de entidad
#         return Opinion.objects.filter(alguna_condicion=True)


#     # Esta funcion sera para Opiniones recientes que se mostraran en la pagina principal
#     def get_opiniones_por_entidad(model_class, entity_id):
#         content_type = ContentType.objects.get_for_model(model_class)
#         return Opinion.objects.filter(content_type=content_type, object_id=entity_id)

