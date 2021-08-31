from django.db import models



class Picture(models.Model):
   
    description = models.TextField( verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Foto", blank=True, null=True)
  
    class Meta:
        verbose_name="Foto"
        verbose_name_plural="Foto"
        
    def __str__(self):
        return self.name