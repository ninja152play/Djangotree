from django.db import models
from django.urls import reverse


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название пункта")
    url = models.CharField(max_length=255, blank=True, verbose_name="Ссылка")
    named_url = models.CharField(max_length=100, blank=True, verbose_name="Имя ссылки")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="children")
    menu_name = models.CharField(max_length=50, verbose_name="Название меню")

    def __str__(self):
        return self.name

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url