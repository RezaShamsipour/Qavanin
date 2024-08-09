from transformers import BertTokenizer, BertModel
import torch


class EmbeddingService:
    tokenizer = BertTokenizer.from_pretrained("HooshvareLab/bert-fa-zwnj-base")
    model = BertModel.from_pretrained("HooshvareLab/bert-fa-zwnj-base")

    @classmethod
    def generate_embedding(cls, text: str):
        encoded_input = cls.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            padding="max_length",
            truncation=True,
            max_length=150,
            return_tensors="pt",
        )
        input_ids = encoded_input["input_ids"]
        attention_mask = encoded_input["attention_mask"]

        with torch.no_grad():
            outputs = cls.model(input_ids, attention_mask=attention_mask)
            embeddings = outputs.last_hidden_state
            embedding_vector = embeddings.mean(dim=1).squeeze()

        return embedding_vector.tolist(), text
