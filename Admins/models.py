import jdatetime
from django.contrib.auth.models import Group, Permission, User
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from Main.models import Address, BaseModel
from Main.views import RandInt, RandString


class Personel(User):
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
    Phone = models.CharField(_("شماره همراه"), max_length=13)
    NationalID = models.CharField(_("کد ملی"), max_length=10)
    BirthDate = models.CharField(_("تاریخ تولد"), max_length=50,)
    Picture = models.ImageField(_("تصویر پروفایل"), upload_to='Admins/', max_length=500)
    Address = models.ForeignKey(Address, verbose_name=_("آدرس"), on_delete=models.CASCADE,blank=True,null=True)
    Team = models.ForeignKey("Team", verbose_name=_("تیم"), on_delete=models.CASCADE,blank=True,null=True,related_name='pers_team')
    JobTitle = models.CharField(_("عنوان شغلی"), max_length=100,blank=True,null=True)
    Status = models.CharField(_("وضعیت"), max_length=20,default=New,choices=STATUS_CHOICE)
    Mood = models.CharField(_("مود رفتاری"), max_length=20,default=OK,choices=MOOD_CHOICE)
    Joined = models.DateField(_("تاریخ شروع همکاری"), auto_now_add=True,blank=True,null=True)
    Left = models.DateField(_("تاریخ پایان همکاری"), auto_now_add=False,blank=True,null=True)



    USERNAME_FIELD = "Phone"
    class Meta(User.Meta):
        verbose_name = _("Personel")
        verbose_name_plural = _("Personels")
    
    def __str__(self):
        return self.first_name + self.last_name
    
    def save(self,*args, **kwargs):
        if not self.pk:
            self.SPE = RandInt('SPE')
        super(Personel, self).save(*args, **kwargs)
    def toJson(self):
        
        res =  {
            'SPE': self.SPE,
            'Name': f'{self.first_name} {self.last_name}',
            'Phone': self.Phone,
            'NationalID': self.NationalID,
            'Address': self.Address,
            
            'JobTitle': self.JobTitle,
            'Status': self.Status,
            'Mood': self.Mood,
            'Joined': self.Joined,
            'LastLogin': self.last_login,
            'Left': self.Left,
        }
        try:
            res['Team'] = self.Team.Name
            res['Team_id'] = self.Team.id
        except:
            pass
        return res

class Education(BaseModel):
    Personel = models.ForeignKey(Personel, verbose_name=_("پرسنل"), on_delete=models.CASCADE,related_name='edu_personel')
    Title = models.CharField(_("عنوان"), max_length=300)
    Institude = models.CharField(_("موسسه/دانشگاه"), max_length=200)
    StartDate = models.CharField(_("تاریخ شروع"), max_length=50)
    EndDate = models.CharField(_("تاریخ پایان"), max_length=50)
    

    class Meta:
        verbose_name = _("education")
        verbose_name_plural = _("educations")

    def __str__(self):
        return self.Title


class JobEXP(BaseModel):
    Personel = models.ForeignKey(Personel, verbose_name=_("پرسنل"), on_delete=models.CASCADE,related_name='exp_personel')
    Position = models.CharField(_("موقعیت شغلی"), max_length=300)
    Company = models.CharField(_("شرکت"), max_length=200)
    StartDate = models.CharField(_("تاریخ شروع"), max_length=50)
    EndDate = models.CharField(_("تاریخ پایان"), max_length=50)
    

    class Meta:
        verbose_name = _("JobEXP")
        verbose_name_plural = _("JobEXPs")

    def __str__(self):
        return self.Position

class Team(BaseModel,MPTTModel):
    ST = models.CharField(_("کد تیم"), max_length=15,blank=True,null=True,unique=True)
    Name = models.CharField(_("نام تیم"), max_length=50)
    parent = TreeForeignKey(
            "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    Description = models.TextField(_("توضیحات"),max_length=600)
    Access = models.ForeignKey(Group, verbose_name=_("دسترسی"), on_delete=models.CASCADE,blank=True,null=True)

    class Meta(BaseModel.Meta):
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.Name

    def save(self,*args, **kwargs):
        if not self.pk:
            self.ST = RandInt('ST')
        super(Team, self).save(*args, **kwargs)

    def toJson(self):
        P = self.parent.Name if self.parent != None else '-'
        A = self.Access.name if self.Access != None else '-'
        D = jdatetime.date.fromgregorian(date=self.Created)
        return {
            'ST': self.ST,
            'Name': self.Name,
            'Parent': P,
            'Description': self.Description,
            'Access': A,
            'Active': str(self.Active),
            'Created': str(D)
        }

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
    Personel = models.ForeignKey(Personel, verbose_name=_("پرسنل"), on_delete=models.CASCADE,related_name='offreq_personel')
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
