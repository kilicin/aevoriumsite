from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Servers, Balances, Users, Profile


@receiver(post_save, sender=Servers)
def create_new_server(sender, instance, created, **kwargs):
    if created:
        users = Users.objects.all()
        balances_to_create = [
            Balances(user=user, server=instance, amount=0) for user in users
        ]
        Balances.objects.bulk_create(balances_to_create)

@receiver(post_save, sender=Users)
def create_new_user(sender, instance, created, **kwargs):
    if created:
        servers = Servers.objects.all()
        balances_to_create = [
            Balances(user=instance, server=server, amount=0) for server in servers
        ]
        Balances.objects.bulk_create(balances_to_create)
        Profile.objects.create(name=instance, donateBalance=0)