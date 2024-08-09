from fastapi import APIRouter, HTTPException
from app.services.pinecone_service import PiceconeService
from app.services.embedding_service import EmbeddingService
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/")
async def search(query: str):
    embedding_query, text = EmbeddingService.generate_embedding(query)
    query_response = PiceconeService.search(embedding_query)
    if not query_response:
        raise HTTPException(status_code=404, detail="No results found")

    results = []
    for item in query_response["matches"]:
        result = {"id": item.id, "metadata": item.metadata, "score": item.score}
        results.append(result)

    return JSONResponse(content={"matches": results})
