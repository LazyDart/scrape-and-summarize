# News Article Summarizer using Textrank and NLP

This script is a proof of concept for summarizing news articles related to the pharmaceutical company Novo Nordisk using Textrank and NLP. The program extracts relevant articles from Reuters' healthcare and pharmaceuticals subsite, processes the text, and generates a summary based on the importance of phrases and sentences.

## Directory Structure
- **./scrapefinnews**: Directory containing a Scrapy crawler for scraping financial news (not finished).
- **.dockerignore**: File specifying which files and directories to exclude when building a Docker image.
- **compose.yaml**: Configuration file for Docker Compose.
- **Dockerfile**: Instructions for building a Docker image.
- **README.md**: Project documentation.
- **requests and bfsoup tests.ipynb**: Jupyter Notebook with the main script for extracting and processing news articles.
- **requirements.txt**: List of Python packages required for the project.
- **spacy tests.ipynb**: Jupyter Notebook with tests for Spacy NLP.

## How to Use

1. Install the required packages using the command:
   ```
   pip install -r requirements.txt
   ```

2. Run the script `requests and bfsoup tests.ipynb` to extract, process, and summarize news articles. Note that the project was not finished due to legal concerns related to scraping news articles.

## Requirements
- beautifulsoup4==4.12.2
- icecream==2.1.3
- itemadapter==0.8.0
- numpy==1.23.5
- pandas==2.0.0
- pytextrank==3.2.5
- Requests==2.31.0
- scikit_learn==1.2.2
- Scrapy==2.11.0
- spacy==3.7.2

## Legal Considerations
Please be aware of the legal implications of scraping news articles. It's essential to review and comply with the terms of service of the websites you are scraping data from. Scraping without permission may violate the website's terms and conditions.

## Notes
- The project was not completed due to legal concerns, and it is recommended to consult with legal professionals before proceeding with web scraping activities.
- The Scrapy crawler in the `./scrapefinnews` directory is not finished and may require further development.

Feel free to contribute to the project or customize it for your specific use case.