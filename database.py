import sys
from datetime import datetime
import time, math
from barcode import EAN13, EAN8, writer
from barcode.writer import ImageWriter
import barcode
from io import BytesIO
from PyQt5 import QtCore
from PyQt5.QtCore import QVariant

from messageBox import msg
import sqlite3, pandas as pd, sqlalchemy
conn = sqlite3.connect('Otomasyon.sqlite')
curs = conn.cursor()

def tableWidgetResize(tableWidget: object, cols: list, blank=12):
    try:
        wid = tableWidget.width() - (tableWidget.verticalHeader().width() + tableWidget.verticalScrollBar().width()+blank)
        commonValue = wid / sum(cols)
        for i, col in enumerate(cols):
            tableWidget.setColumnWidth(i, int(round(col*commonValue,0)))
    except Exception as E:
        print("Fonk: tableWidgetResize  \tHata: ", E)


class Db:
    def __init__(self):
        self.cameId                 = 0
        self.maxDayBooksStay        = 7    # gün
        self.maxNumberOfBooksGiven  = 3    # adet
        self.byteImg                = None

        IdInfo = " INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE"
        self.createTable("YazarTablosu", "yazarId"+IdInfo, "YazarAdi TEXT NOT NULL UNIQUE")
        self.createTable("BolumTablosu", "bolumId"+IdInfo, "Bolum TEXT NOT NULL UNIQUE")
        self.createTable("RafTablosu", "rafId"+IdInfo, "RafNo TEXT NOT NULL UNIQUE")
        self.createTable("KategoriTablosu", "kategoriId"+IdInfo, "Kategori TEXT NOT NULL UNIQUE")
        self.createTable("EmanetTablosu", "emanetId"+IdInfo,
                         "KitapId INTEGER NOT NULL",
                         "UyeId INTEGER NOT NULL",
                         "VerilisTarihi TEXT NOT NULL",
                         "MaxKalmaSuresi INTEGER NOT NULL",
                         "DonusTarihi TEXT",
                         "FOREIGN KEY(KitapId) REFERENCES KitapTablosu(kitapId)")
        self.createTable("UyeTablosu", "uyeId"+IdInfo,
                        "UyeTipi INTEGER NOT NULL",
                        "Durum INTEGER NOT NULL",
                        "TCNo TEXT NOT NULL UNIQUE",
                        "OkulNo TEXT",
                        "Ad TEXT NOT NULL",
                        "Soyad TEXT NOT NULL",
                        "Cinsiyet INTEGER",
                        "Sinif INTEGER",
                        "Sube TEXT",
                        "Tel TEXT",
                        "DogumTarihi TEXT",
                        "UyelikTarihi TEXT",
                        "Photo TEXT"    )
        self.createTable("GorevliTablosu", "gorevliId"+IdInfo,
                        "GorevliTipi TEXT NOT NULL",
                        "TCNo TEXT NOT NULL UNIQUE",
                        "OkulNo TEXT",
                        "Ad TEXT NOT NULL",
                        "Soyad TEXT NOT NULL",
                        "Sinif TEXT",
                        "Sube TEXT",
                        "Username TEXT UNIQUE",
                        "Password TEXT",
                        "Durum INTEGER" )
        self.createTable("OkulBilgiTablosu", "kurumId"+IdInfo,
                        "KurumKodu TEXT NOT NULL",
                        "OkulAdi TEXT NOT NULL",
                        "MaxCount INTEGER",
                        "MaxDay INTEGER")
        self.createTable("KitapTablosu", "kitapId"+IdInfo,
                        "Barkod TEXT NOT NULL UNIQUE",
                        "ISBN TEXT",
                        "KitapAdi TEXT NOT NULL",
                        "YazarId INTEGER",
                        "KategoriId INTEGER",
                        "BolumId INTEGER",
                        "RafId INTEGER",
                        "Yayinevi TEXT",
                        "SayfaSayisi TEXT",
                        "BasimYili TEXT",
                        "Aciklama TEXT",
                        "DisariVerme INTEGER",
                        "KayitTarihi TEXT",
                        "Durum INTEGER",
                        "ImgBarcod BLOB" )

        conn.commit()
        self.setVeriablesValue()

    def setVeriablesValue(self):
        try:
            maxValues = self.getData("OkulBilgiTablosu", "MaxCount", "MaxDay")
            self.maxNumberOfBooksGiven  = maxValues[0][0]
            self.maxDayBooksStay        = maxValues[0][1]
        except Exception as E:
            print(E)

    def createTable(self, TableName, *cols) -> None:
        curs.execute( f"""CREATE TABLE IF NOT EXISTS {TableName} ( {",".join(cols)} )""" )

    def insertData(self, TableName, **cols_datas):
        try:
            cols        = ', '.join( cols_datas.keys() )
            veriler     = tuple( cols_datas.values() )
            soruIsareti = ", ".join( ["?"] * len(cols_datas) )
            sql = f"""INSERT INTO {TableName} ( { cols } ) VALUES( {soruIsareti} )"""
            curs.execute(sql, veriler)
            conn.commit()
        except sqlite3.Error as E:
            msg.popup_mesaj("Kayıt çakışması", "Kaydetmek istediğiniz veriler daha önce kaydedilmiş ve  \n"
                                               "tekrar etmemesi gereken veriler içeriyor. \n\n"
                                               "(Örn: Kullanıcı Adı, TC Kimlik No, Yazar Adı, Kategori, Raf No vs gibi)\n\n"
                                               f"Fonk: insertData\t\tHata Kodu: {E}\n")
        except Exception as E:
            msg.popup_mesaj("Hata ! ! !", f"FONK: insertData    \nHATA KODU : {E}")

    def forceInsertMultiData(self, TableName, Col, dataList) -> None:
        try:
            global liste, counter
            liste = dataList
            counter = 0
            def ekle():
                global counter, liste
                try:
                    veri = liste.pop()
                    if veri:
                        sql = f"""INSERT INTO {TableName} ( {Col}) VALUES( ? )"""
                        curs.execute(sql, (veri,))
                        conn.commit()
                        counter += curs.rowcount
                        ekle()
                except sqlite3.Error as E:
                    print(E)
                    ekle()
            ekle()
        except Exception as E:
            print("Eklenen kayıt sayısı : ", counter)
            msg.popup_mesaj("Başlık", f"Eklenen {Col} sayısı : {counter}")

    def insertMembersDataFromExcel(self):
        try:
            engine = sqlalchemy.create_engine('sqlite:///Otomasyon.sqlite')
            df_sql = pd.read_sql("UyeTablosu", engine)
            df_xls = pd.read_excel("excel/Örnek Öğrenci Listesi.xls")
            del df_sql["Tel"]
            del df_sql['Photo']
            newColNames = dict(zip(df_xls, df_sql.columns[3:]))
            df_xls.rename(columns=newColNames, inplace=True)
            df_xls["Ad"]        = df_xls["Ad"].str.title().str.replace("i","ı").str.replace("ı̇", "i")
            df_xls["Soyad"]     = df_xls["Soyad"].str.title().str.replace("i","ı").str.replace("ı̇", "i")
            df_xls["UyeTipi"]   = 0
            df_xls["Durum"]     = 1
            df_xls["UyelikTarihi"]=datetime.now().date()
            df_xls["Cinsiyet"]  = df_xls["Cinsiyet"].str.replace("Erkek","1")
            df_xls["Cinsiyet"]  = df_xls["Cinsiyet"].str.replace("Kız","0")
            df_xls.to_sql("UyeTablosu", engine, if_exists="append", index=False)
            msg.popup_mesaj("Toplu Üye Kaydı Başarılı", f"{len(df_xls)} üye kaydınız başarı ile gerçekleşti")
        except Exception as E:
            print("Daha önce kaydedilmiş bir TC kimlik umarası tekrar kullanılmaya çalışıyor.\nHata : ", E)

    def insertBookDataFromExcel(self):
        try:
            kitapTablosuCols = ['ISBN', 'KitapAdi', 'YazarId', 'KategoriId', 'BolumId', 'RafId', 'Yayinevi',
                                'SayfaSayisi', 'BasimYili', 'Aciklama', 'DisariVerme', 'KayitTarihi', 'Durum']
            engine = sqlalchemy.create_engine('sqlite:///Otomasyon.sqlite')
            df_sql = pd.read_sql("KitapTablosu", engine)
            df_xls = pd.read_excel("excel/Örnek Kitap Listesi.xls")
            #   excel den gelen sutun isimlerini sql tablolardaki duruma çeviriyoruz. Bu sayede df leri MERGE edebiliyoruz.
            forRename = dict(zip(df_xls.columns[2:6], ["YazarAdi", "Kategori", "Bolum", "RafNo"]))
            df_xls.rename(columns=forRename, inplace=True)
            print(1)
            #   Verilerin boşluklaını alıyor, sadece ilk hafleri büyük yapıyor ve dönüşürken oluşan i harfi sorununu gideriyoruz. Ayrıca null durumunu kontrol ediyoruz

            df_xls['YazarAdi'] = df_xls[df_xls['YazarAdi'].notnull()]['YazarAdi'].str.strip().str.title().str.replace(
                "i", "ı").str.replace("ı̇", "i")
            df_xls['Kategori'] = df_xls[df_xls['Kategori'].notnull()]['Kategori'].str.strip().str.title().str.replace(
                "i", "ı").str.replace("ı̇", "i")
            df_xls['Bolum'] = df_xls[df_xls['Bolum'].notnull()]['Bolum'].str.strip().str.title().str.replace("i","ı").str.replace("ı̇", "i")
            # df_xls['RafNo'] = df_xls[df_xls['RafNo'].notnull()]['RafNo'].str.strip().str.title().str.replace("i","ı").str.replace("ı̇", "i")
            #   Yazar, Kategori, Bölüm ve Raf Bilgisi kayıt edilmemişse kayıt ediyoruz

            self.forceInsertMultiData("KategoriTablosu", "Kategori", list(df_xls["Kategori"].unique()))
            self.forceInsertMultiData("YazarTablosu", "YazarAdi", list(df_xls["YazarAdi"].unique()))
            #   Yazar, kategori, Bolum ve Raf bilgilerini çağırıyoruz
            print(2)
            df_sql_yazar    = pd.read_sql("YazarTablosu", engine, columns=("YazarAdi", "yazarId"))
            df_sql_kategori = pd.read_sql("KategoriTablosu", engine, columns=("Kategori", "kategoriId"))
            df_sql_bolum    = pd.read_sql("BolumTablosu", engine, columns=("Bolum", "bolumId"))
            df_sql_raf      = pd.read_sql("RafTablosu", engine, columns=("RafNo", "rafId"))
            # df leri MERGE ediyoruz
            print(3)
            result = pd.merge(df_xls, df_sql_yazar, how="left")
            result = pd.merge(result, df_sql_kategori, how="left")
            result = pd.merge(result, df_sql_bolum, how="left")
            result = pd.merge(result, df_sql_raf, how="left")
            # gereksiz sütunları siliyoruz
            del result["YazarAdi"], result["Kategori"], result["Bolum"], result["RafNo"]

            newColNames = dict(zip(result.columns[2:6], df_sql.columns[8:12]))
            newColNames[result.columns[1]] = df_sql.columns[3]
            result.rename(columns=newColNames, inplace=True)

            result["KitapAdi"] = result["KitapAdi"].str.strip().str.title().str.replace("i", "ı").str.replace("ı̇", "i")
            result["Yayinevi"] = result["Yayinevi"].str.strip().str.title().str.replace("i", "ı").str.replace("ı̇", "i")
            result["DisariVerme"] = 1
            newBarkod = int(self.createBarkodeNumber())

            result["Barkod"]    = [str(i)+self.createControlNumber(str(i)) for i in range(newBarkod, newBarkod + len(result))]
            result["Durum"]     = 1
            result['KayitTarihi'] = datetime.today().date()
            print(result['Barkod'])
            result.to_sql("KitapTablosu", engine, if_exists="append", index=False)
            print("yapılan kayıt sayısı: ", len(result))
            msg.popup_mesaj("Toplu Kitap Kaydı Başarılı", f"{len(df_xls)} kitap kaydınız başarı ile gerçekleşti")
            mesaj, _ = msg.MesajBox("Uyarı", "Excel dosyasını temizlemek aynı verilerin tekrar kaydolmasını önler.\n\n"
                                             "Excel dosyanız temizlensin mi?")
            if mesaj:
                self.delExcelData()
        except Exception as E:
            msg.popup_mesaj("HATA", f"Hata Kodu : {E}")


    def delExcelData(self):
        pass

    def updateData(self, TableName, **cols_datas):
        try:
            colsInList  = '=?, '.join( cols_datas.keys() ).rsplit(" ", 1)
            veriler     = tuple( cols_datas.values() )
            result, _   = msg.MesajBox("Güncelleme", "Kaydı güncellemek istediğinizden emin misiniz?")
            if result:
                sql = f""" UPDATE {TableName} SET { colsInList[0][0:-1] } WHERE {colsInList[1]}=? """
                curs.execute(sql, veriler)
                conn.commit()
                if curs.rowcount:
                    msg.popup_mesaj("Güncelleme başarılı", "Kayıt başarı ile güncellendi.\t\t\n")
                else:
                    msg.popup_mesaj("DİKKAT : Güncelleme başarısız ! ! !", "Kayıt güncellenemedi ! ! !\t\t\n")
        except sqlite3.Error as E:
            msg.popup_mesaj("Kayıt çakışması", "Güncellemek istediğiniz veriler daha önce kaydedilmiş ve tekrar etmemesi \t\n"
                                               "gereken veriler içeriyor. \n\n"
                                               "(Örn: Kullanıcı Adı, TC Kimlik No, Yazar Adı, Kategori, Raf No vs gibi)\n\n"
                                               f"Fonk: updateData\t\tHata Kodu: {E}\n")
        except Exception as E:
            msg.popup_mesaj("Hata ! ! !", f"FONK: updateData    \nHATA KODU : {E}")

    def updateEntrustTableEscrowState(self, TableName, **cols_datas):
        try:
            colsInList  = '=?, '.join( cols_datas.keys() ).rsplit(" ", 1)
            veriler     = tuple( cols_datas.values() )
            sql = f""" UPDATE {TableName} SET { colsInList[0][0:-1] } WHERE {colsInList[1]}=? """
            curs.execute(sql, veriler)
            conn.commit()
        except Exception as E:
            print(f"FONK: updateData, HATA KODU : {E}")

    def updateBookTableState(self, Durum: list, kitapId: list):
        try:
            sql = f""" UPDATE KitapTablosu SET Durum=? WHERE kitapId=? """
            curs.executemany(sql, zip( Durum*len(kitapId), kitapId))
            conn.commit()
        except Exception as E:
            print(f"FONK: updateBookState, HATA KODU : {E}")

    def updateUserState(self, Durum: str, Username: str):
        try:
            durum = {"Aktif": 0, "Pasif": 1}
            sql = f""" UPDATE GorevliTablosu SET Durum=? WHERE Username=? """
            curs.execute(sql, (durum[Durum], Username))
            conn.commit()
            if curs.rowcount>0:
                msg.popup_mesaj("Görevli durumu",
                            f"""Görevli durumu '{"Pasif" if Durum == "Aktif" else "Aktif"}' olarak değiştirildi""")
        except Exception as E:
            print(f"FONK: updateUserTableState, HATA KODU : {E}")

    def updateSchoolInfo(self, maxCount=3, maxDay=7):
        try:
            sql = f""" UPDATE OkulBilgiTablosu SET MaxCount=?, MaxDay=? WHERE kurumId=1 """
            curs.execute(sql, (maxCount, maxDay))
            conn.commit()
        except Exception as E:
            print(f"FONK: updateSchoolInfo, HATA KODU : {E}")

    def getData(self, TableName, *cols):
        try:
            getCols = ', '.join( cols )                          # ['col1', 'col2', 'col3'] --> ' col1, col2, col3 ' (iter to str)
            curs.execute(f"SELECT {getCols} FROM {TableName}")
            return curs.fetchall()
        except Exception as E:
            print("Fonk: getData => ", E)

    def getDataWithOrderBy(self, TableName, *cols):
        try:
            getCols = ', '.join( cols )                          # ['col1', 'col2', 'col3'] --> ' col1, col2, col3 ' (iter to str)
            curs.execute(f"SELECT {getCols} FROM {TableName} ORDER BY {getCols}")
            return curs.fetchall()
        except Exception as E:
            print("Fonk: getData => ", E)

    def getFreeBooks(self):
        try:
            sql = f"""SELECT KitapTablosu.kitapId, Barkod, KitapAdi, YazarAdi, ISBN FROM KitapTablosu
            LEFT JOIN YazarTablosu ON KitapTablosu.YazarId=YazarTablosu.yazarId WHERE Durum=1 """
            curs.execute(sql)
            return curs.fetchall()
        except Exception as E:
            print("Fonk: getFreeBooks => ", E)

    def getMemberDataNumberOfRead(self):
        try:
            sql = f"""SELECT UyeTablosu.uyeId, {self.maxNumberOfBooksGiven}-count(EmanetTablosu.UyeId), 
                        OkulNo, Ad, Soyad, TCNo, Sinif, Sube FROM UyeTablosu 
                        LEFT JOIN EmanetTablosu ON UyeTablosu.uyeId=EmanetTablosu.UyeId 
                        WHERE Durum=1 AND DonusTarihi is NULL GROUP By UyeTablosu.uyeId"""
            curs.execute(sql)
            return curs.fetchall()
        except Exception as E:
            print("Fonk: getMemberDataNumberOfRead => ", E)

    def getMemberDataWithWhere(self):
        try:
            colLabels = ("Üye Tipi", "Durum", "TC Kimlik No", "Okul No", "Ad", "Soyad", "Cinsiyet", "Sınıf", "Şube",
                         "Telefon", "Doğum Tarihi", "Üyelik Tarihi", "Foto")
            sql = f"""SELECT CASE WHEN UyeTipi=0 THEN 'Öğrenci' ELSE 'Personel' END, CASE WHEN Durum=1 THEN 'Aktif' ELSE 'Pasif' END,
                     TCNo, OkulNo, Ad, Soyad, CASE WHEN Cinsiyet=0 THEN 'Kız' ELSE 'Erkek' END, Sinif, Sube, Tel,
                     strftime('%d.%m.%Y',DogumTarihi), strftime('%d.%m.%Y',UyelikTarihi) FROM UyeTablosu WHERE Durum=1"""
            curs.execute(sql)
            return curs.fetchall()
        except Exception as E:
            print("Fonk: getMemberDataWithWhere => ", E)

    def getMemberDataWithTcno(self, tcno):
        try:
            sql =f"""SELECT * FROM UyeTablosu WHERE TCNo={tcno}"""
            curs.execute(sql)
            return curs.fetchone()
        except Exception as E:
            print("Fonk: getMemberDataWithTcno => ", E)

    def getBookDataWithId(self, Id):
        try:
            sql =f"""SELECT * FROM KitapTablosu WHERE kitapId={Id}"""
            curs.execute(sql)
            return curs.fetchone()
        except Exception as E:
            print("Fonk: getBookDataWithId => ", E)

    def getBookState(self, Barkod):
        try:
            sql =f"""SELECT Durum FROM KitapTablosu WHERE Barkod LIKE '%{Barkod}%' """
            curs.execute(sql)
            return curs.fetchone()
        except Exception as E:
            print("Fonk: getBookState => ", E)


    def getUserInfoWithCase(self) -> list :
        gorevliTipi = ("Öğrenci", "Personel", "Admin")
        try:
            sql =f"""SELECT Username, 
            CASE WHEN GorevliTipi=0 THEN '{gorevliTipi[0]}' WHEN GorevliTipi=1 THEN '{gorevliTipi[1]}' ELSE '{gorevliTipi[2]}' END,
            CASE WHEN Durum=1 THEN 'Aktif' ELSE 'Pasif' END FROM GorevliTablosu ORDER BY GorevliTipi DESC """
            curs.execute(sql)
            return curs.fetchall()
        except Exception as E:
            print("Fonk: getBookDataWithJoinTables => ", E)

    def getBookDataWithJoinTables(self) -> list :
        durum_0, durum_1 = "Okunuyor", "Rafta"
        try:
            sql =f"""SELECT Barkod, ISBN, KitapAdi, YazarAdi, Kategori, Bolum, RafNo, Yayinevi, SayfaSayisi, BasimYili,                    
                    KayitTarihi, CASE WHEN Durum=1 THEN '{durum_1}' ELSE '{durum_0}' END, Aciklama FROM KitapTablosu 
                    LEFT JOIN YazarTablosu ON KitapTablosu.YazarId=YazarTablosu.yazarId
                    LEFT JOIN KategoriTablosu ON KitapTablosu.KategoriId=KategoriTablosu.kategoriId
                    LEFT JOIN BolumTablosu ON KitapTablosu.BolumId=BolumTablosu.bolumId
                    LEFT JOIN RafTablosu ON KitapTablosu.RafId=RafTablosu.rafId     """
            curs.execute(sql)
            return curs.fetchall()
        except Exception as E:
            print("Fonk: getBookDataWithJoinTables => ", E)

    def getEntrustToday(self):
        try:
            gun = db.maxDayBooksStay
            verTarihi = """strftime('%d.%m.%Y',VerilisTarihi)"""
            donTarihi = f"""strftime('%d.%m.%Y', date(VerilisTarihi, '+{gun} day'))"""
            kalanGun = f"""Cast ((JulianDay(date(VerilisTarihi, '+{gun} day')) - JulianDay(date('now'))) As Integer)"""
            sql = f"""SELECT Barkod,KitapAdi,YazarAdi,TCNo,OkulNo,Ad,Soyad,Sinif,Sube,
                    {verTarihi},{kalanGun},{donTarihi} FROM EmanetTablosu 
                    LEFT JOIN KitapTablosu ON KitapTablosu.kitapId=EmanetTablosu.KitapId
                    LEFT JOIN UyeTablosu ON UyeTablosu.uyeId=EmanetTablosu.UyeId
                    LEFT JOIN YazarTablosu ON KitapTablosu.YazarId=YazarTablosu.yazarId
                    WHERE EmanetTablosu.VerilisTarihi='{datetime.today().date()}' ORDER BY emanetId DESC"""
            curs.execute(sql)
            return curs.fetchall()
        except Exception as E:
            print("Fonk: getEntrustToday => ", E)

    def getEscrowBooksReturnToday(self):
        try:
            colLabels = ('Barkod', 'Eser Adı', 'Yazarı', "Verildiği Tarih", "Kalan Gün", "Son İade Tarihi",
                         'Üye No', 'Okul No', 'Ad', 'Soyad', 'Sınıf', 'Şube')
            xGunOnceVerilen = self.bugun_tarihi().addDays(-self.maxDayBooksStay).toPyDate()
            gun = db.maxDayBooksStay
            verTarihi = """strftime('%d.%m.%Y',VerilisTarihi)"""
            donTarihi = f"""strftime('%d.%m.%Y', date(VerilisTarihi, '+{gun} day'))"""
            kalanGun = f"""Cast ((JulianDay(date(VerilisTarihi, '+{gun} day')) - JulianDay(date('now'))) As Integer)"""
            sql = f"""SELECT KitapTablosu.kitapId, EmanetTablosu.emanetId,Barkod,KitapAdi,YazarAdi,
                    {verTarihi},{kalanGun},{donTarihi}, TCNo, OkulNo, Ad, Soyad, Sinif, Sube FROM EmanetTablosu 
                    LEFT JOIN KitapTablosu ON KitapTablosu.kitapId=EmanetTablosu.KitapId
                    LEFT JOIN UyeTablosu ON UyeTablosu.uyeId=EmanetTablosu.UyeId
                    LEFT JOIN YazarTablosu ON KitapTablosu.YazarId=YazarTablosu.yazarId  
                    WHERE EmanetTablosu.VerilisTarihi<='{xGunOnceVerilen}' AND DonusTarihi is NULL ORDER BY emanetId DESC"""
            curs.execute(sql)
            return curs.fetchall()
        except Exception as E:
            print("Fonk: getEscrowBooksReturnToday => ", E)

    def bugun_tarihi(self):
        bugun = datetime.now()
        date_ = QtCore.QDate(bugun.year, bugun.month, bugun.day)
        return date_

    def getOutsides(self):
        try:
            gun = db.maxDayBooksStay
            verTarihi = """strftime('%d.%m.%Y',VerilisTarihi)"""
            donTarihi = f"""strftime('%d.%m.%Y', date(VerilisTarihi, '+{gun} day'))"""
            kalanGun  = f"""Cast ((JulianDay(date(VerilisTarihi, '+{gun} day')) - JulianDay(date('now'))) As Integer)   """
            sql = f"""SELECT KitapTablosu.kitapId, EmanetTablosu.emanetId, Barkod, KitapAdi, YazarAdi, {verTarihi},{kalanGun},{donTarihi},
                    TCNo, OkulNo, Ad, Soyad, Sinif, Sube FROM EmanetTablosu 
                    LEFT JOIN KitapTablosu ON KitapTablosu.kitapId=EmanetTablosu.KitapId
                    LEFT JOIN UyeTablosu ON UyeTablosu.uyeId=EmanetTablosu.UyeId
                    LEFT JOIN YazarTablosu ON KitapTablosu.YazarId=YazarTablosu.yazarId  
                    WHERE DonusTarihi is NULL ORDER BY emanetId ASC"""
            curs.execute(sql)
            return curs.fetchall()
        except Exception as E:
            print("Fonk: getOutsides => ", E)

    def delData(self, TableName, **cols_datas) -> None:
        try:
            cols        = ','.join( cols_datas.keys() )
            veriler     = tuple( cols_datas.values() )
            # sql = f"DELETE FROM {TableName} WHERE {cols}='%s'" % (veriler)
            sql = f"DELETE FROM {TableName} WHERE {cols}='{veriler[0]}'"
            curs.execute(sql)
            conn.commit()
        except Exception as E:
            print("Fonk: delData => ", E)

    def getId(self, TableName, col, searched) -> None:
        try:
            tableId = {"YazarTablosu":"yazarId", "KategoriTablosu":"kategoriId", "BolumTablosu":"bolumId", "RafTablosu":"rafId"}
            self.cameId = None
            if searched:
                curs.execute( f"SELECT {tableId[TableName]} FROM {TableName} WHERE {col} = '{searched}' " )
                cameData = curs.fetchone()
                if cameData is None:
                    if self.insertData(TableName, **{col: searched}):
                        self.getId(TableName, col, searched)
                else:
                    self.cameId = cameData[0]
        except Exception as E:
            print("Fonk: getId => ", E)

    def createBarkodeNumber(self) -> str:
        try:
            kurumKodu = db.getData("OkulBilgiTablosu", "KurumKodu")
            getMaxId = db.getData("KitapTablosu", "max(kitapId)+1")  # enbüyük ID noyu getirir ve ona 1 ekler
            newId = getMaxId[0][0]
            if newId is None: newId = 1
            barcode7 = f"{newId :0>7}"
            self.createControlNumber(barcode7)
            return barcode7
        except Exception as E:
            print(f"Fonk: createBarkodeNumber \t\tHata Kodu : {E}")

    def createControlNumber(self, barcode7) -> str:
        toplam = 0
        for i, num in enumerate(barcode7):
            toplam += (int(num) * 3 if i % 2 == 1 else int(num))
        controlNumber = str(math.ceil(toplam / 10) * 10 - toplam)
        print("controlNumber: ", controlNumber)
        return controlNumber

    def createBarkodeImg(self, number7) -> str :
        try:
            options = {"quiet_zone": 5, "font_size": 16, "text_distance": 2, 'module_height': 12.0}
            byteImg = BytesIO()
            my_code = EAN8(number7, writer=ImageWriter())
            my_code.write(byteImg, options)                                    # resmi  BytesIO nesnesine yazıyoruz.
            self.byteImg = byteImg.getvalue()                                  # resmin binary şeklini alıyoruz
            my_code.save("imgBarkode/"+my_code.get_fullcode(), options)
            print(my_code.get_fullcode())
            return my_code.get_fullcode(), byteImg.getvalue()
        except Exception as E:
            print(f"Fonk: createBarkodeImg \t\tHata Kodu : {E}")



