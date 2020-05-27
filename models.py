from django.db import models
from django.utils import timezone
# Create your models here.

class RawCase(models.Model):
    case_id = models.CharField(max_length=20)  # 病例号——每个病例独一无二
    diagnosis = models.CharField(max_length=100)
    symptoms = models.CharField(max_length=200)  #病症
    prescription = models.CharField(max_length=200)
    photo_path = models.CharField(max_length=500,default="")

    class Meta:
        ordering = ('case_id',)

    def __str__(self):
        return self.case_id


class DiagnosticCase(models.Model):
    case_id = models.CharField(max_length=20) #病例号——每个病例独一无二
    #case_name = models.CharField(max_length=30,default="Unknown")#case 对应的文件名
    age = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('case_id',)

    def __str__(self):
        return self.case_id

class DiscriptionObject(models.Model):#描述对象
    object_id = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ('object_id',)

    def __str__(self):
        return self.name

class Symptoms(models.Model):#症状
    case_id = models.OneToOneField(DiagnosticCase, on_delete=models.CASCADE,primary_key=True)
    object1 = models.ForeignKey(DiscriptionObject, related_name='object1', on_delete=models.CASCADE,default="Unset")
    discription1 = models.CharField(max_length=20,default="Unset")
    object2 = models.ForeignKey(DiscriptionObject, related_name='object2', on_delete=models.CASCADE,default="Unset")
    discription2 = models.CharField(max_length=20,default="Unset")
    object3 = models.ForeignKey(DiscriptionObject, related_name='object3', on_delete=models.CASCADE,default="Unset")
    discription3 = models.CharField(max_length=20,default="Unset")
    object4 = models.ForeignKey(DiscriptionObject, related_name='object4', on_delete=models.CASCADE,default="Unset")
    discription4 = models.CharField(max_length=20,default="Unset")
    object5 = models.ForeignKey(DiscriptionObject, related_name='object5', on_delete=models.CASCADE,default="Unset")
    discription5 = models.CharField(max_length=20,default="Unset")
    object6 = models.ForeignKey(DiscriptionObject, related_name='object6', on_delete=models.CASCADE,default="Unset")
    discription6 = models.CharField(max_length=20,default="Unset")

    class Meta:
        ordering = ('case_id',)

    def __str__(self):
        return self.case_id.case_id


class Illness(models.Model):#诊断意见
    illness_id = models.CharField(max_length=20)
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ('illness_id',)

    def __str__(self):
        return self.name

class Diagnosis(models.Model):
    case_id = models.OneToOneField(DiagnosticCase, on_delete=models.CASCADE,primary_key=True)
    diagnose1 = models.ForeignKey(Illness, related_name='diagnose1', on_delete=models.CASCADE, default="Unset")
    diagnose2 = models.ForeignKey(Illness, related_name='diagnose2', on_delete=models.CASCADE, default="Unset")
    diagnose3 = models.ForeignKey(Illness, related_name='diagnose3', on_delete=models.CASCADE, default="Unset")

    class Meta:
        ordering = ('case_id',)

    def __str__(self):
        return self.case_id.case_id



class Order(models.Model):#医嘱里的每一条
    order_id = models.CharField(max_length=20)
    order =  models.CharField(max_length=40)

    class Meta:
        ordering = ('order_id',)

    def __str__(self):
        return self.order


class Prescription(models.Model): #医嘱
    case_id = models.OneToOneField(DiagnosticCase,on_delete=models.CASCADE)
    order1 = models.ForeignKey(Order, on_delete=models.CASCADE, default="Unset", related_name='order1')
    order2 = models.ForeignKey(Order, on_delete=models.CASCADE, default="Unset", related_name='order2')
    order3 = models.ForeignKey(Order, on_delete=models.CASCADE, default="Unset", related_name='order3')
    order4 = models.ForeignKey(Order, on_delete=models.CASCADE, default="Unset", related_name='order4')
    order5 = models.ForeignKey(Order, on_delete=models.CASCADE, default="Unset", related_name='order5')
    order6 = models.ForeignKey(Order, on_delete=models.CASCADE, default="Unset", related_name='order6')

    class Meta:
        ordering = ('case_id',)

    def __str__(self):
        return self.case_id.case_id


class Photo(models.Model):
    case_id = models.ForeignKey(DiagnosticCase, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img')
    num = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('case_id','num')

    def __str__(self):
        return self.case_id.case_id+'_P'+str(self.num)

# class QuestionPhoto(models.Model):
#     question

class SingleChoice(models.Model):
    question_id = models.PositiveIntegerField(default=0)
    question = models.CharField(max_length=50,default="Unset")
    choice1 = models.CharField(max_length=30,default="Unset")
    choice2 = models.CharField(max_length=30,default="Unset")
    choice3 = models.CharField(max_length=30,default="Unset")
    choice4 = models.CharField(max_length=30,default="Unset")
    correct_answer = models.CharField(max_length=6,default='Unset')
    question_image1 = models.ForeignKey(Photo,on_delete=models.CASCADE)

    class Meta:
        ordering = ('question_id',)

    def __str__(self):
        return self.question

class TrueOrFalse(models.Model):
    question_id = models.PositiveIntegerField(default=0)
    question = models.CharField(max_length=100,default="Unset")
    correct_answer = models.BooleanField(default=True)
    question_image1 = models.ImageField(upload_to="q_img")

    class Meta:
        ordering = ('question_id',)

    def __str__(self):
        return self.question

#记得admin里面要register一下