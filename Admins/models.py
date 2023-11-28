from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from Main.models import Address, BaseModel
from Main.views import RandInt, RandString


class Personel(BaseModel):
    Fabulous = '1'
    Happy = "2"
    Normal = "3"
    OK = "4"
    Bored = "5"
    DND = "6"
    Angry = "7"
    Depressed = "8"

    MOOD_CHOICE = [
        (Fabulous, 'خیلی خوشحال'),
        (Happy, "خوشحال"),
        (Normal, "معمولی"),
        (OK, "بی تفاوت"),
        (Bored, "بی حوصله"),
        (DND, "مزاحمم نشید"),
        (Angry, "عصبانی"),
        (Depressed, "افسرده"),
    ]
    
    New = '1'
    Working = '2'
    Suspended = '3'
    Fired = '4'
    Left = '5'
    Vacation = '6'

    STATUS_CHOICE = [
        (New,'جدید'),
        (Working,'مشغول به کار'),
        (Suspended,'تعلیق'),
        (Fired,'اخراج'),
        (Left,'ترک مجموعه'),
        (Vacation,'مرخصی'),
    ]

    SPE = models.CharField(_("کد پرسنلی"), max_length=15,blank=True,null=True,unique=True)
    FirstName = models.CharField(_("نام"), max_length=50)
    LastName = models.CharField(_("نام خانوادگی"), max_length=50)
    Phone = models.CharField(_("شماره همراه"), max_length=13)
    NationalID = models.CharField(_("کد ملی"), max_length=10)
    Email = models.EmailField(_("ایمیل"), max_length=254)
    Address = models.ForeignKey(Address, verbose_name=_("آدرس"), on_delete=models.CASCADE)
    Team = models.ForeignKey("Team", verbose_name=_("تیم"), on_delete=models.CASCADE,blank=True,null=True)
    JobTitle = models.CharField(_("عنوان شغلی"), max_length=100)
    # Access = 
    Status = models.CharField(_("وضعیت"), max_length=20,default=New,choices=STATUS_CHOICE)
    Mood = models.CharField(_("مود رفتاری"), max_length=20,default=OK,choices=MOOD_CHOICE)
    Joined = models.DateField(_("تاریخ شروع همکاری"), auto_now_add=False)
    Left = models.DateField(_("تاریخ پایان همکاری"), auto_now_add=False)
    class Meta(BaseModel.Meta):
        verbose_name = _("Personel")
        verbose_name_plural = _("Personels")
    
    def __str__(self):
        return self.FirstName + self.LastName
    
    def save(self,*args, **kwargs):
        if not self.pk:
            self.SPE = RandInt('SPE')
        super(Personel, self).save(*args, **kwargs)

class Team(BaseModel,MPTTModel):
    ST = models.CharField(_("کد تیم"), max_length=15,blank=True,null=True,unique=True)
    Name = models.CharField(_("نام تیم"), max_length=50)
    parent = TreeForeignKey(
            "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    Description = models.TextField(_("توضیحات"),max_length=600)
    # Access = 

    class Meta(BaseModel.Meta):
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.Name

    def save(self,*args, **kwargs):
        if not self.pk:
            self.ST = RandInt('ST')
        super(Team, self).save(*args, **kwargs)

class OffDayRequest(BaseModel):
    New = '1'
    Progress = '2'
    Declined = '3'
    Accepted = '4'

    STATUS_CHOICE = [
        (New,'جدید'),
        (Progress,'در حال بررسی'),
        (Declined,'رد شده'),
        (Accepted,'تایید شده'),
    ]

    WithPayment = '1'
    WithoutPayment = '2'

    TYPE_CHOICE = [
        (WithPayment,"استحقاقی"),
        (WithoutPayment,"بدون حقوق")
    ]

    SOD = models.CharField(_("شماره درخواست"), max_length=15,blank=True,null=True,unique=True)
    Personel = models.ForeignKey(Personel, verbose_name=_("پرسنل"), on_delete=models.CASCADE)
    StartDate = models.DateTimeField(_("تاریخ شروع"), auto_now_add=False)
    EndDate = models.DateTimeField(_("تاریخ پایان"), auto_now_add=False)
    Status = models.CharField(_("وضعیت"), max_length=50,default=New,choices=STATUS_CHOICE)
    Type = models.CharField(_("نوع"), max_length=50,default=WithPayment,choices=TYPE_CHOICE)


    class Meta(BaseModel.Meta):
        verbose_name = 'OffDayRequest'
        verbose_name_plural = 'OffDayRequests'

    def __str__(self):
        return self.SOD
    
    def save(self,*args, **kwargs):
        if not self.pk:
            self.SOD = RandInt('SOD')
        super(OffDayRequest, self).save(*args, **kwargs)
