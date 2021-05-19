from django.db import models

ZNACKY = (
        ('apple', 'Apple'),
        ('samsung', 'Samsung'),
        ('huawei', 'Huawei'),
        ('xiaomi', 'Xiaomi'),
)  


def oprava_path(instance, filename):
     return "oprava/" + str(instance.id) + "/fotka_rozbita/" + filename

def opravar_path(instance, filename):
     return "opravar/" + str(instance.name) + "/fotka/" + filename

def model_path(instance, filename):
     return "modely/" + str(instance.name) + filename  

def brand_path(instance, filename):
     return "modely/" + str(instance.name) + filename          


class Brand(models.Model):
    
    name = models.CharField(max_length=200, null= False, verbose_name="Název")
    foto = models.ImageField(upload_to=brand_path, blank=True, null=True, verbose_name="Fotka")


    class Meta:
        ordering = ["name"]


    def __str__(self):
        return f"{self.name}"


class Model(models.Model):
    
    name = models.CharField(max_length=200, null= False, verbose_name="Název")
    znacka = models.ForeignKey(Brand, on_delete=models.CASCADE)
    fotka = models.ImageField(upload_to=model_path, blank=True, null=True, verbose_name="Fotka")
    cena_baterka = models.IntegerField(blank=True, null=True, verbose_name="Cena výměneny baterky")
    cena_displej = models.IntegerField(blank=True, null=True, verbose_name="Cena výměneny displeje")
    cena_stav_a =  models.IntegerField(blank=True, null=True, verbose_name="Výkupní cena stav A")
    popis = models.TextField(blank=True, null=False, verbose_name="Popis produktu") 
    
    class Meta:
        ordering=["znacka"]

    def __str__(self):
        return f"{self.znacka} {self.name}"


class Opravar(models.Model):
    
    name = models.TextField(blank=True, null=False, verbose_name="Jmeno opraváře") 
    zamereni = models.CharField(max_length=20, choices=ZNACKY, blank=True, default="apple", help_text="Zadejte značku jednoho z výrobcu mobilů, které opravujete", verbose_name="Zaměření")
    foto = models.ImageField(upload_to=opravar_path, blank=True, null=True, verbose_name="Fotka")

    class Meta:
        ordering = ["name"]


    def __str__(self):
        return self.name


class Oprava(models.Model):
    
    popis = models.TextField(blank=True, null= False, verbose_name="Popis zavady")
    opravar = models.ForeignKey(Opravar, on_delete=models.CASCADE)
    
    cena = models.IntegerField(blank=True, null=False, verbose_name="Cena opravy")
    zakaznik = models.CharField(max_length=200, blank= True, null=True, verbose_name="Jméno a přijmení zákazníka")
    foto = models.ImageField(upload_to=oprava_path, blank=True, null=True, verbose_name="Fotka")

    class Meta:
        ordering = ["opravar"]


    def __str__(self):
        return f"{self.model} - {self.popis}"