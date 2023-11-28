from django.db import models
from django.utils.translation import gettext_lazy as _

from .views import RandInt, RandString


class BaseModel(models.Model):
    Created = models.DateTimeField(auto_now_add=True)
    Modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['Created']


class City(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    Active = models.BooleanField(_("فعال"), default=True)

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.title


class Address(BaseModel):  # جدول مربوط به ادرس های کاربر
    Personel = models.ForeignKey('Admins.Personel', verbose_name=_("پرسنل"), on_delete=models.CASCADE)
    Title = models.CharField(_("عنوان آدرس"), max_length=100)  # عنوان آدرس
    Phone = models.CharField(_("شماره همراه"), max_length=11)  # شماره تلفن گیرنده
    State = models.ForeignKey(
        City,
        verbose_name=_("استان"),
        related_name="state_city",
        on_delete=models.CASCADE,
    )  # استان
    City = models.ForeignKey(
        City, verbose_name=_("شهر"), related_name="city_city", on_delete=models.CASCADE
    )  # شهر
    PostalAddress = models.CharField(_("آدرس پستی"), max_length=500)  # ادرس پستی
    PostalCode = models.CharField(_("کد پستی"), max_length=10)  # کد پستی
    Number = models.CharField(_("پلاک"), max_length=4)  # پلاک
    Unit = models.CharField(_("واحد"), max_length=5, blank=True)  # واحد
    Active = models.BooleanField(_("فعال"), default=True)

    class Meta:
        verbose_name_plural = "آدرس"

    def toJson(self):
        return {
            "addressTitle": self.Title,
            "User": self.User.FirstName + self.User.LastName,
            "User_id": self.User.pk,
            "Name": self.Name,
            "Phone": self.Phone,
            "State": self.State,
            "City": self.City,
            "PostalAddress": self.PostalAddress,
            "PostalCode": self.PostalCode,
            "Number": self.Number,
            "Unit": self.Unit,
            "Active": self.Active,
        }


class Questonnair(BaseModel):
    POLL = '1'
    QUESTIONNAIR = '2'

    TYPE_CHOICE = [
        (POLL,'نظرسنجی'),
        (QUESTIONNAIR,'پرسشنامه')
    ]
    SQ = models.CharField(_("شماره پرسشنامه"), max_length=15,blank=True,null=True,unique=True)
    Form = models.TextField(_("فرم"))
    DefaultForm = models.TextField(_("فرم پیشفرض"))
    Creator = models.ForeignKey("Admins.Personel", verbose_name=_("ایجاد کننده"), on_delete=models.CASCADE)
    DeadLine = models.DateTimeField(_("ددلاین"), auto_now_add=False,blank=True,null=True)
    Team = models.ForeignKey("Admins.Team", verbose_name=_("تیم"), on_delete=models.CASCADE,blank=True,null=True)
    Type = models.CharField(_("نوع"), max_length=50,default=POLL,choices=TYPE_CHOICE)


    class Meta(BaseModel.Meta):
        verbose_name = _("Questonnair")
        verbose_name_plural = _("Questonnairs")

    def __str__(self):
        return self.SQ

    def save(self,*args, **kwargs):
        if not self.pk:
            self.SQ = RandInt('SQ')
        super(Questonnair, self).save(*args, **kwargs)


class Respondent(BaseModel):

    SQR = models.CharField(_("شماره پاسخ"), max_length=15,blank=True,null=True,unique=True)
    Questonnair = models.ForeignKey(Questonnair, verbose_name=_("پرسشنامه"), on_delete=models.CASCADE)
    Form = models.TextField(_("فرم"))
    Personel = models.ForeignKey("Admins.Personel", verbose_name=_("کارمند"), on_delete=models.CASCADE)

    class Meta(BaseModel.Meta):
        verbose_name = _("Respondent")
        verbose_name_plural = _("Respondents")

    def __str__(self):
        return self.SQR

    def save(self,*args, **kwargs):
        if not self.pk:
            self.SQR = RandInt('SQR')
        super(Respondent, self).save(*args, **kwargs)