#!/usr/bin/env python
# coding: utf-8

# In[95]:


#importando bibliotecas
import requests
from bs4 import BeautifulSoup
import os
import numpy as np


#********************************FUNCOES************************************************************

#FUNCAO 1 - AUTOMATIZACAO PARA EXTRAIR IMAGENS DO SITE burst.shopify
#obs para a imagem tipo glacier nao ha tantas opcoes - entao ficara para outra funcao
def download_image_website(pasta, url_main):
    
    #diretorio onde deve ser salvo os arquivos
    pasta_completa = os.path.join('/home/rafael/Python/projetos/image_classification/primeiro_projeto_coursera/base_dados_web_scraping', pasta)
    os.chdir(pasta_completa)
    
    #verificando se o link possui informacoes
    r = requests.get(url_main)
    
    #lendo as infoormacoes e textos do link
    soup = BeautifulSoup(r.text, 'html.parser')
    
    #procurando todas setencas que possui no texto `img
    images = soup.find_all('img')

    #laco  de repeticao para salvar todas as imagens
    for image in images:
        
        print(image['alt'],image['src'])
        
        #atribuindo nome da imagem e link para as variaveis name e link
        name = image['alt']
        link = image['src']

        #salvando a imagem
        with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
            img = requests.get(link)
            f.write(img.content)
    
   
    pages = np.arange(2, 41,1)
    
    #fazendo um laco de repeticao para repetir avancar nas proximas 40 pages para baicar as imagens
    for page in pages:
        
        #separando o link
        lista = url_main.split('?')
        #construindo novamente o link para com o numero da 'page'
        url = lista[0] + '?page=' + page + '&' + lista[1]
        
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        images = soup.find_all('img')

        for image in images:
            print(image['alt'],image['src'])

            name = image['alt']
            link = image['src']

            with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
                img = requests.get(link)
                f.write(img.content)
        
        
#FUNCAO 2 - AUTOMATIZACAO PARA EXTRAIR IMAGENS DE ALGUNS SITES PARA GLACIER
def download_image_website_glacier(url_main, i):
    
    pasta_completa = os.path.join('/home/rafael/Python/projetos/image_classification/primeiro_projeto_coursera/base_dados_web_scraping/glacier')
    os.chdir(pasta_completa)
    
    r = requests.get(url_main)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    images = soup.find_all('img')

    for image in images:
        if  (image['src'].__contains__('jpg') or image['src'].__contains__('png')) and  (image['src'].__contains__('https') or image['src'].__contains__('http')) :
            
            print(image['src'])
            i = i + 1
            print(i)
            name = 'glacier_' + str(i)
            link = image['src']

            with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
                img = requests.get(link)
                f.write(img.content)
                
    return str(i)
                
            
#FUNCAO 3 - AUTOMATIZACAO PARA EXTRAIR IMAGENS DO GOOGLE IMAGENS PARA GLACIER
def download_image_website_glacier_google(url_main, i):
    
    pasta_completa = os.path.join('/home/rafael/Python/projetos/image_classification/primeiro_projeto_coursera/base_dados_web_scraping/glacier')
    os.chdir(pasta_completa)
    
    r = requests.get(url_main)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    images = soup.find_all('img')
    for image in images:
        i = i + 1 
        if (image['src'].__contains__('https') or image['src'].__contains__('http')) :
            
            print(image['src'])
            print(i)
            name = 'glacier_' + str(i)
            link = image['src']

            with open(name.replace(' ', '-').replace('/', '') + '.jpg', 'wb') as f:
                img = requests.get(link)
                f.write(img.content)
                
    return str(i)



#*********************************************************************************************************



#***************************************-----//------*****************************************************



#********************************EXTRAINDO IMAGENS FUNCAO 1***********************************************

#colocando em um dicionario os links para as imagens tipo (forest, buildings, mountain, sea, street)
dic_page_1 = {'forest' : 'https://burst.shopify.com/photos/search?q=forest',
              'buildings' : 'https://burst.shopify.com/photos/search?q=buildings',
              'mountain' : 'https://burst.shopify.com/photos/search?q=mountain', 
              'sea' : 'https://burst.shopify.com/photos/search?q=ocean',
              'street' : 'https://burst.shopify.com/photos/search?q=street'}


#laco de repeticao chamar FUNCAO 1
for pasta in dic_page_1.keys():
    download_image_website(pasta, dic_page_1[pasta])

#*********************************************************************************************************



#********************************EXTRAINDO IMAGENS FUNCAO 2***********************************************


