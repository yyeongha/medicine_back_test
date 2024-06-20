from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Group, Permission
from django.db import models

# Create your models here.
class Drug(models.Model):
    """ Drug Model Definition """
    drug_no = models.CharField(max_length=20, primary_key=True)
    drug_name = models.CharField(max_length=200)
    drug_name_en = models.CharField(max_length=200)
    drug_material = models.CharField(max_length=50)
    drug_company = models.CharField(max_length=200)
    drug_shape = models.CharField(max_length=20)
    drug_color = models.CharField(max_length=100)
    drug_print_front = models.CharField(max_length=100, null=True, blank=True)
    drug_print_back = models.CharField(max_length=100, null=True, blank=True)
    drug_line_front = models.CharField(max_length=20, null=True, blank=True)
    drug_line_back = models.CharField(max_length=20, null=True, blank=True)
    drug_price_amount = models.FloatField()
    drug_price_unit = models.CharField(max_length=20)
    drug_price = models.IntegerField()
    drug_illness = models.CharField(max_length=20)
    drug_img_path = models.CharField(max_length=400)

    class Meta:
        """ Meta class """
        db_table = 'drug'
        managed = True 

    def __str__(self):
        return self.drug_name


# db에서 drug_images 테이블 사라짐..

# class DrugImage(models.Model):
#     """ Drug Image Model Definition """
#     drug_image_id = models.AutoField(primary_key=True)
#     drug_no = models.ForeignKey(Drug, on_delete=models.CASCADE, db_column='drug_no')
#     drug_imgkey = models.CharField(max_length=200)

#     class Meta:
#         """ Meta class """
#         db_table = 'drug_images'
#         verbose_name_plural = 'Drug Images'
#         managed = True # FIXME: Change this to False if you want to use the existing table

#     def __str__(self):
#         return f"{self.drug_no.drug_name} - Image"




class Search(models.Model):
    """ Search Model Definition """
    search_id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=36)
    drug_no = models.ForeignKey(Drug, on_delete=models.CASCADE, db_column='drug_no')
    drug_code = models.CharField(max_length=20)
    search_ip = models.CharField(max_length=20)
    search_date = models.CharField(max_length=100)
    drug_name = models.CharField(max_length=200)
    search_response = models.CharField(max_length=100)

    class Meta:
        """ Meta class """
        db_table = 'search'
        verbose_name_plural = 'Search'
        managed = True # FIXME: Change this to False if you want to use the existing table

    def __str__(self):
        return f"{self.search_id} - {self.drug_no.drug_name}"

class DrugDetail(models.Model):
    """ Drug Detail Model Definition """
    customer_id = models.CharField(max_length=36)
    drug_no = models.CharField(max_length=20)
    drug_code = models.CharField(max_length=20, null=True, blank=True)
    drug_name = models.CharField(max_length=200)

    class Meta:
        """ Meta class """
        db_table = 'drug_details'
        verbose_name_plural = 'Drug Details'
        managed = True # FIXME: Change this to False if you want to use the existing table

    def __str__(self):
        return self.drug_name
    
class CustomUserManager(BaseUserManager):
    """ Custom User Manager Definition """
    def create_user(self, username, email=None, password=None, **extra_fields):
        """ Create and return a user with an email, username, and password """
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """ Create and return a user with superuser permissions """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.create_user(username, email, password, **extra_fields)
        # 기본값 설정
        Customer.objects.create(user=user, sex='Not specified', age=0)
        return user

# 여기 수정함
class User(AbstractUser):
    """ Custom User Model Definition """
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)
    objects = CustomUserManager()


class Customer(models.Model):
    """ Customer Model Definition """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    sex = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username
