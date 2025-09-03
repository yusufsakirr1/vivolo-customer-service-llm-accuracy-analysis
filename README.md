# LLM Müşteri Hizmetleri Analiz Projesi

Bu proje, müşteri hizmetleri konuşmalarını LLM (Large Language Model) kullanarak otomatik olarak sınıflandıran ve manuel etiketlemelerle karşılaştırarak doğruluk analizi yapan bir sistemdir.

## 📊 Analiz Sonuçları

### Genel Performans
- **Toplam Doğruluk: %84.67** (150 tahmin içinden 127 doğru)
- **Analiz Edilen Konuşma Sayısı: 50**
- **Değerlendirilen Kategoriler: 3** (Konu, Duygu, Bot Yanıt)

### Kategori Bazlı Doğruluk Oranları

#### 1. Duygu Analizi (Sentiment Analysis)
- **Doğruluk: %98.00** 
- **Doğru Tahmin: 49/50**
- **Yanlış Tahmin: 1**
- **Performans: Mükemmel** ⭐⭐⭐⭐⭐
- **Hata Detayı:** 1 adet "Nötr" vs "Pozitif" karışıklığı

#### 2. Konu Sınıflandırması (Topic Classification)  
- **Doğruluk: %88.00**
- **Doğru Tahmin: 44/50**
- **Yanlış Tahmin: 6**
- **Performans: İyi** ⭐⭐⭐⭐
- **Ana Hata Kaynakları:**
  - Benzer etkinlik türleri arasında karışıklık (düğün/sünnet)
  - Nişan türevleri arasında belirsizlik

#### 3. Bot Yanıt Sınıflandırması (Bot Answered)
- **Doğruluk: %68.00**
- **Doğru Tahmin: 34/50** 
- **Yanlış Tahmin: 16**
- **Performans: Geliştirilmeli** ⭐⭐⭐
- **Ana Problem:** Yanlış negatif eğilimi (LLM "Hayır" der, gerçekte "Evet")

## 📈 Detaylı Hata Analizi

### Bot Yanıt Hatalar (16 adet)
- **Yanlış Negatif:** 15 adet (LLM "Hayır", Manuel "Evet")
- **Yanlış Pozitif:** 1 adet (LLM "Evet", Manuel "Hayır")
- **Ana Sorun:** Konservatif tahmin eğilimi

### Konu Sınıflandırma Hataları (6 adet)
- düğün/mekan → bekarlığa_veda/mekan
- düğün/mekan → sünnet/mekan  
- düğün/organizasyon → nişan/organizasyon
- Ve diğer benzer etkinlik karışıklıkları

## 📁 Oluşturulan Dosyalar

- `llm_analysis_v7_final_results.csv` - Ana veri seti (Numbers'dan dönüştürülmüş)
- `detailed_topic_classification_comparison.csv` - Konu sınıflandırma karşılaştırması
- `detailed_sentiment_analysis_comparison.csv` - Duygu analizi karşılaştırması  
- `detailed_bot_answered_comparison.csv` - Bot yanıt karşılaştırması
- `analyze_llm_accuracy.py` - Python analiz scripti
- `llm_accuracy_analysis_summary.txt` - Kapsamlı yazılı rapor

## 🎯 Öneriler

### Öncelik Sırası
1. **Acil:** Bot Yanıt doğruluğunu %68'den %85+'a çıkarın
2. **Orta:** Benzer etkinlik türleri için konu sınıflandırmasını geliştirin
3. **Uzun Vadeli:** Konservatif tahmin eğilimini düzeltin

### İyileştirme Stratejileri
- Bot etkileşimi tahminleri için ek eğitim verisi
- Benzer kategoriler arası ayırt etme kapasitesini artırma
- Yanlış negatif oranını azaltmaya odaklanma

## 🔧 Teknik Detaylar

- **Veri Kaynağı:** Apple Numbers dosyası (.numbers)
- **Analiz Yöntemi:** Python pandas ile karşılaştırmalı analiz
- **Metrikler:** Basit doğruluk oranı (accuracy)
- **Veri Boyutu:** 50 konuşma × 3 kategori = 150 tahmin

## 📊 Sonuç

LLM sistemi genel olarak **%84.67 doğrulukla** başarılı performans göstermektedir. Duygu analizi mükemmel seviyede, konu sınıflandırması iyi seviyede çalışırken, bot yanıt tahmini geliştirilmeye ihtiyaç duymaktadır.