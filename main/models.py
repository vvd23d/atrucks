from django.db import models


class Numbering(models.Model):
    kod = models.CharField(max_length=3, verbose_name='Код')
    fr = models.IntegerField(verbose_name='От')
    to = models.IntegerField(verbose_name='До')
    capacity = models.IntegerField(verbose_name='Емкость')
    operator = models.CharField(max_length=100, verbose_name='Оператор')
    region = models.CharField(max_length=100, verbose_name='Регион')

    def __str__(self):
        return self.kod

    class Meta:
        verbose_name = 'Нумерация'
        verbose_name_plural = u'Нумерации'
        ordering = ('kod',)
