from django.urls import path

from . import views

app_name= 'myportfolio'

urlpatterns =[

    path("",views.index,name="index"),
    # path("projects",views.projects,name="projects"),
    path("experiences",views.experiences,name="experiences"),
    # path("skills",views.skills,name="skills"),
    # path("contact",views.contact,name="contact"),
    #  path('contact/', views.contact, name='contact'),
    # path('contact', views.contact_us, name='contact_us'),

    # path('success/', views.success, name='success'),

    path('blogs/', views.Blogs, name='Blogs'),
    path('blogs/<id>/', views.detail, name='detail')

]


