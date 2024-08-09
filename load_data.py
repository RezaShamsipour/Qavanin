import markdownify
from pathlib import Path
from app.services.pinecone_service import PiceconeService
from app.services.embedding_service import EmbeddingService


def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()
    
    html_content = markdownify.markdownify(md_content)
    return html_content


def process_markdown_files(directory):
    vector_list = []
    for index,md_file_path in enumerate(Path(directory).glob('*.md'), start=1):
        html_content = parse_markdown(md_file_path)
        embeded , text = EmbeddingService.generate_embedding(html_content)
        vector_dict={
            "id": f"vec{index}",
            "values": embeded,
            "metadata": {"text": text}
        }
        vector_list.append(vector_dict)

    PiceconeService.add(vector_list)
    


def main():
    directory = 'app/data_extraction'
    process_markdown_files(directory)

if __name__ == "__main__":
    main()