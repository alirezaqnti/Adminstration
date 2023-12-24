from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from Main.models import BaseModel
from Main.views import RandInt, RandString


class TaskBaseModel(BaseModel):
    New = '1'
    Progress = '2'
    Confirmation = '3'
    Confirmed = '4'
    Rejected = '5'
    Declined = '6'

    STATUS_CHOICE = [
        (New,'جدید'),
        (Progress,'در حال اجرا'),
        (Confirmation,'در انتظار تایید'),
        (Confirmed,'تایید شده'),
        (Rejected,'رد شده'),
        (Declined,'لغو شده'),
    ]
    Title = models.CharField(_("عنوان"), max_length=300)
    DeadLine = models.DateTimeField(_("ددلاین"), auto_now_add=False,blank=True,null=True)
    Fulfilld = models.DateTimeField(_("تاریخ پایان"), auto_now_add=False,blank=True,null=True)
    Description = RichTextUploadingField(_("توضیحات"),blank=True,null=True)
    Report = models.TextField(_("گزارش"),max_length=500,blank=True,null=True)
    Status = models.CharField(_("وضعیت"), max_length=20,default=New,choices=STATUS_CHOICE)
    
    class Meta:
        abstract = True    


class Task(TaskBaseModel):
    STA = models.CharField(_("شماره تسک"), max_length=15,blank=True,null=True,unique=True)
    Owner = models.ForeignKey("Admins.Personel", verbose_name=_("کارفرما"), on_delete=models.CASCADE,related_name='owner_pers')
    Assigned_To = models.ForeignKey("Admins.Personel", verbose_name=_("محول شده"), on_delete=models.CASCADE,blank=True,null=True,related_name='assign_pers')
    Team = models.ForeignKey("Admins.Team", verbose_name=_("تیم"), on_delete=models.CASCADE,blank=True,null=True,related_name='task_team')
    

    class Meta(BaseModel.Meta):
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.Title
    
    def save(self,*args, **kwargs):
        if not self.pk:
            self.STA = RandInt('STA')
        super(Task, self).save(*args, **kwargs)


class SubTask(TaskBaseModel,MPTTModel):

    SST = models.CharField(_("شماره ساب تسک"), max_length=15,blank=True,null=True,unique=True)
    Task = models.ForeignKey(Task, verbose_name=_("تسک"), on_delete=models.CASCADE)   
    parent = TreeForeignKey(
            "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class Meta(BaseModel.Meta,MPTTModel.Meta):
        verbose_name = _("SubTask")
        verbose_name_plural = _("SubTasks")

    def __str__(self):
        return self.Title

    def save(self,*args, **kwargs):
        if not self.pk:
            self.SST = RandInt('SST')
        super(SubTask, self).save(*args, **kwargs)


class TaskFile(models.Model):
    T = '1'
    S = '2'

    TYPE_CHOICE = [
        (T,'تسک'),
        (S,'جزئیات')
    ]
    STF = models.CharField(_("شماره فایل"), max_length=15,blank=True,null=True,unique=True)
    Task = models.ForeignKey(Task, verbose_name=_("تسک"), on_delete=models.CASCADE,blank=True,null=True)
    Sub = models.ForeignKey(SubTask, verbose_name=_("ساب تسک"), on_delete=models.CASCADE,blank=True,null=True)
    File = models.FileField(_("فایل"), upload_to='Tasks/', max_length=150)
    Type = models.CharField(_("نوع"), max_length=50,default=T,choices=TYPE_CHOICE)
    class Meta:

        verbose_name = 'TaskFile'
        verbose_name_plural = 'TaskFiles'

    def __str__(self):
        return self.STF

    def save(self,*args, **kwargs):
        if not self.pk:
            self.STF = RandInt('STF')
        super(TaskFile, self).save(*args, **kwargs)