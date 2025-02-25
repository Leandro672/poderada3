from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/stream/{video_id}")
async def stream_video(video_id: str):
    if not is_video_available(video_id):
        raise HTTPException(status_code=404, detail="Vídeo não encontrado")
    return {"message": f"Reproduzindo o vídeo {video_id}"}

def is_video_available(video_id: str) -> bool:
    # Simulação de verificação de disponibilidade do vídeo
    available_videos = ["vid123", "vid456", "vid789"]
    return video_id in available_videos
