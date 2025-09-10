import tkinter as tk
from tkinter import scrolledtext, messagebox
import socket
import threading

class PacketSenderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PacketSender")

        # Sabit portlar
        self.udp_port = 32256
        self.tcp_port = 32257

        # IP Address
        tk.Label(root, text="IP Address:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.ip_entry = tk.Entry(root)
        self.ip_entry.grid(row=0, column=1, padx=5, pady=5)

        # Port
        tk.Label(root, text="Hedef Port:").grid(row=0, column=2, padx=5, pady=5, sticky='e')
        self.port_entry = tk.Entry(root)
        self.port_entry.grid(row=0, column=3, padx=5, pady=5)

        # Protocol selection
        tk.Label(root, text="Protocol:").grid(row=0, column=4, padx=5, pady=5, sticky='e')
        self.protocol_var = tk.StringVar(value="TCP")
        self.tcp_radio = tk.Radiobutton(root, text="TCP", variable=self.protocol_var, value="TCP")
        self.udp_radio = tk.Radiobutton(root, text="UDP", variable=self.protocol_var, value="UDP")
        self.tcp_radio.grid(row=0, column=5)
        self.udp_radio.grid(row=0, column=6)

        # Gönderilen Mesaj
        tk.Label(root, text="Message:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.grid(row=1, column=1, columnspan=4, padx=5, pady=5)

        # Gönder butonu
        self.send_button = tk.Button(root, text="Gönder", command=self.send_message)
        self.send_button.grid(row=1, column=5, columnspan=2, padx=5, pady=5)

        # Port bilgilerini göster (görünür ve sabit)
        self.udp_label = tk.Label(root, text=f"UDP Dinleme Portu: {self.udp_port}", fg="blue", font=("Arial", 10, "bold"))
        self.udp_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky="w")

        self.tcp_label = tk.Label(root, text=f"TCP Dinleme Portu: {self.tcp_port}", fg="green", font=("Arial", 10, "bold"))
        self.tcp_label.grid(row=2, column=3, columnspan=4, padx=5, pady=5, sticky="w")

        # Mesaj kutusu
        self.chat_box = scrolledtext.ScrolledText(root, width=90, height=20, state='disabled')
        self.chat_box.grid(row=3, column=0, columnspan=7, padx=5, pady=10)

        # Dinleyicileri başlat
        self.start_tcp_server_thread()
        self.start_udp_server_thread()

    def start_tcp_server_thread(self):
        threading.Thread(target=self.listen_for_tcp_messages, daemon=True).start()

    def start_udp_server_thread(self):
        threading.Thread(target=self.listen_for_udp_messages, daemon=True).start()

    def listen_for_tcp_messages(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('', self.tcp_port))
        server_socket.listen(5)

        while True:
            client_socket, addr = server_socket.accept()
            threading.Thread(target=self.handle_tcp_client, args=(client_socket, addr), daemon=True).start()

    def handle_tcp_client(self, client_socket, addr):
        try:
            message = client_socket.recv(1024).decode('utf-8')
            self.display_message(f"[TCP Gelen] {addr[0]}:{addr[1]} → {message}")
        finally:
            client_socket.close()

    def listen_for_udp_messages(self):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind(('', self.udp_port))

        while True:
            try:
                data, addr = udp_socket.recvfrom(1024)
                message = data.decode('utf-8')
                self.display_message(f"[UDP Gelen] {addr[0]}:{addr[1]} → {message}")
            except:
                continue

    def send_message(self):
        ip = self.ip_entry.get()
        port = self.port_entry.get()
        message = self.message_entry.get()
        protocol = self.protocol_var.get()

        if not ip or not port or not message:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
            return

        try:
            port = int(port)
            if protocol == "TCP":
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((ip, port))
                client_socket.send(message.encode('utf-8'))
                client_socket.close()
                self.display_message(f"[TCP Ben] {ip}:{port} → {message}")
            elif protocol == "UDP":
                udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                udp_socket.sendto(message.encode('utf-8'), (ip, port))
                self.display_message(f"[UDP Ben] {ip}:{port} → {message}")
            self.message_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Bağlantı Hatası", str(e))

    def display_message(self, message):
        self.chat_box.config(state='normal')
        self.chat_box.insert(tk.END, message + '\n')
        self.chat_box.yview(tk.END)
        self.chat_box.config(state='disabled')

# Uygulamayı başlat
if __name__ == "__main__":
    root = tk.Tk()
    app = PacketSenderApp(root)
    root.mainloop()
