@pytest.fixture def male_name(): 'Phil'i döndür @pytest.fixture def female_name(): 'Claire' değerini döndür def test_male_prefix(male_name): 'Bay' deyin. == get_gender_heading(erkek_adı) def test_female_prefix(female_name): 'Bayan' deyin. == get_gender_heading(kadın_adı)

Bu fikstürü parametre ile test etmeden çalıştırın autouse. Bu, işlevlere yama/alaycı ekleme yaparken özellikle yararlıdır: @pytest.fixture(autouse=True, scope='function') def common_patches(): mock.patch(...)

Parametreli testler pytest.mark.parametrize kurtarmak için! Yukarıdaki dekoratör çok güçlü bir işlevselliktir, her yinelemede girilen parametreleri değiştirerek bir test işlevini birden çok kez çağırmaya izin verir. İlk bağımsız değişken, dekore edilmiş işlevin bağımsız değişkenlerini virgülle ayrılmış bir dizeyle listeler. İkinci bağımsız değişken, çağrı değerleri için yinelenebilir.

@pytest.mark.parametrize('isim', ['Claire', 'Gloria', 'Haley']) def test_female_prefix_v2(name): 'Bayan' iddiası == get_gender_heading(isim)

Böylece, pytest birden çok kez arayacaktır test_female_prefix_v2: önce ile name='Claire', sonra ile name='Gloria'vb. Bu, özellikle aynı anda birden çok bağımsız değişken kullanıldığında kullanışlıdır:

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
