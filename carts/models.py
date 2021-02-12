from abc import abstractclassmethod
from django.db import models
from training.models import Practice
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save, post_save, m2m_changed


User = settings.AUTH_USER_MODEL

# Create your models here.


class CartManager(models.Manager):

    def new_or_get(self, request):
        """
        Method returning either the already created cart or a new cart if not exits
        """
        cart_id = request.session.get("cart_id", None)
        print(cart_id)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            new_obj = True
            cart_obj = Cart.objects.new(user=request.user)
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    practices = models.ManyToManyField(Practice, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    due_date = models.DateTimeField(null=True, blank=True)
    total_duration = models.IntegerField(default=0)

    objects = CartManager()

    def __str__(self):
        return "Cart id :%s" % (self.id)

    def get_absolute_url(self):
        # helping to return the full path to the object according the primary key
        return reverse("practice-details", kwargs={"pk": self.pk})


def m2m_save_cart_receiver(sender, instance, action, *args, **kwargs):
    """
    Method used in order to manage cart information before saving cart 
    information
    """
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        # according the list of actions listed above we calculate the total duration and save it
        practices = instance.practices.all()
        total_duration = 0
        for practice in practices:
            total_duration += practice.duration_in_minutes
        instance.total_duration = total_duration
        instance.save()


# Saving cart once many to many relationship has changed
m2m_changed.connect(m2m_save_cart_receiver, sender=Cart.practices.through)
