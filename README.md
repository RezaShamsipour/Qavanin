## Installation
Follow these steps to install and run the project:

**1. Install Requirements**

First, install the required packages:
```bash
  pip install -r requirements.txt
```
* note: install in virtual environment.(Optional)

* note: that used on pytorch with **(CPU)** , you can install your version of pytorch : [PYTORCH Website](https://pytorch.org/get-started/previous-versions/)


**2. Install Playwright**
```bash
  playwright install
```

**3. Configure Pinecone**
We use Pinecone as our database. You need to create an account on the [PINECONE Website](https://pinecone.io)
```bash
  #app/services/pinecone_service.py

  
  pine_cone = Pinecone(api_key="YOUR_API")
    index = pine_cone.Index(
        "YOUR_INDEX", "YOUR_HOST"
    )
```
* note: in that project we use DIMENSIONS=768 also need create index with DIMENSIONS=768.

**4. Scrape Data**
You can scrape data from Qavanin.ir or use the default data in the <data_extraction> folder:

* The default folder contains 6 documents scraped from the site.

* To add custom documents, use **crawl.py**. Update the URL as needed:
```bash
url = "https://qavanin.ir/Law/TreeText/?IDS=12441882026455145609"
```
then run:
```bash
python crawl.py
```

**5. Import Data into the Database**
After scraping the data, import it into the database using **load_data.py**
```bash
python load_data.py
```

**6. Run the Project**
Finally, run the project with:
```bash
  python main.py
```
You should see:
```bash
  INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```
You can now access the API documentation at:
```bash
  http://127.0.0.1:8000/docs/
```

and work with swagger to search.


* The first 2 objects with the highest score are returned.
* if get : timeoutError, that is for internet , try more.

* used Model : **HooshvareLab/bert-fa-zwnj-base** from https://huggingface.co/ , So it can be a bit slow.


