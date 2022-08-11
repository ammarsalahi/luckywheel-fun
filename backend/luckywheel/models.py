from email.policy import default
from django.db import models
from colorfield.fields import ColorField





class LuckyAward(models.Model):
    awards= (
        ('پوچ','پوچ'),
        ('تخفیف','تخفیف'),
        ('شارژ کیف پول','شارژ کیف پول'),
    )

    text=models.CharField(max_length=100,verbose_name='متن',unique=True)
    color=ColorField(default="#000000",verbose_name="رنگ")
    value=models.IntegerField(verbose_name='مقدار')
    lucky_award=models.CharField(max_length=20,choices=awards,verbose_name='جایزه') 
    active=models.BooleanField(default=False,verbose_name="فعال")

    class Meta:
        verbose_name="جایزه"
        verbose_name_plural="جایزه" 

    def __str__(self)->str:
        return "{}--{}--{}".format(self.text,self.value,self.lucky_award)

    def get_award(self)->str:
        return "{} تومان {}".format(self.value,self.lucky_award)    



