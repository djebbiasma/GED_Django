# documents/urls.py
from django.urls import path
from .views import DocumentListView, DocumentDetailView, DocumentCreateView, DocumentUpdateView, DocumentDeleteView,add_comment
from .views import DossierListView,DossierCreateView,DossierDetailView,DossierUpdateView,DossierDeleteView,add_comment

urlpatterns = [
    path('', DocumentListView.as_view(), name='document_list'),
    path('<int:pk>/', DocumentDetailView.as_view(), name='document_detail'),
    path('new/', DocumentCreateView.as_view(), name='document_new'),
    path('<int:pk>/edit/', DocumentUpdateView.as_view(), name='document_edit'),
    path('<int:pk>/delete/', DocumentDeleteView.as_view(), name='document_delete'),

    path('dossiers/', DossierListView.as_view(), name='dossier_list'),
    path('dossiers/<int:pk>/', DossierDetailView.as_view(), name='dossier_detail'),
    path('dossiers/new/', DossierCreateView.as_view(), name='dossier_create'),
    path('dossiers/<int:pk>/edit/', DossierUpdateView.as_view(), name='dossier_edit'),
    path('dossiers/<int:pk>/delete/', DossierDeleteView.as_view(), name='dossier_delete'),
    path('<int:document_id>/comment/', add_comment, name='add_comment'),

]
