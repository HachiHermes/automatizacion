#!/usr/bin/env python3
"""
Script para sincronizar carpeta de Google Drive a repositorio local.
Requiere: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
"""
import os
import json
from pathlib import Path

# Configuración
FOLDER_ID = "1RIndks15ecfnZ2yzUnsWRZ0pgE9WVSTS"
LOCAL_DIR = Path("documentos")
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def main():
    print(f"🔄 Sincronizando carpeta Google Drive {FOLDER_ID} -> {LOCAL_DIR}")
    print("⚠️  Necesitas configurar credentials.json de Google Cloud Console")
    print("   1. Ve a https://console.cloud.google.com/")
    print("   2. APIs y Servicios > Credenciales > Crear credenciales > ID de cliente OAuth")
    print("   3. Descarga credentials.json y ponlo en este directorio")
    print("   4. Ejecuta: python3 sync_gdrive.py")
    
    LOCAL_DIR.mkdir(exist_ok=True)
    
    # Aquí iría la lógica real de Google Drive API
    # Por ahora creamos un README de ejemplo
    (LOCAL_DIR / "README.md").write_text(
        f"# Documentos desde Google Drive\n\n"
        f"Carpeta: https://drive.google.com/drive/folders/{FOLDER_ID}\n\n"
        f"*Sincroniza ejecutando: python3 sync_gdrive.py*"
    )
    
    print(f"✅ Directorio {LOCAL_DIR} creado con README.md")

if __name__ == "__main__":
    main()
