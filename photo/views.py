from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Photo


class PhotoListView(ListView):
    model = Photo
    template_name = 'photo/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort', 'recent')
        if sort == 'recent':
            queryset = queryset.order_by('-uploaded_at')  # Tri des plus récentes aux plus anciennes
        else:
            queryset = queryset.order_by('uploaded_at')  # Tri des plus anciennes aux plus récentes
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Passe le paramètre `sort` dans le contexte pour ajuster le label du bouton
        context['sort'] = self.request.GET.get('sort', 'recent')
        return context


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo/detail.html'

class PhotoUploadView(CreateView):
    model = Photo
    fields = ['name', 'photo']
    template_name = 'photo/form.html'
    success_url = reverse_lazy('list')

class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['name', 'photo']
    template_name = 'photo/form.html'
    success_url = reverse_lazy('list')

class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = 'photo/confirm_delete.html'
    success_url = reverse_lazy('list')
