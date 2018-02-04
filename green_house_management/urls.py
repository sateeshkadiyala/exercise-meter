from django.urls import path
from django.conf.urls import url
from .views import plot_views, device_views, media_views, plot_setting_views, alert_views, generate_new_data
from django.conf import settings


urlpatterns = [
    # plot routes
    url(r'^$', plot_views.PlotList.as_view(), name='plot_list'),
    url(r'^plots$', plot_views.PlotList.as_view(), name='plot_list'),
    url(r'^plots/new$', plot_views.PlotCreate.as_view(), name='plot_new'),
    url(r'^plots/edit/(?P<pk>\d+)$', plot_views.PlotUpdate.as_view(), name='plot_edit'),
    url(r'^plots/delete/(?P<pk>\d+)$', plot_views.PlotDelete.as_view(), name='plot_delete'),
    # device routes
    url(r'^devices$', device_views.DeviceList.as_view(), name='device_list'),
    url(r'^devices/new$', device_views.DeviceCreate.as_view(), name='device_new'),
    url(r'^devices/edit/(?P<pk>\d+)$', device_views.DeviceUpdate.as_view(), name='device_edit'),
    url(r'^devices/delete/(?P<pk>\d+)$', device_views.DeviceDelete.as_view(), name='device_delete'),

    # media routes
    url(r'^media$', media_views.MediaList.as_view(), name='media_list'),
    url(r'^media/new$', media_views.MediaCreate.as_view(), name='media_new'),
    url(r'^media/edit/(?P<pk>\d+)$', media_views.MediaUpdate.as_view(), name='media_edit'),
    url(r'^media/delete/(?P<pk>\d+)$', media_views.MediaDelete.as_view(), name='media_delete'),

    # media routes
    url(r'^plot_setting$', plot_setting_views.plot_setting_list, name='plot_setting_list'),
    url(r'^plot_setting/new$', plot_setting_views.plot_setting_new, name='plot_setting_new'),
    url(r'^plot_setting/edit/(?P<pk>\d+)$', plot_setting_views.plot_setting_edit, name='plot_setting_edit'),
    url(r'^plot_setting/delete/(?P<pk>\d+)$', plot_setting_views.PlotSettingDelete.as_view(), name='plot_setting_delete'),

    url(r'^alerts/list$', alert_views.AlertList.as_view(), name='alert_list'),
    url(r'^newdata$', generate_new_data.generate_new_data, name='generate_new_data'),
]