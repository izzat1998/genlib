from celery.schedules import crontab
from celery.task import periodic_task
from django.utils import timezone

from reg.models import SecurityNumber


@periodic_task(run_every=crontab(minute='*/5'))
def delete_old_foos():
    # Query all the foos in our database
    secure_numbers = SecurityNumber.objects.all()
    print(secure_numbers)
    # Iterate through them
    for secure_number in secure_numbers:

        # If the expiration date is bigger than now delete it
        if secure_number.expiration_date < timezone.now():
            secure_number.delete()
            # log deletion
    return "completed deleting foos at {}".format(timezone.now())
