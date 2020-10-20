from django.contrib.auth import get_user_model
User = get_user_model()

adminuser = User.objects.filter(username__icontains='adminuser')
if adminuser:
    pass
else:
    User.objects.create_superuser('adminuser', 'dev@email.io', '1234567')
