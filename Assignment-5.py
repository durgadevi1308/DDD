"""Importing Necessary Packages"""
import random
import pandas as pd
from datetime import datetime
import requests
import re
from bs4 import BeautifulSoup


class MobileShowroom:
    """Offline Store"""
    def __init__(self,brand,model,search):
        self.brand=brand
        self.model=model
        self.search=search
        
    def launch(self):
        print("NEW LAUNCHES OF THE WEEK")
        nl=["Samsung","Xiaomi","Apple"]
        return f"{nl}"
    
    """Specifying the user requirements"""    
    def requirements(self,**kwargs):
        print("\nYOUR REQUIREMENTS")
        req=[]
        for key,value in kwargs.items():
            req.append("{} : {}".format(key,value))
        return f"{req}"
    
    """Have used match cases for finding the brands,
       if-elif-else clause for finding the models of the brands"""
    def mobile_key_specs(self):
        print("\nMOBILE OPTIONS BASED ON YOUR REQUIREMENT")
        print("Your choice of brand is:",self.brand)
        choice=self.brand
        match choice:
            case "Samsung":
                if self.model=="S23":
                    print("Your choice of model is:",self.model,"\nKEY SPECIFICATIONS:")
                    m={}
                    m["RAM|ROM"]="8 GB RAM|128 GB ROM"
                    m["Processor"]="Qualcomm Snapdragon 8 Gen 2|Octa core|3.36 GHz"
                    m["Camera"]="(50MP+10MP+12MP),12MP"
                    m["Display"]="6.1 inch Full, HD+Dynamic AMOLED 2X"
                    m["Battery"]="3900 mAh"
                    m["Price"]="46,999"
                    m["Variants"]="Cream,Green,Lavender"
                    return m
              
                elif self.model=="S24 Ultra":
                    print("Your choice of model is:",self.model,"\nKEY SPECIFICATIONS:")
                    m={}
                    m["RAM|ROM"]="12 GB RAM|512 GB ROM"
                    m["Processor"]="Snapdragon 8, Gen3, Octacore"
                    m["Camera"]="(200MP+0+12MP),12MP"
                    m["Display"]="6.8 inch, Dynamic LTPO 2X AMOLED"
                    m["Battery"]="6000 mAh"
                    m["Price"]="1,29,999"
                    m["Variants"]="Blue,Green,Orange"
                    return m   
           
                else:
                    print("Your choice of model is:",self.model)
                    return f"Sorry!!The mobile isn't available in this recent launch section. Please check with the other sections"
                
                    
            case "Xiaomi":
                if self.model=="11i Hypercharge":
                    print("Your choice of model is:",self.model,"\nKEY SPECIFICATIONS:")
                    m={}
                    m["RAM|ROM"]="6 GB RAM|128 GB ROM"
                    m["Processor"]="Mediatek DImensity 920|Octacore|2.5GHz "
                    m["Camera"]="(108MP+8MP+2MP),16MP"
                    m["Display"]="6.67 inch,Full HD+AMOLED Dot display"
                    m["Battery"]="4500 mAh"
                    m["Price"]="26,663"
                    m["Variants"]="Purple Mist,Pacific,Stealth"
                    return m
                   
                elif self.model=="12 Pro":
                    print("Your choice of model is:",self.model,"\nKEY SPECIFICATIONS:")
                    m={}
                    m["RAM|ROM"]="12 GB RAM|256 GB ROM"
                    m["Processor"]="Snapdragon 8 Gen 1|Octacore|3 GHz"
                    m["Camera"]="(50MP+50MP+50MP),32MP"
                    m["Display"]="6.73 inch,Full HD+ 2K+ AMOLED"
                    m["Battery"]="4600 mAh"
                    m["Price"]="84,999"
                    m["Variants"]="Black,Couture,Opera"
                    return m   
                
                else:
                    print("Your choice of model is:",self.model)
                    return f"Sorry!!The mobile isn't available in this recent launch section. Please check with the other sections"    
                    
                    
            case "Apple":
                if self.model=="iPhone 15":
                    print("Your choice of model is:",self.model,"\nKEY SPECIFICATIONS:")
                    m={}
                    m["RAM|ROM"]="12 GB RAM|128 GB ROM"
                    m["Processor"]="A16 Bionic Chip,6 Core processor|Hexacore"
                    m["Camera"]="(48MP+12MP),12MP"
                    m["Display"]="6.1 inch All Screen OLED Display"
                    m["Battery"]="6000 mAh"
                    m["Price"]="64,999"
                    m["Varaints"]="Pink,Yellow,Blue,Green"
                    return m
                    
                elif self.model=="iPhone15 Pro Max":
                    print("Your choice of model is:",self.model,"\nKEY SPECIFICATIONS:")
                    m={}
                    m["RAM|ROM"]="12 GB RAM|256 GB ROM"
                    m["Processor"]="A17 Pro Chip, 6 Core Processor|Hexacore"
                    m["Camera"]="(48MP+12MP+12MP),12MP"
                    m["Display"]="6.7 inch, All Screen OLED Display"
                    m["Battery"]="6000 mAh"
                    m["Price"]="1,48,900"
                    m["variants"]="White,Black,Blue"
                    return m 
                    
                else:
                    print("Your choice of model is:",self.model)
                    return f"Sorry!!The mobile isn't available in this recent launch section. Please check with other sections" 
                    
                    
            case _:
                return f"Your choice of model is:{self.model} \nSorry!! {self.model} is not found in recent launches. Please check with other sections"
            


    def taxes(self,price):
        print("\nTAXING CRITERIA")
        while True:
                try:
                    self.cgst=price*0.09
                    self.sgst=price*0.09
                    self.gst=self.cgst+self.sgst
                    return f"The CGST is {self.cgst}\nThe SGST is {self.sgst}\nThe total GST is:{self.gst}"
                    break 
                except Exception as e:
                    return f"ERROR OCCURRED!!!!\nPlease enter the valid amount"
                    break
                
    def other_accessories(self,t,b):
        print("\nOTHER ACCESSORIES")
        temp_gls=dict({"Gorilla Glass":450,"Anti Glare glass":500,"Privacy Tempered glass":350})
        bck_case=dict({"Flip Covered":400,"Sillicon Case":250,"Plastic Case":270,"Fabric Case":350})
        self.tg=t
        self.bc=b
        self.tp=temp_gls[t]
        self.bp=bck_case[b]
        return f"Price of {t} is: {self.tp} \nPrice of {b} is: {self.bp}"

    """Have used pandas to display the bill"""    
    def billing(self,cname,cphn):
        print("\n-----------------------------BILL----------------------------------------")
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        bill={
              "Items":[(self.brand,self.model,"Blue"),self.tg,self.bc],
              "Price":[129999,self.tp,self.bp],
              "CGST":[self.cgst,None,None],
              "SGST":[self.sgst,None,None],
              "Cost":[(129999+self.cgst+self.sgst),self.tp,self.bp],
              " Warranty":["1 Year",None,None]
        }
        df = pd.DataFrame(bill)
        print(df)
        tot= df["Cost"].sum()
        return f"\n\nTOTAL COST:{tot}\nNAME:{cname}\nPHONE:{cphn}\nDATE&TIME:{dt_string}"

    """Have used random library to generate 
    random scratch card numbers between 1 and 7"""    
    def scratch_card_voucher(self):
        print("\nSCRATCH CARD VOUCHER GIFT")
        num = random.randint(1, 7)
        match num:
            case 1:
                return f"Your random scratch card number is: {num}\nYour gift: 64 GB SD Card"
            case 2:
                return f"Your random scratch card number is: {num}\nYour gift: 20% Flat discount on your next purchase. To avail this bring your bill"
            case 3:
                return f"Your random scratch card number is: {num}\nYour gift: 450 rupees worth Tecno minipod (Olive Green)"
            case 4:
                return f"Your random scratch card number is: {num}\nYour gift: 8 GB HP Pendrive"    
            case 5:
                return f"Your random scratch card number is: {num}\nYour gift: 350 rupees worth PTron Headset"
            case _:
                return f"Your random scratch card number is: {num}\nYour gift: Scratch another card again"


    """Have Used Beautiful Soup to scrape the details 
       of a mobile from flipkart website"""            
    def online_store(self): 
        print("\n-----WELCOMING YOU TO THE FLIPKART ONLINE STORE-----")
        url = f'https://www.flipkart.com/search?q={self.search}'
        data=requests.get(url)
        soupobj=BeautifulSoup(data.content,features='lxml')

        choice=soupobj.find_all(string=re.compile(self.search))
        if choice:
            print("\nYayy!!Your choice of mobile is Found!!")
        else:
            print("\nOops!!Your choice of mobile is not Found")    
        print("If you want to order, visit our website to place the order")
        mobile=soupobj.find("div",{"class":"KzDlHZ"})
        specs=soupobj.find("ul",{"class":"G4BRas"})
        price=soupobj.find("div",class_="Nx9bqj _4b5DiR")
        delivery=soupobj.find("div",class_="k6cAZE dlFt9U")

        print("\nCHOICE OF MOBILE:",mobile.text)
        print("\nFEATURES AND SPECIFICATIONS:")
        for i in specs:
            print(i.text)
        print("\nDELIVERY TYPE:",delivery.text)
        for j in price:
            return f"\nPRICE:{j.text}"


ms=MobileShowroom("Samsung","S24 Ultra","motorola g-34")    
print(ms.launch())
print(ms.requirements(Pricerange="Under 1,50,000",Brand="Samsung"))
print(ms.mobile_key_specs())  
print(ms.taxes(129999))
print(ms.other_accessories("Gorilla Glass","Sillicon Case"))
print(ms.billing("Durga Swami","7339173893"))
print(ms.scratch_card_voucher())
print(ms.online_store())

    

             
