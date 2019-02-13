from django.conf.urls import include, url
from . import view #. = current directory for bringing the html files when user clicks a 
#url

urlpatterns = [
	url(r'^$',view.index,name = "index"), #not urls and not view

	# /music/712/
	url(r'^(?P<album_id>[0-9]+)/$', view.detail)
	]