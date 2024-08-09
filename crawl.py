from playwright.sync_api import sync_playwright
#from transformers import BertTokenizer, BertModel
#import chromadb
import markdownify
#import torch


def crawl_page(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Linux; Android 8.0.0; AGS2-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Safari/537.36"
        )
        page = context.new_page()

        page.goto(url)

        page.wait_for_selector("#treeText")

        div_text = page.inner_text("#treeText")

        markdown_content = markdownify.markdownify(div_text, heading_style="ATX")

        with open("markdown.md", "w", encoding="utf-8") as file:
            file.write(markdown_content)

        browser.close()


# URL to crawl
url = "https://qavanin.ir/Law/TreeText/?IDS=15937310645561164886"

# Run crawler
crawl_page(url)
