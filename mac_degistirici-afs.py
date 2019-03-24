import subprocess # terminalde komut calistirmak icin kullanilan kutuphane
import optparse # kullanicidan girdi almak icin kullanilan kutuphane
import re # ifconfig in ciktisinda arama yapmak icin kullandigimiz kutuphane--regex101.com--

# kullanicidan girdiler almak icin kullanacagimiz fonksiyon

def kullanici_girdisi():
    parse_object=optparse.OptionParser()
# girdi objesi olusturduk.
    parse_object.add_option("-i", "-- interface", dest="interface", help="interface to change")
# objemize kullanicin girecegi interface secenegini ekleyip yardim ve dest degerlerini belirttik
    parse_object.add_option("-m","--mac", dest="mac_address", help="new mac address")
# objemize girilecek mac adresi secenegini ekledik.
    return parse_object.parse_args()
# alinan degerleri dondurduk.

#terminalde komutlari calistirip maci degistirecek olan fonksiyon

def mac_degistir(interface, mac_address):
    subprocess.call(["ifconfig", interface, "down"])
# terminalde interface i kapadik
    subprocess.call(["ifconfig" , interface, "hw", "ether", mac_address])
# kullanicidan aldigimiz degerleri terminalde mac adresini degistiren komuta ekledik
    subprocess.call(["ifconfig", interface, "up"])
# terminalde interface i actik

# mac adresinin degisip degismedigini kontrol eden fonksiyon

def kontrol_et(interface):
    ifconfig= subprocess.check_output(["ifconfig", interface])
# ifconfig diye bir degisken tanimlayip terminalde ifconfig+interface ciktisini degiskene atadik
    new_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)
# regex kutuphanesiyle ifconfig in icinde mac adresini bulduk ve new_mac e atadik

# regex bize herzaman dogru sonucu vermeyebilir. bu yuzden sonuc alip almadigimizi kontrol etmeliyiz.

    if new_mac :
     # metod string dondurmedigi icin gruba atiyoruz.
        return new_mac.group(0)
    else:
        return None
print("AFS mac degisitirici basladi... ")

(girdi,arguments)= kullanici_girdisi()

# kullanici girdilerini girdi adli degiskene atadik

mac_degistir(girdi.interface, girdi.mac_address)

# mac adresini degistiren fonksiyonun icine kullanici girdilerini yazip calistirdik

son_mac = kontrol_et(girdi.interface)

# mac in degisip degismedigini kontrol icin ifconfigin ciktisndaki mac adresini son_mac diye bir degiskene atadik

# son_mac in kullanicinin girdigi adrese esit olup olmadigini kontrol edip cikti veren kosul yapisi
if son_mac==girdi.mac_address:
    print("Basarili")

else:
    print("Hatali")

# kullanim= python mac_degistirici-afs.py -i {interface} -m {mac adresi}
# ornek= python mac_degistirici-afs.py -i wlan0 -m 12:12:12:12:12:12
#--------------- ahmetfurkansonmez12@gmail.com ----------------------------