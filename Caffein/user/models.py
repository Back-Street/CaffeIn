from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from store.models import Store

class CaffeInUserManager(BaseUserManager):
    use_in_migrations = True    

    # 유저생성 시 실행되는 func
    def create_user(self, user_id, name, password=None):
        if not user_id:
            raise ValueError("user_id를 입력해주세요")
        if not name:
            raise ValueError("이름을 입력해주세요")

        user = self.model(
            user_id=user_id,
            name=name,
        )
        # password hash및 유저 save
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    # super-user 생성 func
    def create_superuser(self, user_id, name, password=None):

        user = self.model(
            user_id=user_id,
            name=name,
            )   
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        
        # password hash및 유저 save
        user.set_password(password)
        user.save(using=self._db)
        
        return user


class CaffeInUser(AbstractBaseUser):
    
    class Meta:
        db_table = 'users'
        verbose_name = '카페인 유저'
        verbose_name_plural = '카페인 유저들'

    objects = CaffeInUserManager()  # 헬퍼 클래스 지정
    
    # 식별자들
    user_id = models.CharField(unique=True, max_length=20, verbose_name='아이디')
    uid = models.CharField(
        primary_key=True,
        unique=True,
        max_length=100,
        verbose_name='유저 UID'
    ) # uid는 firebase noti를 위해서 firebase 내부에서 자체 생성하려고 합니다.

    # 개인정보
    name = models.CharField(max_length=10, verbose_name='이름')
    # birth = models.DateField(verbose_name='생년월일')
    # phone = models.CharField(max_length=20, verbose_name='전화번호')
    # email = models.EmailField('이메일', unique=True)
    likes = models.ManyToManyField(to=Store,related_name='likers')
    
    # 생성시간
    date_joined = models.DateTimeField(verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    
    # permission
    is_owner = models.BooleanField(default=False) # 카페사장님인지 check
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['name']  # 필수로 받는 요소

    def __str__(self):
        return self.user_id

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Label):
        return True