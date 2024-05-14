



@pytest.mark.parametrize( 'isim, bekleniyor', [('Claire', 'Mrs'), ('Jay', 'Mr')] ) def test_both_sex_v2(isim, bekleniyor): iddia bekleniyor == get_gender_heading(name )

Birden çok bağımsız değişkenle, pytest.mark.parametrizedizine dayalı basit bir ilişkilendirme gerçekleştirir, bu nedenle while önce ve sonra değerleri namevarsayar , ve değerleri alır .ClaireJayexpectedMrsMr

Bazı Dekoratörler

pytest.approx(): İki veya ikiden fazla sayının sayı kümeleri yaklaşık olarak bazı farklılıklara eşitler.

pytest.fail(): Yürütülmekte olan test açıkça başarısız olursa, mesaj gösterir.

pytest.skip(): Gösterilen mesajla yürütme testini atlatır.

pytest.exit(): Test sürecinden çıkartır.

pytest.main(): İşlem içi test yürütmesi tamamlandığında çıkış kodunu döndürür

pytest.raises(): Bir kod bloğu çağrısının beklenen istisnayı ortaya çıkardığını veya bir hata istisnası oluşturduğunu ileri sürer.

pytest.mark.skip(): Bu dekoratör bir test fonksiyonunda belirlenen testi atlamak için kullanılır.

pytest.mark.timeout(): Bir testin belirli bir sürede tamamlanması gerektiğini belirlemek için kullanılır.
