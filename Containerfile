# Nutze das UBI8-Python-Image als Basis
FROM registry.access.redhat.com/ubi8/python-39

# Root-Kontext zum Installieren
USER 0
RUN pip install --no-cache-dir flask
# Wechsle zurück zu einem nicht-root User (OpenShift Best Practice)
USER 1001

WORKDIR /app

# Kopiere unsere kleine Web-App in das Image
COPY app.py /app/

# Der Webserver läuft auf Port 8080
EXPOSE 8080

# Standard-Startbefehl
CMD ["python", "app.py"]

