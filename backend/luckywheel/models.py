from email.policy import default
from django.db import models
from colorfield.fields import ColorField



awards=(
        ('پوچ','پوچ'),
        ('تخفیف','تخفیف'),
        ('شارژ کیف پول','شارژ کیف پول'),
    )

class Award(models.Model):
   
    text=models.CharField(max_length=100,verbose_name='متن',unique=True)
    color=ColorField(default="#000000",verbose_name="رنگ")
    value=models.IntegerField(verbose_name='مقدار')
    lucky_award=models.CharField(max_length=20,choices=awards,verbose_name='جایزه') 
    
    class Meta:
        verbose_name="جایزه"
        verbose_name_plural="جایزه" 

    
    def __str__(self)->str:
        return "{}--{}--{}".format(self.text,self.value,self.lucky_award)

    def get_award(self)->str:
        return "{} تومان {}".format(self.value,self.lucky_award)    


class SpacialAward(models.Model):

    count_number=models.IntegerField(verbose_name='شماره')
    value=models.IntegerField(verbose_name='مقدار')
    lucky_award=models.CharField(max_length=20,choices=awards,verbose_name='جایزه') 

    class Meta:
        verbose_name="جایزه ویژه"
        verbose_name_plural="جایزه های ویژه"

    def get_award(self)->str:
        return "{} تومان {}".format(self.value,self.lucky_award)


class HideAward(models.Model):

    value=models.IntegerField(verbose_name='مقدار')
    lucky_award=models.CharField(max_length=20,choices=awards,verbose_name='جایزه') 

    class Meta:
        verbose_name="جایزه مخفی"
        verbose_name_plural="جایزه های مخفی" 

    def get_award(self)->str:
        return "{} تومان {}".format(self.value,self.lucky_award)    
