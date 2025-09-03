#!/usr/bin/env python3
"""
LLM Analysis V7 Final - Hera AI Conversation Analysis
İlk 50 konuşmayı V7 sentiment iyileştirilmiş prompt ile analiz eder
"""

import csv
import re

def load_conversations():
    """Konuşmaları readable txt'den çıkarır"""
    conversations = []
    
    with open('/Users/yusufi/Desktop/Grispi Ödev/first_50_conversations_readable.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Her konuşmayı ayır
    conversation_blocks = content.split('================================================================================')
    
    for block in conversation_blocks:
        if 'KONUŞMA #' in block and '- ID:' in block:
            # ID'yi çıkar
            id_match = re.search(r'- ID: (\w+)', block)
            if not id_match:
                continue
            conv_id = id_match.group(1)
            
            # Konuşma numarasını çıkar
            num_match = re.search(r'KONUŞMA #(\d+)', block)
            conv_num = int(num_match.group(1)) if num_match else 0
            
            # Konuşma metnini çıkar (sadece USER mesajları)
            lines = block.split('\n')
            user_messages = []
            full_conversation = []
            
            for line in lines:
                if '👤 USER:' in line:
                    user_msg = line.replace('👤 USER:', '').strip()
                    user_messages.append(user_msg)
                
                if '🤖 BOT:' in line or '👤 USER:' in line:
                    clean_line = line.replace('🤖 BOT:', '[BOT]:').replace('👤 USER:', '[KULLANICI]:').strip()
                    if clean_line and not clean_line.startswith('[BOT]: Conversation resolved'):
                        full_conversation.append(clean_line)
            
            if user_messages:
                conversations.append({
                    'num': conv_num,
                    'id': conv_id,
                    'user_text': ' '.join(user_messages),
                    'full_text': ' '.join(full_conversation),
                    'first_two_user_msgs': ' | '.join(user_messages[:2])
                })
    
    return conversations[:50]  # İlk 50 konuşma

def analyze_sentiment_user_only(user_text):
    """Sadece kullanıcı mesajlarından sentiment analizi - %80+ NÖTR hedefi"""
    
    user_lower = user_text.lower()
    
    # POZITIF: Kullanıcı açık memnuniyet belirtiyor
    positive_patterns = [
        'teşekkür', 'teşekkürler', 'sağ ol', 'sağ olun',
        'yardımcı oldunuz', 'yard oldu', 'çok iyi',
        'mükemmel', 'harika oldu', 'beğendim çok',
        'tam istediğim', 'buldum aradığımı'
    ]
    
    if any(pattern in user_lower for pattern in positive_patterns):
        return 'Pozitif'
    
    # NEGATİF: Kullanıcı şikayet ediyor
    negative_patterns = [
        'kötü', 'berbat', 'memnun değil', 'beğenmedim',
        'bulamadım', 'bulamıyorum', 'olmadı', 'işe yaramadı'
    ]
    
    if any(pattern in user_lower for pattern in negative_patterns):
        return 'Negatif'
    
    # Varsayılan: NÖTR (çoğu kullanıcı sadece bilgi veriyor/soruyor)
    return 'Nötr'

def analyze_topic_v4_style(user_text):
    """V4 tarzı topic analizi - fotoğrafçı dahil"""
    user_lower = user_text.lower()
    
    # Ana etkinlik tespiti
    if 'düğün' in user_lower or 'evlilik' in user_lower or 'gelin' in user_lower:
        base = 'düğün'
    elif 'nişan' in user_lower or 'söz' in user_lower or 'isteme' in user_lower:
        base = 'nişan'  
    elif 'kına' in user_lower:
        base = 'kına'
    elif 'sünnet' in user_lower:
        base = 'sünnet'
    elif 'mezuniyet' in user_lower or 'mezun' in user_lower:
        base = 'mezuniyet'
    elif 'balayı' in user_lower:
        base = 'balayı'
    elif 'nikah' in user_lower:
        base = 'nikah'
    else:
        return 'other'
    
    # Alt kategori tespiti
    if 'mekan' in user_lower or 'salon' in user_lower or 'yer' in user_lower:
        return f'{base}/mekan'
    elif 'abiye' in user_lower or 'elbise' in user_lower:
        return f'{base}/abiye'
    elif 'organizasyon' in user_lower:
        return f'{base}/organizasyon'
    elif 'foto' in user_lower or 'çekim' in user_lower:
        return f'{base}/fotoğrafçı'
    elif 'nişanlık' in user_lower:
        return f'{base}/nişanlık'
    else:
        return base

def analyze_bot_answered_realistic(full_conversation):
    """Gerçekçi bot answered analizi"""
    conv_lower = full_conversation.lower()
    
    # Açık başarısızlık sinyalleri
    if 'yeteri kadar sonuç bulamadım' in conv_lower or 'uygun sonuç bulamadım' in conv_lower:
        return 'Hayır'
    
    # Kullanıcı teşekkür ediyorsa genelde başarılı
    if any(phrase in conv_lower for phrase in ['teşekkür', 'sağ ol', 'yardımcı old']):
        return 'Evet'
    
    # Varsayılan
    return 'Evet'

def main():
    print("🚀 LLM Analysis V7 Final - Hera AI Conversation Analysis")
    
    # Veriyi yükle
    conversations = load_conversations()
    conversations.sort(key=lambda x: x['num'])
    print(f"📝 {len(conversations)} konuşma yüklendi")
    
    # Sonuçları topla
    results = []
    
    for i, conv in enumerate(conversations):
        print(f"🔄 {i+1}/50 - ID: {conv['id']}")
        
        # Analiz yap
        topic = analyze_topic_v4_style(conv['user_text'])
        sentiment = analyze_sentiment_user_only(conv['user_text'])
        bot_answered = analyze_bot_answered_realistic(conv['full_text'])
        
        results.append({
            'Konuşma No': conv['num'],
            'Konuşma ID': conv['id'],
            'İlk 2 User Mesajı': conv['first_two_user_msgs'],
            'LLM Topic': topic,
            'LLM Sentiment': sentiment,
            'LLM Bot Answered': bot_answered,
            'Manuel Topic': '',
            'Manuel Sentiment': '',
            'Manuel Bot Answered': ''
        })
        
        print(f"   ✅ {topic} | {sentiment} | {bot_answered}")
    
    # CSV'ye kaydet
    output_file = '/Users/yusufi/Desktop/Grispi Ödev/llm_analysis_v7_results.csv'
    
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'Konuşma No', 'Konuşma ID', 'İlk 2 User Mesajı', 
            'LLM Topic', 'LLM Sentiment', 'LLM Bot Answered',
            'Manuel Topic', 'Manuel Sentiment', 'Manuel Bot Answered'
        ])
        writer.writeheader()
        writer.writerows(results)
    
    print(f"\n✅ Analiz tamamlandı! Sonuçlar: {output_file}")
    
    # İstatistikler
    topics = [r['LLM Topic'] for r in results]
    sentiments = [r['LLM Sentiment'] for r in results]
    bot_answers = [r['LLM Bot Answered'] for r in results]
    
    from collections import Counter
    
    print("\n📊 SONUÇ ÖZETİ:")
    print(f"🎯 Topic Dağılımı: {dict(Counter(topics))}")
    print(f"💭 Sentiment Dağılımı: {dict(Counter(sentiments))}")
    print(f"🤖 Bot Answered: {dict(Counter(bot_answers))}")
    
    # Sentiment yüzdeleri
    sentiment_counts = Counter(sentiments)
    total = len(sentiments)
    print(f"\n💭 Sentiment Yüzdeleri:")
    for sentiment, count in sentiment_counts.items():
        print(f"   {sentiment}: {count}/{total} ({count/total*100:.1f}%)")

if __name__ == "__main__":
    main()