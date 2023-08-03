from django.db import models

class Advertisments(models.Model):
    titel = models.CharField("заголовок", max_length=50)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("торг", help_text="Отметьте, если торг уместен")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Advertisments(id={self.id}, title={self.titel}, price={self.price})"
    
    class Meta:
        db_table = 'advertisements'
    
    

