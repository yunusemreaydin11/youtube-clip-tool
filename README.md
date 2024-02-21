# Projenin İşleyişi
1. İlk olarak, gerekli kütüphaneleri içe aktarıyoruz. build fonksiyonu, YouTube API'si için bir YouTube nesnesi oluşturmak için kullanılır. YouTube sınıfı, video indirmek için kullanılır. VideoFileClip sınıfı, video dosyalarını işlemek için kullanılır. os modülü, işletim sistemi işlevleri sağlar. re modülü, düzenli ifadelerle metin eşleştirmeyi sağlar.
2. YouTube API'sine erişmek için kullanılacak geliştirici anahtarını ve API istemcisini oluşturmak için build fonksiyonunu kullanıyoruz.
3. 'get_video_id' fonksiyonu, YouTube video URL'sinden video kimliğini (ID) ayıklamak için kullanılır.
4. Kullanıcıdan bir YouTube video URL'si girmesini istiyoruz.
5. Girilen URL'den video kimliğini alıyoruz ve YouTube API'sini kullanarak video hakkında bilgi alıyoruz.
6. Video başlığının temizlenmiş bir sürümünü oluşturuyoruz. Burada, başlık içindeki özel karakterleri temizliyor ve boşlukları alt çizgiyle değiştiriyoruz.
7. 'pytube' modülünü kullanarak YouTube'dan videoyu indiriyoruz. En yüksek çözünürlükteki videoyu indirmek için 'get_highest_resolution()' yöntemini kullanıyoruz.
8. Saat, dakika ve saniye cinsinden verilen bir süreyi saniyeye dönüştüren bir yardımcı işlev tanımlıyoruz.


# Projenin Bana Kattıları
### Öncelikle, YouTube API'sini kullanarak video bilgilerini almayı ve indirmeyi öğrendim.Python'un os modülünü kullanarak dosya işlemlerini gerçekleştirmeyi ve kullanıcıdan girdi almayı öğrendim.MoviePy kütüphanesini kullanarak video düzenleme becerilerimi geliştirdim.Hata yakalama yeteneğimi geliştirdim ve kodlama becerilerimi pekiştirdim
