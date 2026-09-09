from django.urls import path
from . import views
from . import user_settings
from . import field_permissions_views

app_name = 'authentication'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Settings
    path('settings/profile/', user_settings.user_profile_settings, name='user_profile_settings'),
    path('settings/company/', user_settings.company_settings, name='company_settings'),
    
    # User Management
    path('users/', views.user_management_view, name='users'),
    path('users/create/', views.create_user_view, name='create_user'),
    path('users/<int:user_id>/', views.view_user_profile, name='view_user_profile'),
    path('users/<int:user_id>/edit/', views.edit_user_view, name='edit_user'),
    path('users/<int:user_id>/toggle-status/', views.toggle_user_status, name='toggle_user_status'),
    path('users/<int:user_id>/delete/', views.delete_user_view, name='delete_user'),
    path('users/<int:user_id>/assign-profile/', views.assign_user_profile_view, name='assign_profile'),
    
    # Profile Management
    path('profiles/', views.profiles_view, name='profiles'),
    path('profiles/create/', views.create_profile_view, name='create_profile'),
    path('profiles/<int:profile_id>/', views.profile_detail_view, name='profile_detail'),
    path('profiles/<int:profile_id>/edit/', views.edit_profile_view, name='edit_profile'),
    path('profiles/<int:profile_id>/delete/', views.delete_profile_view, name='delete_profile'),
    path('profiles/<int:profile_id>/permissions/', views.update_profile_permissions, name='update_permissions'),
    path('profiles/<int:profile_id>/fields/<str:module_name>/', views.get_module_fields, name='get_module_fields'),
    path('profiles/<int:profile_id>/data-filters/', views.manage_data_filter, name='manage_data_filter'),
    path('profiles/<int:profile_id>/dropdown-restrictions/', views.manage_dropdown_restriction, name='manage_dropdown_restriction'),
    path('model-fields/<str:module_name>/', views.get_model_fields_for_filter, name='get_model_fields_for_filter'),
    path('field-choices/<str:module_name>/<path:field_name>/', views.get_field_choices, name='get_field_choices'),
    path('auth-check/', views.auth_check_view, name='auth_check'),
    
    # Field Permissions
    path('field-permissions/', field_permissions_views.field_permissions_dashboard, name='field_permissions_dashboard'),
    path('field-permissions/matrix/', field_permissions_views.field_permissions_matrix, name='field_permissions_matrix'),
    path('field-permissions/data-filters/', field_permissions_views.data_filters_manager, name='data_filters_manager'),
    path('field-permissions/test/', field_permissions_views.test_user_permissions, name='test_user_permissions'),
    path('field-permissions/bulk-update/', field_permissions_views.bulk_update_permissions, name='bulk_update_permissions'),
    path('field-permissions/profile/<int:profile_id>/edit/', field_permissions_views.profile_field_editor, name='profile_field_editor'),
    path('field-permissions/data-filters/create/', field_permissions_views.create_data_filter, name='create_data_filter'),
    path('field-permissions/data-filters/<int:filter_id>/edit/', field_permissions_views.edit_data_filter, name='edit_data_filter'),
    path('field-permissions/data-filters/<int:filter_id>/delete/', field_permissions_views.delete_data_filter, name='delete_data_filter'),
    path('field-permissions/dropdowns/', field_permissions_views.dropdown_restrictions_manager, name='dropdown_restrictions_manager'),
    path('field-permissions/dropdowns/create/', field_permissions_views.create_dropdown_restriction, name='create_dropdown_restriction'),
    path('field-permissions/dropdowns/<int:restriction_id>/edit/', field_permissions_views.edit_dropdown_restriction, name='edit_dropdown_restriction'),
    path('field-permissions/dropdowns/<int:restriction_id>/delete/', field_permissions_views.delete_dropdown_restriction, name='delete_dropdown_restriction'),
]