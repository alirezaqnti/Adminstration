from django.db import models
from django.utils.translation import gettext_lazy as _

from Main.models import BaseModel
from Main.views import RandInt, RandString


class ChatThread(BaseModel):
    P2P = '1'
    GROUP = '2'

    TYPE_CHOICE = [
        (P2P,'شخصی'),
        (GROUP,'گروهی'),
    ]
    SCT = models.CharField(_("کد چت"), max_length=15,blank=True,null=True,unique=True)
    Team = models.ForeignKey("Admins.Team", verbose_name=_("تیم"), on_delete=models.CASCADE,blank=True,null=True,related_name='thread_team')
    Type = models.CharField(_("نوع"), max_length=50,default=P2P,choices=TYPE_CHOICE)

    class Meta(BaseModel.Meta):
        verbose_name = _("ChatThread")
        verbose_name_plural = _("ChatThreads")

    def __str__(self):
        return self.SCT
    
    def save(self,*args, **kwargs):
        if not self.pk:
            self.SCT = RandInt('SCT')
            print('RAND:',self.SCT)
        super(ChatThread, self).save(*args, **kwargs)


class ChatParticipant(BaseModel):
    Thread = models.ForeignKey(ChatThread, verbose_name=_("چت"), on_delete=models.CASCADE)
    Personel = models.ForeignKey("Admins.Personel", verbose_name=_("پرسنل"), on_delete=models.CASCADE,)
    # Access

    class Meta(BaseModel.Meta):
        verbose_name = _("chatParticipant")
        verbose_name_plural = _("chatParticipants")

    def __str__(self):
        return self.Personel.SPE
    

class ChatMessage(BaseModel):
    
    SCM = models.CharField(_("شماره پیام"), max_length=15,blank=True,null=True,unique=True)
    Thread = models.ForeignKey(ChatThread, verbose_name=_("چت"), on_delete=models.CASCADE)
    Participant = models.ForeignKey(ChatParticipant, verbose_name=_("عضو"), on_delete=models.CASCADE)
    Text = models.TextField(_("پیام"))
    Seen = models.BooleanField(_("دیده شده"),default=False)
    Name = models.CharField(_("نام"), max_length=50)

    class Meta(BaseModel.Meta):
        verbose_name = _("ChatMessage")
        verbose_name_plural = _("ChatMessages")

    def __str__(self):
        return self.SCM


    def save(self,*args, **kwargs):
        if not self.pk:
            self.SCM = RandInt('SCM')
        super(ChatMessage, self).save(*args, **kwargs)


class ChatFile(BaseModel):
    Message = models.ForeignKey(ChatMessage, verbose_name=_("پیام"), on_delete=models.CASCADE)
    File = models.FileField(_("فایل"), upload_to='Chats/', max_length=100)

    class Meta:
        verbose_name = _("ChatFile")
        verbose_name_plural = _("ChatFiles")

    def __str__(self):
        return str(self.pk)


class ThreadLog(BaseModel):
    Thread = models.ForeignKey(ChatThread, verbose_name=_("چت"), on_delete=models.CASCADE)
    Participant = models.ForeignKey(ChatParticipant, verbose_name=_("عضو"), on_delete=models.CASCADE)
    Action = models.CharField(_("اکشن"), max_length=100)
    

    class Meta:
        verbose_name = _("ThreadLog")
        verbose_name_plural = _("ThreadLogs")

    def __str__(self):
        return str(self.pk)
    

class MessageLog(BaseModel):
    Message = models.ForeignKey(ChatMessage, verbose_name=_("پیام"), on_delete=models.CASCADE)
    Participant = models.ForeignKey(ChatParticipant, verbose_name=_("عضو"), on_delete=models.CASCADE)
    Action = models.CharField(_("اکشن"), max_length=100)

    class Meta:
        verbose_name = _("MessageLog")
        verbose_name_plural = _("MessageLogs")

    def __str__(self):
        return str(self.pk)
    




