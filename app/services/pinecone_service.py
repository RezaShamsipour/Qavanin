from pinecone import Pinecone


class PiceconeService:
    pine_cone = Pinecone(api_key="e8958617-8938-4968-910a-221c8ea20557")
    index = pine_cone.Index(
        "qavanin", "https://qavanin-du7kydj.svc.aped-4627-b74a.pinecone.io"
    )

    @classmethod
    def search(cls, query_vector: list, top_k=2):
        results = cls.index.query(
            vector=query_vector, top_k=top_k, include_metadata=True
        )
        return results

    @classmethod
    def add(cls, vecotr_list: list):
        cls.index.upsert(vecotr_list)
