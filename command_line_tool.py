# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape Stack Overflow data
def scrape_stackoverflow(tag='python', query_filter='Votes', num_pages=1):
    # Base URL for Stack Overflow questions
    base_url = 'https://stackoverflow.com/questions/tagged/'
    url = f"{base_url}{tag}?tab={query_filter}"

    # Function to scrape a single page
    def scrape_page(url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            post_summaries = soup.find_all(class_=['s-post-summary'])
            data = []
            for post_summary in post_summaries:
                question_title = post_summary.find(class_='s-post-summary--content-title').text.strip()
                votes = post_summary.find(class_='s-post-summary--stats-item-number').text.strip()
                tags = post_summary.find(class_='tags').text.strip()
                post_data = {
                    'question_title': question_title,
                    'votes': votes,
                    'tags': tags
                }
                data.append(post_data)
            return data

    # Scrape multiple pages
    all_data = []
    for page_num in range(1, num_pages + 1):
        url_with_page = f"{url}&page={page_num}"
        page_data = scrape_page(url_with_page)
        all_data.extend(page_data)

    return all_data

# Function to run the script
def run_script(tag='python', query_filter='Votes', num_pages=1, output_file='output.csv'):
    # Scrape Stack Overflow data
    stackoverflow_data = scrape_stackoverflow(tag, query_filter, num_pages)

    # Convert the data to a DataFrame
    df = pd.DataFrame(stackoverflow_data)

    # Save the DataFrame to a CSV file
    df.to_csv(output_file, index=False)

# Run the script with default parameters
run_script()
