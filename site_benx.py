import webbrowser
import socket
import http.server
import socketserver
import threading

# HTML atualizado com botões empilhados + rodapé com dados Benx
html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>BENX INCORPORADORA</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #222; color: white; margin: 0; text-align: center; }
        .main-container { padding: 40px; max-width: 1000px; margin: auto; }
        h1 { font-size: 40px; margin-bottom: 20px; }
        h2 { font-size: 28px; margin: 10px 0; color: #ccc; }
        h3 { font-size: 22px; margin: 10px 0 30px 0; }
        iframe { width: 100%; height: 400px; border: none; border-radius: 10px; margin-bottom: 30px; }
        .btn { display: block; width: 100%; margin: 15px auto; padding: 15px; border-radius: 8px; text-decoration: none;
               font-size: 18px; background: linear-gradient(135deg, #667eea, #764ba2); color: white; transition: 0.3s; max-width: 400px; }
        .btn:hover { background: linear-gradient(135deg, #f093fb, #f5576c); }
        .footer { margin-top: 50px; font-size: 14px; color: #aaa; line-height: 1.6; }
    </style>
</head>
<body>
    <div class="main-container">
        <h1>BENX INCORPORADORA</h1>
        <h2>Empreendimento</h2>
        <h3>Viva Benx Casa do Ator</h3>

        <!-- Google Maps -->
        <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3656.8943727766244!2d-46.663879!3d-23.5945229!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce574f1e6f3f9d%3A0x5c43a5a6cce2f5c2!2sR.%20Casa%20do%20Ator%2C%201100%20-%20Vila%20Ol%C3%ADmpia%2C%20S%C3%A3o%20Paulo%20-%20SP%2C%2004526-003!5e0!3m2!1spt-BR!2sbr!4v1695225478000!5m2!1spt-BR!2sbr" 
            allowfullscreen="" loading="lazy">
        </iframe>

        <!-- Botões -->
        <a class="btn" href="https://www.benx.com.br/" target="_blank">Site Benx Incorporadora</a>
        <a class="btn" href="VBCA - Manual do Proprietário (1).pdf" target="_blank">Manual do Proprietário</a>
        <a class="btn" href="VBCA - Manual do Proprietário - garantias.pdf" target="_blank">Termo de Garantia</a>
        <a class="btn" href="VBCA - Manual do Proprietário - fornecedores.pdf" target="_blank">Fornecedores</a>

        <!-- Rodapé -->
        <div class="footer">
            <p><b>BENX INCORPORADORA</b></p>
            <p>Av. Dr. Cardoso De Melo, 1340 - 6º Andar<br>
            Vila Olímpia • São Paulo • SP • CEP: 04548-004<br>
            0800 729 1981</p>
        </div>
    </div>
</body>
</html>
"""

# Nome do arquivo HTML
file_name = "site_benx.html"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(html_content)

# Servidor HTTP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
port = 8000
Handler = http.server.SimpleHTTPRequestHandler

def start_server():
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Servidor rodando em: http://{local_ip}:{port}/{file_name}")
        httpd.serve_forever()

threading.Thread(target=start_server, daemon=True).start()
webbrowser.open(f"http://{local_ip}:{port}/{file_name}")

print("🚀 Site Benx Incorporadora iniciado!")
print(f"📱 Acesse: http://{local_ip}:{port}/{file_name}")
print("💡 Pressione Ctrl+C para encerrar...")

try:
    input()
except KeyboardInterrupt:
    print("\n👋 Servidor encerrado!")

