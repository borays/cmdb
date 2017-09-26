from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.index,name='index'),

    ### for server
    url(r'^server_items/$',views.server_list,name='server_items'),
    url(r'^server_new/$',views.server_new,name='server_new'),
    url(r'^server_edit/(?P<item_id>\d+)/$', views.server_edit, name='server_edit'),
    url(r'^server_delete/(?P<item_id>\d+)/$',views.server_delete,name='server_delete'),
    url(r'^server_search/$',views.server_search,name='server_search'),

    ### for idc
    url(r'^idc_items/$',views.idc_list,name='idc_items'),
    url(r'^idc_new/$',views.idc_new,name='idc_new'),
    url(r'^idc_edit/(?P<item_id>\d+)/$', views.idc_edit, name='idc_edit'),
    url(r'^idc_delete/(?P<item_id>\d+)/$',views.idc_delete,name='idc_delete'),
    url(r'^idc_search/$',views.idc_search,name='idc_search'),

    ### for cabinet
    url(r'^cabinet_items/$',views.cabinet_list,name='cabinet_items'),
    url(r'^cabinet_new/$',views.cabinet_new,name='cabinet_new'),
    url(r'^cabinet_edit/(?P<item_id>\d+)/$', views.cabinet_edit, name='cabinet_edit'),
    url(r'^cabinet_delete/(?P<item_id>\d+)/$',views.cabinet_delete,name='cabinet_delete'),
    url(r'^cabinet_search/$',views.cabinet_search,name='cabinet_search'),

    ### for people
    url(r'^people_items/$',views.people_list,name='people_items'),
    url(r'^people_new/$',views.people_new,name='people_new'),
    url(r'^people_edit/(?P<item_id>\d+)/$', views.people_edit, name='people_edit'),
    url(r'^people_delete/(?P<item_id>\d+)/$',views.people_delete,name='people_delete'),
    url(r'^people_search/$',views.people_search,name='people_search'),

    ### for container
    url(r'^container_items/$', views.container_list, name='container_items'),
    url(r'^container_new/$', views.container_new, name='container_new'),
    url(r'^container_edit/(?P<item_id>\d+)/$', views.container_edit, name='container_edit'),
    url(r'^container_delete/(?P<item_id>\d+)/$', views.container_delete, name='container_delete'),
    url(r'^container_search/$', views.container_search, name='container_search'),

    ### for vm_cluster
    url(r'^vm_cluster_items/$', views.vm_cluster_list, name='vm_cluster_items'),
    url(r'^vm_cluster_new/$', views.vm_cluster_new, name='vm_cluster_new'),
    url(r'^vm_cluster_edit/(?P<item_id>\d+)/$', views.vm_cluster_edit, name='vm_cluster_edit'),
    url(r'^vm_cluster_delete/(?P<item_id>\d+)/$', views.vm_cluster_delete, name='vm_cluster_delete'),
    url(r'^vm_cluster_search/$', views.vm_cluster_search, name='vm_cluster_search'),

    ### for vm
    url(r'^vm_items/$', views.vm_list, name='vm_items'),
    url(r'^vm_new/$', views.vm_new, name='vm_new'),
    url(r'^vm_edit/(?P<item_id>\d+)/$', views.vm_edit, name='vm_edit'),
    url(r'^vm_delete/(?P<item_id>\d+)/$', views.vm_delete, name='vm_delete'),
    url(r'^vm_search/$', views.vm_search, name='vm_search'),


]