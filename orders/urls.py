from django.urls import path
from .views import manage_menu,add_food_item, update_food_item, delete_food_item,home,CategoryMenuView
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'orders' 
urlpatterns = [
    path('menu/', manage_menu, name='manage_menu'),
    # path("menu/add-category/", add_category, name="add_category"),
    path("menu/delete-category/<int:category_id>/", delete_category, name="delete_category"),
    path('menu/add/', add_food_item, name='add_food_item'),
    path('menu/update/<int:food_id>/', update_food_item, name='update_food_item'),
    path('menu/delete/<int:food_id>/', delete_food_item, name='delete_food_item'),
    path('', home, name='home'),
    path("category-menu/", CategoryMenuView.as_view(), name="cat_menu"),
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:food_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('place-order/', place_order, name='place_order'),
    path('payment-success/', payment_success, name='payment_success'),
    path('cancel-order/', cancel_order, name='cancel_order'),
    path('order-history/', order_history, name='order_history'),
    path("import-menu/", import_menu, name="import_menu"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


