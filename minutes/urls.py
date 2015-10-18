from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^hello_world/$', views.hello_world),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^user/(?P<user>.+)/$', views.user_page),
    url(r'^org/(?P<organization>.+/?P<mtgminutes_date>.+/?P<mtgminutesitem_view>.+)/', views.mtgminutesitem_view),
    url(r'^org/(?P<organization>.+/?P<mtgminutes_date>.+)/', views.organization_view),
    url(r'^org/(?P<organization>.+)/', views.organization_view),
]

'''
def user_page(request):
    # display the user page
    context = {}
    return render(request, 'minutes/user_view.html', context)

def organization_view(request):
    # desplay the organization_view
    context = {}
    return render(request, 'minutes/organization_view.html', context)

def mtgminutes_view(request):
    # display the mtgminutes_view
    context = {}
    return render(request, 'minutes/mtgminutes_view.html',context)

def mtgminutesitem_view(request):
'''
