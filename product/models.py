from django.db import models
from django.db import models
from django_jalali.db import models as jmodels
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


# =======================================<< Brand >>=======================================
class Brand(models.Model):

    # ---------------------------------------
    class Name(models.TextChoices):
        #JAPAN
        SEIKO = 'سیکو', 'سیکو'
        ORIENT = 'ارینت', 'ارینت'
        CITIZEN = 'سیتیزن', 'سیتیزن'
        CASIO = 'کاسیو', 'کاسیو'
        G_SHOCK = 'جی شاک', 'جی شاک'
        # SWISS
        ROLEX = 'رولکس', 'رولکس'
        PATEK_PHILIPPE = 'پتک فیلیپ', 'پتک فیلیپ'
        OMEGA = 'امگا', 'امگا'
        TAG_HEUER = 'تگ هویر', 'تگ هویر'
        ROMANSON = 'رومانسون', 'رومانسون'
        FREDERIQUE_CONSTANT = 'فردریک کنستانت', 'فردریک کنستانت'
        # AMERICA
        FOSSIL = 'فسیل', 'فسیل'
        KENNETH_COLE = 'کنت کول', 'کنت کول'
        # GERMANY
        ESCADA = 'اسکادا', 'اسکادا'
        DUFA = 'دوفا', 'دوفا'
        # DANMARK
        SKAGEN = 'اسکاگن', 'اسکاگن'
        BESTDON = 'بستدان', 'بستدان'

    class Nationality(models.TextChoices):
        CHINA = 'CHINA', 'چین'
        SWITZERLAND = 'SWITZERLAND', 'سوئیس'
        JAPAN = 'JAPAN', 'ژاپن'
        AMERICA = 'AMERICA', 'آمریکا'
        DENMARK = 'DENMARK', 'دانمارک'
        ENGLAND = 'ENGLAND', 'انگلیس'
        ITALY = 'ITALY', 'ایتالیا'
        GERMANY = 'GERMANY', 'آلمان'
        AUSTRIA = 'AUSTRIA', 'اتریش'
        AUSTRALIA = 'AUSTRALIA', 'استرالیا'
        OTHER = 'OTHER', 'دیگر'

    # ---------------------------------------
    name = models.CharField(max_length=100, verbose_name='برند')
    persian_name = models.CharField(max_length=100, verbose_name='نام فارسی برند')
    nationality = models.CharField(max_length=50, verbose_name='ملیت')

    # ---------------------------------------
    objects = jmodels.jManager()

    # ---------------------------------------
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    # ---------------------------------------
    def __str__(self):
        return self.name


# =======================================<< Color >>=======================================
class Color(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام رنگ')
    value = models.CharField(max_length=50, blank=True, null=True, verbose_name='کد رنگ')

    # ---------------------------------------
    objects = jmodels.jManager()

    # ---------------------------------------
    class Meta:
        ordering = ['name']
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'

    # ---------------------------------------
    def __str__(self):
        return self.name


# =======================================<< Product >>=======================================
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Product.Status.PUBLISHED)


