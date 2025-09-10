
A program that is based on communication protocols and allows you to send files or messages using an IP address and port.
# 📡 PacketSender (Python + Tkinter)

Bu proje, Python kullanılarak geliştirilen basit bir **UDP/TCP Packet Sender** uygulamasıdır.  
`tkinter` kütüphanesi ile oluşturulan grafik arayüz (GUI) sayesinde kullanıcı, belirlediği IP adresi ve port numarasına TCP veya UDP protokolü üzerinden mesaj gönderebilir.  
Aynı zamanda uygulama, sabit portlar üzerinden gelen mesajları dinler ve ekranda görüntüler.  DİKKAT! (Bu program sadece aynı ağa bağlı cihazlar arasında kullanılabilir).

---

## 🚀 Özellikler

- **TCP ve UDP desteği**: İstenilen protokol seçilip mesaj gönderilebilir.
- **Sabit dinleme portları**:
  - UDP: **32256**
  - TCP: **32257**
- **Mesaj geçmişi**: Gönderilen ve alınan tüm mesajlar protokol bilgisi ile birlikte listelenir.
- **Kullanıcı dostu arayüz**: IP adresi, hedef port, mesaj alanı ve seçim butonları ile kolay kullanım.

---

## 🖥️ Arayüz

- **IP Address**: Mesajı göndermek istediğiniz hedef IP adresi.  
- **Hedef Port**: Mesajın gönderileceği hedef port.  
- **Protocol**: TCP veya UDP seçimi yapılır.  
- **Message**: Gönderilmek istenen mesajın yazıldığı alan.  
- **Chat Box**: Gönderilen ve alınan mesajların görüntülendiği kutu.  

Uygulama açıldığında ayrıca sabit dinleme portları ekranda görüntülenir:

- `UDP Dinleme Portu: 32256`
- `TCP Dinleme Portu: 32257`

---

## ⚙️ Kurulum

1. Python 3 kurulu olduğundan emin olun.  
2. Uygulamayı çalıştırmak için terminalde:  

```bash
python packetsender.py
