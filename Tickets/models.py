from django.db import models
from django.utils.translation import gettext_lazy as _

from Main.models import BaseModel
from Main.views import RandInt, RandString


class Ticket(BaseModel):
    ADMINNEW = '1'
    USERNEW = '2'
    PROGRESS = '3'
    ADMINANSWERED = '4'
    USERSEEN = '5'
    OPEN = '6'
    CLOSED = '7'

    STATUS_CHOICE = [
        (ADMINNEW,'تیکت ادمین'),
        (USERNEW,'تیکت کاربر'),
        (PROGRESS,'درحال بررسی'),
        (ADMINANSWERED,'پاسخ داده شده'),
        (USERSEEN,'دیده شده'),
        (OPEN,'باز'),
        (CLOSED,'بسته'),
    ]
    USER = '1'
    PROVIDER = '2'
    
    TYPE_CHOICE = [
        (USER,'خریدار'),
        (PROVIDER,'فروشنده'),
        
    ]


    STK = models.CharField(_("کد تیکت"), max_length=15,blank=True,null=True,unique=True)
    Team = models.ForeignKey("Admins.Team", verbose_name=_("تیم"), on_delete=models.CASCADE,blank=True,null=True,related_name='ticket_team')
    Personel = models.ForeignKey('Admins.Personel', verbose_name=_("پرسنل"), on_delete=models.CASCADE,blank=True,null=True)
    User = models.IntegerField(_("خریدار"),default=0)
    Provider = models.IntegerField(_("فروشنده"),default=0)
    Subject = models.CharField(_("موضوع"), max_length=300)
    Type = models.CharField(_("کاربر هدف"), max_length=50,default=USER,choices=TYPE_CHOICE)
    Status = models.CharField(_("وضعیت"), max_length=50,default=USERNEW,choices=STATUS_CHOICE)

    class Meta(BaseModel.Meta):
        verbose_name = _("Ticket")
        verbose_name_plural = _("Tickets")

    def __str__(self):
        return self.STK
    
    def save(self,*args, **kwargs):
        if not self.pk:
            self.STK = RandInt('STK')
        super(Ticket, self).save(*args, **kwargs)

class TicketMessage(BaseModel):
    USER = '1'
    PROVIDER = '2'
    ADMIN = '3'
    TYPE_CHOICE = [
        (USER,'خریدار'),
        (PROVIDER,'فروشنده'),
        (ADMIN,'ادمین')
    ]
    STM = models.CharField(_("شماره پیام"), max_length=15,blank=True,null=True,unique=True)
    Ticket = models.ForeignKey(Ticket, verbose_name=_("تیکت"), on_delete=models.CASCADE)
    Sender = models.CharField(_("فرستنده"), max_length=50,default=USER,choices=TYPE_CHOICE)
    Text = models.TextField(_("پیام"))
    Name = models.CharField(_("نام"), max_length=50)

    class Meta(BaseModel.Meta):
        verbose_name = _("TicketMessage")
        verbose_name_plural = _("TicketMessages")

    def __str__(self):
        return self.STM


    def save(self,*args, **kwargs):
        if not self.pk:
            self.STM = RandInt('STM')
        super(TicketMessage, self).save(*args, **kwargs)

class TicketFile(BaseModel):
    Message = models.ForeignKey(TicketMessage, verbose_name=_("پیام"), on_delete=models.CASCADE)
    File = models.FileField(_("فایل"), upload_to='Tickets/', max_length=100)

    class Meta(BaseModel.Meta):
        verbose_name = _("TicketFile")
        verbose_name_plural = _("TicketFiles")

    def __str__(self):
        return str(self.pk)

class TicketSwitch(BaseModel):
    TEAM = '1'
    BOTH = '2'
    ADMIN = '3'
    TYPE_CHOICE = [
        (TEAM,'تیم'),
        (BOTH,'هردو'),
        (ADMIN,'ادمین')
    ]
    STS = models.CharField(_("شماره  سوییچ"), max_length=15,blank=True,null=True,unique=True)
    Ticket = models.ForeignKey(Ticket, verbose_name=_("تیکت"), on_delete=models.CASCADE)
    OldTeam = models.ForeignKey("Admins.Team", verbose_name=_("تیم قدیم"), on_delete=models.CASCADE,blank=True,null=True,related_name='ot_switch_team')
    NewTeam = models.ForeignKey("Admins.Team", verbose_name=_("تیم جدید"), on_delete=models.CASCADE,blank=True,null=True,related_name='nt_switch_team')
    OldPersonel = models.ForeignKey('Admins.Personel', verbose_name=_("پرسنل قدیم"), on_delete=models.CASCADE,blank=True,null=True,related_name='op_switch_team')
    NewPersonel = models.ForeignKey('Admins.Personel', verbose_name=_("پرسنل جدید"), on_delete=models.CASCADE,blank=True,null=True,related_name='np_switch_team')
    Type = models.CharField(_("کاربر هدف"), max_length=50,default=ADMIN,choices=TYPE_CHOICE)


    class Meta(BaseModel.Meta):
        verbose_name = _("TicketSwitch")
        verbose_name_plural = _("TicketSwitchs")

    def __str__(self):
        return self.STS
    
    def save(self,*args, **kwargs):
        if not self.pk:
            self.STS = RandInt('STS')
        super(TicketSwitch, self).save(*args, **kwargs)