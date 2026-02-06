import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURACIÓN (Esto iría en un archivo de configuración seguro .env) ---
# En un entorno real, NO ponemos contraseñas en el código.
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "tu_correo@gmail.com"
# Para Gmail, necesitas una "Contraseña de Aplicación", no tu contraseña normal.
# Ver: https://myaccount.google.com/apppasswords
SENDER_PASSWORD = "tu_contraseña_de_aplicación" 

def enviar_correo_automatizado(destinatario, asunto, mensaje_texto, adjunto_path=None):
    """
    Función que Pime IA usaría para enviar reportes automáticamente.
    """
    try:
        # Crear el objeto del mensaje
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = destinatario
        msg['Subject'] = asunto

        # Agregar el cuerpo del mensaje
        msg.attach(MIMEText(mensaje_texto, 'plain'))

        # (Aquí iría la lógica para adjuntar archivos si fuera necesario)

        # Iniciar conexión segura con el servidor de correo
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls() # Encriptar conexión
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        # Enviar correo
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, destinatario, text)
        server.quit()
        
        print(f"✅ Correo enviado exitosamente a {destinatario}")
        return True

    except Exception as e:
        print(f"❌ Error al enviar correo: {e}")
        return False

# --- EJEMPLO DE USO PIME IA ---
if __name__ == "__main__":
    print("--- AGENTE DE COMUNICACIÓN PIME IA ---")
    print("Para que esto funcione, necesitas configurar tu 'App Password' de Google.")
    
    # Simulación
    # enviar_correo_automatizado("santiago@desafia.com", "Plan de Trabajo", "Hola, adjunto el plan...")
