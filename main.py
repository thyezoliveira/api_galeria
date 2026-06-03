from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from drive_service import get_gallery_data

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend URL(s) in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/galeria")
async def get_galeria():
    try:
        data = get_gallery_data()
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

#if __name__ == "__main__":
#    import uvicorn
#    uvicorn.run(app, host="0.0.0.0", port=8000)
