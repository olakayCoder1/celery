from celery import shared_task
from django.contrib.auth import get_user_model


User = get_user_model()




@shared_task(bind=True)
def client_mail(self):
    users = User.objects.all()
    for user in users:
        print(user)
        print("Mail send to user")
        """ 
        Sending mail with celery
        """
    return "Done"