#colocando em um dicionario os links para as imagens do tipo glacier (varios links)
dic = {'glacier_1' : 'https://stock.adobe.com/br/search?filters%5Bcontent_type%3Aphoto%5D=1&filters%5Bcontent_type%3Aillustration%5D=1&filters%5Bcontent_type%3Azip_vector%5D=1&filters%5Bcontent_type%3Avideo%5D=0&filters%5Bcontent_type%3Atemplate%5D=0&filters%5Bcontent_type%3A3d%5D=0&filters%5Bcontent_type%3Aaudio%5D=0&filters%5Binclude_stock_enterprise%5D=0&filters%5Bis_editorial%5D=0&filters%5Bfree_collection%5D=0&filters%5Bcontent_type%3Aimage%5D=1&k=glacier&order=relevance&safe_search=1&search_type=freebr-asset-click&asset_id=515666417',
       'glacier_2' : 'https://www.istockphoto.com/es/search/2/image?phrase=glacier&irgwc=1&cid=IS&utm_medium=affiliate_SP&utm_source=FreeImages&clickid=2LbQlQyVkxyNRG4SXLQ6Hw7xUkAxyW1-9wiR0k0&utm_term=glacier&utm_campaign=home_home_searchbar-popup&utm_content=270498&irpid=246195',
       'glacier_4' : 'https://unsplash.com/s/photos/Glacier',
       'glacier_5' : 'https://www.lifeofpix.com/search/glacier?',
       'glacier_6' : 'https://stock.adobe.com/br/search/free?k=glacier&search_type=usertyped',
       'glacier_7' : 'https://burst.shopify.com/photos/search?q=glacier',
       'glacier_9' : 'https://www.google.com/search?q=glacier&sxsrf=ALiCzsZUtX'}

#laco de repeticao chamar FUNCAO 2
i = 0
for nome_link in dic.keys():
    i = i + 1
    i = download_image_website_glacier(dic[nome_link], i)
    i = int(i)


#*********************************************************************************************************
 
    
    
#********************************EXTRAINDO IMAGENS FUNCAO 3***********************************************


#colocando em um dicionario os links para as imagens do tipo glacier (links google)
dic = {'g_1' : 'https://www.google.com/search?q=glacier&sxsrf=ALiCzsZUtXSs9jzxlA-PnZ3ksdZWa8zygw:1670106487264&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj_76O_v977AhUzH7kGHVuaDgwQ_AUoAXoECAEQAw&biw=1517&bih=700&dpr=0.9',
       'glacier_2' : 'https://www.google.com/search?q=glacier&tbm=isch&hl=pt-BR&chips=q:glacier,online_chips:alaska+glacier+bay:uVPB5l7NWEY%3D,online_chips:park:OFc69DG75_o%3D&sa=X&ved=2ahUKEwj0m5Ha0N77AhVQBLkGHdR7AuUQ4lYoAHoECAEQKA&biw=1501&bih=700',
       'glacier_4' : 'https://www.google.com/search?q=glacier&tbm=isch&hl=pt-BR&chips=q:glacier,online_chips:alaska+glacier+bay:uVPB5l7NWEY%3D,online_chips:park:OFc69DG75_o%3D,online_chips:national:OFc69DG75_o%3D&sa=X&ved=2ahUKEwjIuq_k0N77AhWxNbkGHWFpB-wQ4lYoAHoECAEQKw&biw=1501&bih=700',
       'glacier_5' : 'https://www.google.com/search?q=glacier&tbm=isch&hl=pt-BR&chips=q:glacier,online_chips:alaska+glacier+bay:uVPB5l7NWEY%3D,online_chips:park:OFc69DG75_o%3D,online_chips:national:OFc69DG75_o%3D,online_chips:princess+cruise:NPLIYQYpq-A%3D&sa=X&ved=2ahUKEwj0sL3y0N77AhXPN7kGHQsmDi0Q4lYoBHoECAEQNg&biw=1501&bih=700',
       'glacier_6' : 'https://www.google.com/search?q=geleiras&tbm=isch&ved=2ahUKEwjY1qCL0d77AhVSAtQKHf9TBeIQ2-cCegQIABAA&oq=geleiras&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgjECc6CAgAEIAEELEDOgcIIxDqAhAnOgQIABBDUPUJWOkpYPMqaAFwAHgAgAGgAYgB8wiSAQMwLjmYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCsABAQ&sclient=img&ei=6d-LY5i-PNKE0Ab_p5WQDg&bih=700&biw=1501&hl=pt-BR',
       'glacier_7' : 'https://www.google.com/search?q=geleiras&tbm=isch&hl=pt-BR&chips=q:geleira,g_1:wallpaper:lXcCtdzEY9I%3D&sa=X&ved=2ahUKEwi8jfCO0d77AhXkCbkGHWgDC_MQ4lYoAXoECAEQJw&biw=1501&bih=700',
       'glacier_9' : 'https://www.google.com/search?q=geleiras&tbm=isch&hl=pt-BR&chips=q:geleira,g_1:wallpaper:lXcCtdzEY9I%3D,online_chips:neve:H28Rj6BO-tU%3D&sa=X&ved=2ahUKEwiJ_PiW0d77AhXNHLkGHbg5B5QQ4lYoBnoECAEQNA&biw=1501&bih=700'}

#laco de repeticao chamar FUNCAO 3
i = 300
for nome_link in dic.keys():
    i = i + 1
    i = download_image_website_glacier_google(dic[nome_link], i)
    i = int(i)

    
#*********************************************************************************************************


