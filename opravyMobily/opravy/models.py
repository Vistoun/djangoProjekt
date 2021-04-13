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
     return "opravar/" + str(instance.id) + "/fotka/" + filename


class Opravar(models.Model):

    name = models.TextField(blank=True, null=False, verbose_name="Jmeno opraváře") 
    zamereni = models.CharField(max_length=20, choices=ZNACKY, blank=True, default="apple", help_text="Zadejte značku jednoho z výrobcu mobilů, které opravujete", verbose_name="Zaměření")
    bydliste = models.CharField(max_length=200, verbose_name="Bydliště")
    vyplata = models.IntegerField(blank=True, null=False, verbose_name="Výplata")
    foto = models.ImageField(upload_to=opravar_path, blank=True, null=True, verbose_name="Fotka")

    class Meta:
        ordering = ["name"]


    def __str__(self):
        return self.name


class Model(models.Model):
    
    name = models.CharField(max_length=200, null= False, verbose_name="Název")
    znacka = models.CharField(max_length=20, choices=ZNACKY, blank=True, default="apple", verbose_name="Výrobce")
    cena = models.IntegerField(blank=True, null=True, verbose_name="Cena")

    class Meta:
        ordering=["znacka"]

    def __str__(self):
        return f"{self.znacka} {self.name}"

class Oprava(models.Model):

    popis = models.TextField(blank=True, null= False, verbose_name="Popis zavady")
    opravar = models.ForeignKey(Opravar, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    cena = models.IntegerField(blank=True, null=False, verbose_name="Cena opravy")
    time = models.DateTimeField(auto_now=True)
    zakaznik = models.CharField(max_length=200, blank= True, null=True, verbose_name="Jméno a přijmení zákazníka")
    foto = models.ImageField(upload_to=oprava_path, blank=True, null=True, verbose_name="Fotka")

    class Meta:
        ordering = ["opravar"]


    def __str__(self):
        return f"{self.model} - {self.popis}"

#class Zakaznik(models.Model):