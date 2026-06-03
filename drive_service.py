import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

def get_drive_service():
    creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not creds_path:
        raise Exception("GOOGLE_APPLICATION_CREDENTIALS not set")
    
    creds = service_account.Credentials.from_service_account_file(creds_path)
    return build("drive", "v3", credentials=creds)

def get_gallery_data():
    service = get_drive_service()
    folder_id = os.getenv("GOOGLE_DRIVE_FOLDER_ID")
    
    # Get categories (subfolders)
    query = f"'{folder_id}' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    folders = service.files().list(q=query, fields="files(id, name)").execute().get("files", [])
    
    gallery = {}
    
    for folder in folders:
        service.permissions().create(
                fileId=folder["id"],
                body={'type': 'anyone', 'role': 'reader'}
            ).execute()
        # Get images in the subfolder
        # Note: In a real scenario, you might want to filter by mimeType, e.g., 'image/jpeg'
        files_query = f"'{folder['id']}' in parents and trashed = false"
        files = service.files().list(
            q=files_query, 
            fields="files(id, name)"
        ).execute().get("files", [])
        
        gallery[folder['name']] = [
            {"name": f['name'], "link": f"https://drive.google.com/thumbnail?sz=w1200&id={f['id']}"} for f in files
        ]
        
    return gallery