#print(createBarkodeNumber())
def deneme():
    a = [1,2,3,4]
    b = ("a","b","c")
    print(dict(zip(a, b)))



db = Db()

if __name__=="__main__":
    #db.getget()
    #db.insertBookDataFromExcel()
    # veri = db.getId("YazarTablosu", "YazarAdi", "Ali")
    # print("veri : ", veri)
    #db.insertMembersDataFromExcel()
    #print(db.getData("OkulBilgiTablosu", *("*")))
    #print(db.getData("OkulBilgiTablosu", *("KurumKodu", "OkulAdi")))
    # print(db.getDataWithWhere("UyeTablosu", *("TCNo", "OkulNo", "Ad", 'Soyad'), **{"TCNo": '98765432105'}))
    # db.deneme()
    # db.updateData("UyeTablosu", **{"TCNo":"987", "OkulNo":"123", "Id":1})

    pass


"""
cols = ['Barkod', 'ISBN', 'KitapAdi', 'KayitTarihi', 'Durum']           # sadece istenen columns
engine = sqlalchemy.create_engine('sqlite:///Otomasyon.sqlite')         
df_sql = pd.read_sql("KitapTablosu", engine, columns=cols)
print(df_sql.columns)                                                   # columns
df_xls = pd.read_excel("excel/Örnek Kitap Listesi.xls")
df_xls.rename(columns={"KayitTarihi":"Kayıt Tarihi","KitapAdi":"Kitap Adı", "SayfaSayisi":"Sayfa Sayısı"}, inplace=True)
df_xls.to_sql("KitapTablosu", engine, if_exists="append", index=False)
"""
