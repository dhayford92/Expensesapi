from django.db import models
from authentication.models import User

class Source(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Income(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: ['-date']

    def __str__(self):
        return str(self.owner) + 's income'