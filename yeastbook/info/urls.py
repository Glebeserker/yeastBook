from django.urls import path, include
from django.urls.resolvers import URLPattern

from info import views

urlpatterns = [
    path('companies/', views.CompanyView.as_view()),
    path('types/', views.TypeView.as_view()),
    path('all-yeast/', views.AllYeast.as_view()),
    path('companies/<slug:company_slug>/', views.CompanyFilteredView.as_view()),
    path('types/<slug:type_slug>/', views.TypeFilteredView.as_view()),
    path('types/<slug:type_slug>/<slug:yeast_slug>/', views.TypedYeastView.as_view()),
    path('companies/<slug:company_slug>/<slug:yeast_slug>/', views.CompanyYeastView.as_view())
]