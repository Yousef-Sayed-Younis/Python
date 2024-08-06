from requests_html import HTMLSession

urlList = ['https://www.amazon.com/gp/slredirect/picassoRedirect.html/ref=pa_sp_atf_aps_sr_pg1_1?ie=UTF8&adId=A00929693U5HVOTSDN7AM&url=%2FHP-15-Notebook-6405U-AllyFlex%2Fdp%2FB08PRZGB5V%2Fref%3Dsr_1_2_sspa%3Fcrid%3D2R2ILX3B100EQ%26dchild%3D1%26keywords%3Dlaptop%26qid%3D1611153174%26sprefix%3Dla%252Caps%252C303%26sr%3D8-2-spons%26psc%3D1%26smid%3DA254Q68O1TCVS&qualifier=1611153174&id=4973731835922615&widgetName=sp_atf',
'https://www.amazon.com/Acer-Display-Graphics-Keyboard-A515-43-R19L/dp/B07RF1XD36/ref=sr_1_3?crid=2R2ILX3B100EQ&dchild=1&keywords=laptop&qid=1611153174&sprefix=la%2Caps%2C303&sr=8-3',
'https://www.amazon.com/Acer-Predator-i7-10750H-Dual-Channel-PH315-53-72XD/dp/B08842D7JS/ref=sr_1_4?crid=2R2ILX3B100EQ&dchild=1&keywords=laptop&qid=1611153174&sprefix=la%2Caps%2C303&sr=8-4']

def getPrice(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1, timeout=8)

    try:
        product = {
            'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
            'price': r.html.xpath('//*[@id="priceblock_ourprice"]', first= True).text,
        }
        
        print(product)
        return product
    
    except:
        pass


productsList = [] 
for url in urlList:
    productsList.append(getPrice(url))

print(productsList)