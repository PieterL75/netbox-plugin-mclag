from django.urls import path

from netbox.views.generic import ObjectChangeLogView
from netbox_plugin_mclag.models import McDomain,McLag
from netbox_plugin_mclag.views import (
    McDomainView,
    McDomainListView,
    McDomainEditView,
    McDomainBulkEditView,
    McDomainDeleteView,
    McDomainBulkDeleteView,
    McLagView,
    McLagListView,
    McLagEditView,
    McLagDeleteView,
    McLagBulkEditView,
    McLagBulkDeleteView,
)

urlpatterns = (

    # McDomain
    path('domains/', McDomainListView.as_view(), name='mcdomain_list'),
    path('domains/add/', McDomainEditView.as_view(), name='mcdomain_add'),
    path('domains/edit/', McDomainBulkEditView.as_view(), name='mcdomain_bulk_edit'),
    path('domains/delete/', McDomainBulkDeleteView.as_view(), name='mcdomain_bulk_delete'),
    path('domains/<int:pk>/', McDomainView.as_view(), name='mcdomain'),
    path('domains/<int:pk>/edit/', McDomainEditView.as_view(), name='mcdomain_edit'),
    path('domains/<int:pk>/delete/', McDomainDeleteView.as_view(), name='mcdomain_delete'),
    path('domains/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='mcdomain_changelog', kwargs={
        'model': McDomain
    }),

    # McLag
    path('mclags/', McLagListView.as_view(), name='mclag_list'),
    path('mclags/add/', McLagEditView.as_view(), name='mclag_add'),
    path('mclags/edit/', McLagBulkEditView.as_view(), name='mclag_bulk_edit'),
    path('mclags/delete/', McLagBulkDeleteView.as_view(), name='mclag_bulk_delete'),
    path('mclags/<int:pk>/', McLagView.as_view(), name='mclag'),
    path('mclags/<int:pk>/edit/', McLagEditView.as_view(), name='mclag_edit'),
    path('mclags/<int:pk>/delete/', McLagDeleteView.as_view(), name='mclag_delete'),
    path('mclags/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='mclag_changelog', kwargs={
        'model': McLag
    }),

)