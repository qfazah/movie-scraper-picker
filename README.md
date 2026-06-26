# Movie Scraper and Selector

A Python-based automation tool that handles web scraping and file management to help you decide what movie to watch next. It scrapes top movie titles from the web, stores them locally, and serves a random recommendation while keeping track of your watch history.

---

## 🛠️ Built With (Technologies & Concepts)

This project utilizes several core Python libraries and programming concepts to achieve automation:

* **Web Scraping (`BeautifulSoup4`):** Parses HTML structure to accurately target and extract movie titles from the web.
* **HTTP Requests (`requests`):** Simulates browser requests with custom headers to safely fetch online webpage data.
* **File Handling (`os` & File I/O):** Manages local data persistence by checking file existence, reading records, and safely overwriting lists.
* **Data Manipulation (`random`):** Implements randomized selection logic and handles array filtering to remove elements after selection.

---

## 🚀 How It Works

### Step 1: Web Scraping & Storage
The script checks if a local database file (`movie_names_file.txt`) exists. If it doesn't, it sends an HTTP request to Empire Online, scrapes the top movie headings using `BeautifulSoup`, cleans the data, and saves them to the file.

### Step 2: Random Selection & Tracking
When you run the script, it reads the local text file and picks a random movie. To ensure you never get the same recommendation twice, it automatically deletes the chosen movie from the list and updates the text file.

---

## 💻 Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/movie-scraper-and-selector.git](https://github.com/YOUR-USERNAME/movie-scraper-and-selector.git)
   cd movie-scraper-and-selector
