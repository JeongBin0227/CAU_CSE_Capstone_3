import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beautyforme.settings")
import django
django.setup()
from cosmetic.models import *

if __name__=='__main__':
    Small_Category(big_category=Big_Category.objects.get(big_category="기초"), small_category="스킨").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="기초"), small_category="로션").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="기초"), small_category="에센스").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="기초"), small_category="크림").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="기초"), small_category="미스트").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="기초"), small_category="메이크업픽서").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="기초"), small_category="페이스오일").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="기초"), small_category="토너/필링패드").save()

    Small_Category(big_category=Big_Category.objects.get(big_category="베이스"), small_category="메이크업베이스").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="베이스"), small_category="톤업크림").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="베이스"), small_category="베이스프라이머").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="베이스"), small_category="포인트프라이머").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="베이스"), small_category="파운데이션").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="베이스"), small_category="비비크림").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="베이스"), small_category="씨씨크림").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="베이스"), small_category="쿠션타입").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="베이스"), small_category="컨실러").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="베이스"), small_category="팩트").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="베이스"), small_category="파우더").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="베이스"), small_category="트윈케익").save()

    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="립스틱").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="립글로스/락커").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="립틴트").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="립밤").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="립라이너").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="아이라이너-펜슬&젤").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="아이라이너-리퀴드").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="마스카라").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="픽서/영양제").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="아이섀도우").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="아이브로우-펜슬").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="아이브로우-파우더").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="아이브로우-마스카라&리퀴드").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="하이라이터").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="쉐딩").save()
    Small_Category(big_category=Big_Category.objects.get(big_category="색조"), small_category="블러셔").save()