class Product(models.Model):

    # ---------------------------------------
    class Status(models.TextChoices):
        PUBLISHED = 'PB', 'Published'
        DRAFTED = 'DR', 'Drafted'
        REJECTED = 'RJ', 'Rejected'

    class GlassMaterial(models.TextChoices):
        ACRYLIC = 'آکریلیک', 'آکریلیک'
        MINERAL = 'منیرال', 'منیرال'
        HARD_MINERAL = 'منیرال سخت', 'منیرال سخت'
        SAPPHIRE = 'سافایر', 'سافایر'
        SAPPHIRE_CRYSTAL = 'سافایر کریستال', 'سافایر کریستال'
        RESISTANT_SAPPHIRE_CRYSTAL = 'کریستال یاقوت کبود', 'کریسال یاقوت کبود'
        PVC = 'پی وی سی', 'پی وی سی'
        OTHER = 'دیگر', 'دیگر'

    class StrapMaterial(models.TextChoices):
        LEATHER = 'چرم', 'چرم'
        STEEL = 'استیل', 'استیل'
        SILICONE = 'سیلیکون', 'سیلیکون'
        NYLON = 'نایلون', 'نایلون'
        CANVAS = 'پارچه', 'پارچه'
        TITANIUM = 'تیتانیوم', 'تیتانیوم'
        CERAMIC = 'سرامیک', 'سرامیک'
        ALUMINUM = 'آلومینیوم', 'آلومینیوم'
        SILVER = 'نقره', 'نقره'
        BRONZE = 'برنز', 'برنز'
        CARBON = 'کربن', 'کربن'
        BRASS = 'برنج', 'برنج'
        OTHER = 'دیگر', 'دیگر'

    class StrapType(models.TextChoices):
        OYSTER = 'صدفی', 'صدفی'
        JUBILEE = 'جوبیلی', 'جوبیلی'
        MESH = 'مشبک', 'مشبک'
        NATO = 'ناتو', 'ناتو'
        RUBBER = 'لاستیکی', 'لاستیکی'
        PERLON = 'پرلون', 'پرلون'
        CASUAL_LEATHER = 'چرم کژال', 'چرم کژال'
        ENGINEER = 'مهندسی', 'مهندسی'
        SAILCLOTH = 'پارچه بادبانی', 'پارچه بادبانی'
        ZULU = 'زولو', 'زولو'
        RALLY_LEATHER = 'چرم رالی', 'چرم رالی'
        AVIATION = 'خلبانی', 'خلبانی'
        OTHER = 'دیگر', 'دیگر'

    class Style(models.TextChoices):
        MILITARY = 'نظامی', 'نظامی'
        CLASSIC = 'کلاسیک', 'کلاسیک'
        RACING = 'مسابقه ای', 'مسابقه ای'
        DIVING = 'غواصی', 'غواصی'
        FIELD = 'جنگی', 'جنگی'
        FASHION = 'فشن', 'فشن'
        LUXURY = 'لاکچری', 'لاکچری'
        SMART = 'هوشمند', 'هوشمند'
        SPORT = 'اسپرت', 'اسپرت'
        PILOT = 'خلبانی', 'خلبانی'
        OFFICIAL = 'رسمی', 'رسمی'
        OTHER = 'دیگر', 'دیگر'

    class EngineType(models.TextChoices):
        MECHANICAL = 'مکانیکی', 'مکانیکی'
        AUTOMATIC = 'اتوماتیک', 'اتوماتیک'
        QUARTZ = 'کوارتز', 'کوارتز'
        OTHER = 'دیگر', 'دیگر'

    class DialType(models.TextChoices):
        Skeleton = 'اسکلتون', 'اسکلتون'
        OPEN_HEART = 'قلب باز', 'قلب باز'
        MINIMAL = 'مینیمال', 'مینیمال'

    class WaterResistance(models.TextChoices):
        ATM_1 = '1ATM', "1 ATM"
        ATM_3 = '3ATM', "3 ATM"
        ATM_5 = '5ATM', "5 ATM"
        ATM_10 = '10ATM', "10 ATM"
        ATM_20 = '20ATM', "20 ATM"
        NOT = "not", 'not'

    class Sex(models.TextChoices):
        MALE = 'مردانه', 'مردانه'
        FEMALE = 'زنانه', 'زنانه'
        SPORT = 'اسپرت', 'اسپرت'

    # ---------------------------------------
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', verbose_name='فروشنده',
                               default=1)

    model = models.CharField(max_length=250, verbose_name='مدل', null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_watched', verbose_name='برند')

    sex = models.CharField(max_length=50, choices=Sex.choices, verbose_name='جنسیت')

    style = models.CharField(max_length=100, choices=Style.choices, verbose_name='استابل')

    engine_type = models.CharField(max_length=100, choices=EngineType.choices, verbose_name='نوع موتور')
    dial_type = models.CharField(max_length=100, choices=DialType.choices, verbose_name='نوع صفحه')
    strap_type = models.CharField(max_length=100, choices=StrapType.choices, verbose_name='نوع بند')

    glass_material = models.CharField(max_length=100, choices=GlassMaterial.choices, verbose_name='جنس شیشه')
    strap_material = models.CharField(max_length=100, choices=StrapMaterial.choices, verbose_name='جنس بند')

    strap_color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name='straps',
                                    null=True, blank=True, verbose_name='رنگ بند')
    dial_color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name='dials',
                                   null=True, blank=True, verbose_name='رنگ صفحه')
    case_color = models.ForeignKey(Color, on_delete=models.SET_NULL, related_name='cases',
                                   null=True, blank=True, verbose_name='رنگ قالب')

    water_resistance = models.CharField(max_length=10, choices=WaterResistance.choices, verbose_name='میزان مقاومت در برابر آب')

    weight = models.PositiveIntegerField(default=0, verbose_name='وزن بر حسب گرم')

    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    off = models.PositiveIntegerField(default=0, verbose_name='درصد تخفیف')
    new_price = models.PositiveIntegerField(default=0, verbose_name='قیمت پس از تخفیف')
    stock = models.PositiveIntegerField(default=0, verbose_name='موجودی')

    slug = models.SlugField(max_length=250, unique=True, verbose_name='اسلاگ')

    # ---------------------------------------
    publish = jmodels.jDateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    create = jmodels.jDateTimeField(auto_now_add=True)
    update = jmodels.jDateTimeField(auto_now=True)

    # ---------------------------------------
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFTED, verbose_name='وضعیت')

    # ---------------------------------------
    objects = jmodels.jManager()
    published = PublishedManager()

    # ---------------------------------------
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    # ---------------------------------------
    def save(self, *args, **kwargs):
        self.new_price = (1-self.off / 100) * self.price
        super().save(*args, **kwargs)

    # ---------------------------------------
    def __str__(self):
        return f" ساعت مچی برند{self.brand} مدل {self.model} "


# =======================================<< Ticket >>=======================================
class Ticket(models.Model):

    # ---------------------------------------
    name = models.CharField(max_length=250, verbose_name='نام و نام انوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    subject = models.CharField(max_length=250, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')

    seen = models.BooleanField(default=False, verbose_name='دیده شده')

    # ---------------------------------------
    objects = jmodels.jManager()

    # ---------------------------------------
    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'

    # ---------------------------------------
    def __str__(self):
        return self.subject


# =======================================<< Comment >>=======================================
class Comment(models.Model):

    # ---------------------------------------
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name='محصول')

    # ---------------------------------------
    name = models.CharField(max_length=250, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    body = models.TextField(verbose_name='متن کامنت')

    create = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    update = jmodels.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ویرایش')

    active = models.BooleanField(default=False, verbose_name='وضعیت')

    # ---------------------------------------
    objects = jmodels.jManager()

    # ---------------------------------------
    class Meta:
        ordering = ['-create']
        indexes = [
            models.Index(fields=['-create'])
        ]
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    # ---------------------------------------
    def __str__(self):
        return f"{self.name}:{self.product}"
