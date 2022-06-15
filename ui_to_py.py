
from PyQt5 import uic


with open("ui/anasayfaUI.py", "w", encoding='utf-8') as fout:
    uic.compileUi('ui/anasayfa2.ui', fout)

with open("ui/ayarlarUI.py", "w", encoding='utf-8') as fout:
    uic.compileUi('ui/ayarlar.ui', fout)

with open("ui/emanetVermeUI.py", "w", encoding='utf-8') as fout:
    uic.compileUi('ui/emanetVerme.ui', fout)

with open("ui/kitapKayitUI.py", "w", encoding='utf-8') as fout:
    uic.compileUi('ui/kitapKayit.ui', fout)

with open("ui/uyeKayitUI.py", "w", encoding='utf-8') as fout:
    uic.compileUi('ui/uyeKayit.ui', fout)

with open("ui/raporlarUI.py", "w", encoding='utf-8') as fout:
    uic.compileUi('ui/raporlar.ui', fout)

with open("ui/confirmationUI.py", "w", encoding='utf-8') as fout:
    uic.compileUi('ui/confirmation.ui', fout)

