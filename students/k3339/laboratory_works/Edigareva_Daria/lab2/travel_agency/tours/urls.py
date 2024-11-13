from . import views
from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView, LoginView
from .views import SignUpView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path(
        'signin/',
        LoginView.as_view(
            template_name='registration/signin.html',
            next_page=reverse_lazy('tour_list')
        ),
        name='signin'
    ),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('tour_list')), name='logout'),
    path('', views.TourListView.as_view(), name='tour_list'),
    path('tour/<int:pk>/', views.tour_detail, name='tour_detail'),
    path('tour/<int:pk>/reserve/', views.reserve_tour, name='reserve_tour'),
    path('tour/<int:pk>/add_review/', views.add_review, name='add_review'),
    path('reservation/<int:pk>/edit/', views.edit_reservation, name='edit_reservation'),
    path('reservation/<int:pk>/delete/', views.delete_reservation, name='delete_reservation'),
    path('sold-tours/', views.sold_tours_by_country, name='sold_tours_by_country'),
]

#
# schema_view = get_schema_view(
#     openapi.Info(
#         title="API Documentation",
#         default_version='v1',
#         description="Документация для Warriors API",
#         contact=openapi.Contact(email="your-email@example.com"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
#
# urlpatterns += [
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]
