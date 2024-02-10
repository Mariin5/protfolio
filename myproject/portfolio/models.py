from django.db import models
from django.utils import timezone 
import datetime

#作品のカテゴリ
class Category(models.Model):
    category_choice=[
        ("自然","自然"),
        ("建築","建築"),
        ("食べ物","食べ物"),
        ("乗り物","乗り物"),
        ("その他","その他"),
    ]
    category = models.CharField(verbose_name="カテゴリ", max_length=5 ,choices=category_choice,unique=True)
    created_at  = models.DateTimeField(verbose_name="登録日時", default=timezone.now)
    updated_at  = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.category

#撮影場所
class Area(models.Model):
    area_choice=[
        ('北海道', '北海道'),
        ('青森県', '青森県'),
        ('岩手県', '岩手県'),
        ('宮城県', '宮城県'),
        ('秋田県', '秋田県'),
        ('山形県', '山形県'),
        ('福島県', '福島県'),
        ('茨城県', '茨城県'),
        ('栃木県', '栃木県'),
        ('群馬県', '群馬県'),
        ('埼玉県', '埼玉県'),
        ('千葉県', '千葉県'),
        ('東京都', '東京都'),
        ('神奈川県', '神奈川県'),
        ('新潟県', '新潟県'),
        ('富山県', '富山県'),
        ('石川県', '石川県'),
        ('福井県', '福井県'),
        ('山梨県', '山梨県'),
        ('長野県', '長野県'),
        ('岐阜県', '岐阜県'),
        ('静岡県', '静岡県'),
        ('愛知県', '愛知県'),
        ('三重県', '三重県'),
        ('滋賀県', '滋賀県'),
        ('京都府', '京都府'),
        ('大阪府', '大阪府'),
        ('兵庫県', '兵庫県'),
        ('奈良県', '奈良県'),
        ('和歌山県', '和歌山県'),
        ('鳥取県', '鳥取県'),
        ('島根県', '島根県'),
        ('岡山県', '岡山県'),
        ('広島県', '広島県'),
        ('山口県', '山口県'),
        ('徳島県', '徳島県'),
        ('香川県', '香川県'),
        ('愛媛県', '愛媛県'),
        ('高知県', '高知県'),
        ('福岡県', '福岡県'),
        ('佐賀県', '佐賀県'),
        ('長崎県', '長崎県'),
        ('熊本県', '熊本県'),
        ('大分県', '大分県'),
        ('宮崎県', '宮崎県'),
        ('鹿児島県', '鹿児島県'),
        ('沖縄県', '沖縄県'),
        ('台湾', '台湾'),
        ('香港', '香港'),
        ('マカオ', 'マカオ'),
        ('韓国', '韓国'),
        ('マレーシア', 'マレーシア'),
        ('タイ', 'タイ'),
        ('オーストリア', 'オーストリア'),
        ('ドイツ', 'ドイツ'),
        ]
    area        = models.CharField(verbose_name="撮影場所", max_length=10, choices=area_choice,unique=True)
    created_at  = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    updated_at  = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.area
    
#作品撮影日（カレンダー）
class DateModel(models.Model):
    date_field = models.DateField()
    
    def __str__(self):
        return self.date_field
        
#作品
class Photo(models.Model):
    image           = models.ImageField(verbose_name="作品", upload_to="media/portfolio/photo/")
    name            =models.CharField(verbose_name="作品名", max_length=20, null=True,blank=True)
    category        = models.ManyToManyField(Category,verbose_name="カテゴリ")
    area            = models.ManyToManyField(Area, verbose_name="撮影場所")
    date            = models.DateField()
    detail            =models.CharField(verbose_name="詳細", max_length=100,blank=True)
    created_at      = models.DateTimeField(verbose_name="投稿日時", default=timezone.now)
    updated_at      = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return str(self.category)
    
    def __str__(self):
        return str(self.area)
    
    def __str__(self):
        return str(self.image)


