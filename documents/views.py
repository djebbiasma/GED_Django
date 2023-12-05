# documents/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Dossier, Document
from django.urls import reverse_lazy,reverse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import CommentForm
from django.db.models import Q
from django.contrib.auth.mixins import UserPassesTestMixin

class DocumentListView(ListView):
    model = Document
    template_name = 'documents/document/list.html'

    

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'documents/document/details.html'

class DocumentCreateView(CreateView):
    model = Document
    template_name = 'documents/document/new.html'
    fields = ['nom', 'fichier', 'categorie','dossier']
    success_url = reverse_lazy('document_list')

class DocumentUpdateView(UpdateView):
    model = Document
    template_name = 'documents/document/edit.html'
    fields = ['nom', 'fichier', 'categorie']
    success_url = reverse_lazy('document_list')

class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'documents/document/delete.html'
    success_url = reverse_lazy('document_list')
# documents/views.py


class DossierListView(ListView):
    model = Dossier
    template_name = 'documents/dossier/dossier_list.html'  
    context_object_name = 'dossiers'

class DossierDetailView(DetailView):
    model = Dossier
    template_name = 'documents/dossier/dossier_detail.html'  
#lahne dossiercreateview heritent mend eux classes: userpassesstestmixin et createview. user passesstestmixin hiya eli bech tjibli test_func eli bech
#traja3li true ke el user admin . 
class DossierCreateView(UserPassesTestMixin,CreateView):
    model = Dossier
    template_name = 'documents/dossier/dossier_form.html'  
    fields = ['nom']
    success_url = reverse_lazy('dossier_list')
    def test_func(self):
        # Check if the user has the 'admin' role
        return self.request.user.role == 'admin'
class DossierUpdateView(UpdateView):
    model = Dossier
    template_name = 'documents/dossier/dossier_form.html'  
    fields = ['nom']

class DossierDeleteView(DeleteView):
    model = Dossier
    template_name = 'documents/dossier/dossier_confirm_delete.html'  
    success_url = reverse_lazy('dossier_list')
def add_comment(request, document_id):
    document = get_object_or_404(Document, pk=document_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.document = document
            comment.user = request.user

            comment.save()

            return HttpResponseRedirect(reverse('document_detail', args=[document.id]))
    else:
        form = CommentForm()

    return render(request, 'documents/document/comment.html', {'form': form, 'document': document})