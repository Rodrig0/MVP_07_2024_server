# Usar uma imagem oficial do Python como imagem base
FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar o conteúdo do diretório atual para o container no diretório /app
COPY . /app

# Instalar os pacotes necessários especificados no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Tornar a porta 5004 disponível para o mundo externo a este container
EXPOSE 5004

# Definir a variável de ambiente FLASK_APP
ENV FLASK_APP=app.py

# Executar app.py quando o container for iniciado
CMD ["flask", "run", "--host=0.0.0.0", "--port=5004"]
