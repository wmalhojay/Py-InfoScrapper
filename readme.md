# Movie Scraping and CSV Creation

This Python script scrapes a list of movies from Empire Online's website and extracts relevant data such as tags, classes, movie numbers, names, and brief descriptions. It utilizes the following libraries:

- `requests` for fetching the webpage content
- `BeautifulSoup` from `bs4` for parsing HTML
- `pandas` for organizing and exporting data to CSV

### Script Overview:
1. Imports necessary libraries:
   - `requests` for fetching webpage content
   - `BeautifulSoup` from `bs4` for parsing HTML
   - `DataFrame` from `pandas` for data manipulation

2. Defines the URL of the webpage to be scraped.

3. Sends a GET request to the URL and extracts the HTML content.

4. Uses `BeautifulSoup` to parse the HTML content and find all movie titles and descriptions.

5. Extracts:
   - Tag names associated with each movie
   - Classes associated with each movie
   - Movie numbers (extracted from the movie titles)
   - Actual movie names (cleaned from the movie titles)
   - Brief descriptions of each movie

6. Constructs a pandas `DataFrame` from the extracted data.

7. Writes the extracted data into a CSV file named "Movie.csv" using pandas functionality.

### Usage:
- Ensure you have Python installed with `requests`, `beautifulsoup4`, and `pandas` libraries.
- Run the script to scrape the desired webpage and generate the CSV file with movie data.

### Notes:
- Modify the URL variable (`url`) to scrape data from a different webpage if needed.
- The script assumes a specific HTML structure from the target webpage. Adjust parsing logic if the structure changes.
