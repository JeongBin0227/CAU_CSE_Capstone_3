from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beautyforme.settings")
import django
django.setup()
from cosmetic.models import *

urls = []

# 립/립스틱
urls.append("https://www.esteelauder.co.kr/products/649/")

# 립/리퀴드 립
urls.append("https://www.esteelauder.co.kr/products/648/")

# 립/립 글로스
urls.append("https://www.esteelauder.co.kr/products/647/")

# 아이/아이섀도우
urls.append("https://www.esteelauder.co.kr/products/636/")

# 아이/아이브로우
urls.append("https://www.esteelauder.co.kr/products/634/")

# 아이/아이라이너
urls.append("https://www.esteelauder.co.kr/products/635/")

# 아이/마스카라
urls.append("https://www.esteelauder.co.kr/products/637/")

# 페이스/파운데이션
urls.append("https://www.esteelauder.co.kr/products/643/")

# 페이스/컨실러
urls.append("https://www.esteelauder.co.kr/products/642/")

# 페이스/파우더
urls.append("https://www.esteelauder.co.kr/products/644/")

# 페이스/프라이머
urls.append("https://www.esteelauder.co.kr/products/1473/")

# 페이스/비비크림
urls.append("https://www.esteelauder.co.kr/products/12367/")

# 페이스/블러쉬
urls.append("https://www.esteelauder.co.kr/products/639/")

# 브러쉬&기타
urls.append("https://www.esteelauder.co.kr/products/12883/")

# 브러쉬&악세사리
urls.append("https://www.esteelauder.co.kr/products/12884/")

# 스킨케어/클레저&토너
urls.append("https://www.esteelauder.co.kr/products/684/")

# 스킨케어/리페어&세럼
urls.append("https://www.esteelauder.co.kr/products/689/")

# 스킨케어/로션&크림
urls.append("https://www.esteelauder.co.kr/products/688/")

# 스킨케어/페이스오일
urls.append("https://www.esteelauder.co.kr/products/14707/")

# 스킨케어/아이 케어
urls.append("https://www.esteelauder.co.kr/products/685/")

# 스킨케어/스페셜케어&마스크
urls.append("https://www.esteelauder.co.kr/products/687/")

cnt = 0
for url in urls:
    origin_url = "https://www.esteelauder.co.kr"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    main_html = urlopen(req).read()
    soup = BeautifulSoup(main_html, "html.parser")

    raws = soup.find_all("a", {"class": "product_brief__image-container"})
    product_additional_url = []
    product_names = []
    for raw in raws:
        j1 = str(raw).split('href=\"')
        j2 = j1[1]
        j3 = j2.split('\"')
        j4 = j3[0]
        product_additional_url.append(j4)
    
    for i in range(len(product_additional_url)):
        product_color_names = []
        product_color_values = []
        product_images = []

        product_url = 'https://www.esteelauder.co.kr' + product_additional_url[i]
        req = Request(product_url, headers={'User-Agent': 'Mozilla/5.0'})
        main_html = urlopen(req).read()
        soup = BeautifulSoup(main_html, "html.parser")

        if type(soup.find("h3", {"class": "product-full__title product_brief__sub-line"})) is not type(None):
            product_names.append(soup.find("h3", {"class": "product-full__title product_brief__sub-line"}).text)
        elif type(soup.find("h4", {"class": "product-full__title product_brief__sub-line"})) is not type(None):
            product_names.append(soup.find("h4", {"class": "product-full__title product_brief__sub-line"}).text)
        elif type(soup.find("h4", {"class": "product_brief__sub-header"})) is not type(None):
            product_names.append(soup.find("h4", {"class": "product_brief__sub-header"}).text)
        
        product_color_name_tags = str(soup.findAll("a", {"class": "swatch swatch--selected"}))
        if product_color_name_tags:
            product_color_name_tags = product_color_name_tags.split(',')
            for tag_content in product_color_name_tags:
                tmp1 = tag_content.split('name=\"')
                if len(tmp1) == 1:
                    product_color_names.append("None")
                else:
                    tmp2 = tmp1[1]
                    tmp3 = tmp2.split('\"')
                    tmp4 = tmp3[0]
                    product_color_names.append(tmp4)
        elif not product_color_name_tags:
            product_color_names.append("None")

        product_color_value_tags = str(soup.findAll("div", {"class": "swatch--1"}))
        if product_color_value_tags:
            product_color_value_tags = product_color_value_tags.split(',')
            for tag_content in product_color_value_tags:
                sharp_pos = tag_content.find("#")
                if len(tag_content[sharp_pos:sharp_pos+7]) is not 7:
                    product_color_values.append("None")
                else:
                    product_color_values.append(tag_content[sharp_pos:sharp_pos+7])
        elif not product_color_value_tags:
            product_color_values.append("None")

        product_color_values = product_color_values[len(product_color_values)-len(product_color_names):]

        product_image_tags = []
        tmp_color_tags = soup.findAll("div", {"itemprop": "color"})
        if tmp_color_tags:
            for tag_content in tmp_color_tags:
                str_tag_content = str(tag_content.findAll("meta", {"itemprop": "image"}))
                contnet_pos = str_tag_content.find('content')
                itemprop_pos = str_tag_content.find('itemprop')
                str_tag_content = str_tag_content[contnet_pos+9:itemprop_pos-2]
                product_image_tags.append(str_tag_content)
        else:
            product_image_tags.append("None")

        # 결과 확인
        for j in range(len(product_color_values)):
            cnt +=1
            try:
                stripped_product_name = product_names[i].strip()
                stripped_product_color_name = product_color_names[j].strip()
                print(Cosmetic.objects.get(product=Product.objects.get(brand=Brand.objects.get(brand_name="에스티 로더 (ESTEE LAUDER)"), product_name=stripped_product_name),
                                           type_name=stripped_product_color_name))
                print("이미 존재하는 제품입니다.")
            except:
                try:
                    stripped_product_name = product_names[i].strip()
                    stripped_product_color_name = product_color_names[j].strip()
                    stripped_product_color_value = product_color_values[j].strip()
                    stripped_product_image = product_image_tags[j].strip()
                    cosmetic = Cosmetic(product = Product.objects.get(brand=Brand.objects.get(brand_name="에스티 로더 (ESTEE LAUDER)"), product_name=stripped_product_name),
                                        type_name = stripped_product_color_name,
                                        rgb_value = stripped_product_color_value, 
                                        image_link = stripped_product_image)
                    cosmetic.save()
                except:
                    print(stripped_product_name)
                    print("Error")
print(cnt)