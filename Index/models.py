from django.db import models



class Picture(models.Model):
   
    description = models.TextField( verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Foto", blank=True, null=True)
  
    class Meta:
        verbose_name="Foto"
        verbose_name_plural="Foto"
        
    def __str__(self):
        return self.name
    

class Therapist (models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulo")
    image = models.ImageField(verbose_name="Foto", blank=True, null=True)
    description = models.TextField()
    
    class Meta:
        verbose_name="Terapeuta"
        verbose_name_plural = "Terapeutas"
    
    def __str__(self):
        self.name
        
        
class Therapy(models.Model):
    name = models.CharField(max_length=255 , verbose_name = "Nombre")
    image = models.ImageField(verbose_name="Foto", blank=True, null=True)
    description = models.TextField()
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    duration = models.IntegerField (verbose_name="Duracion (Tiempo) ")
    price = models.IntegerField(verbose_name="Precio")
    
    class Meta:
            verbose_name="Terapia"
            verbose_name_plural="Terapias"
        
    def __str__(self):
        return self.name
    
    