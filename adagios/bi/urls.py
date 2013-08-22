from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('adagios',
        (r'^/?$', 'bi.views.index'),
        (r'^/add/?$', 'bi.views.add'),
        (r'^/add/subprocess/?$', 'bi.views.add_subprocess'),
        (r'^/add/graph/?$', 'bi.views.add_graph'),
        (r'^/(?P<process_name>.+)/edit/status_method$', 'bi.views.change_status_calculation_method'),
        (r'^/(?P<process_name>.+)/edit/?$', 'bi.views.edit'),
        (r'^/(?P<process_name>.+)/graphs.json/?$', 'bi.views.graphs_json'),
        (r'^/(?P<process_name>.+)/delete/?$', 'bi.views.delete'),
        (r'^/(?P<process_type>.+)/(?P<process_name>.+)/$', 'bi.views.view'),
        (r'^/(?P<process_name>.+)/?$', 'bi.views.view'),
        )
