# 📚 Popularity-Based Book Recommendation System

This project recommends books based on their popularity, calculated from metrics like the number of ratings and average rating.
It serves as a simple yet effective baseline recommender model for beginners and those exploring data-driven book suggestions.

## 🚀 Features

Ranks books using rating count and average rating

Displays top trending books

Simple, interpretable, and easy to extend

Implemented using Python and Jupyter Notebook

## 📁 Project Structure
Popularity-based-book-Recommendation-system/
├── data/                     # Dataset folder (contains Books.csv)
├── Popularity_based_book_recommendation.ipynb   # Main Jupyter Notebook
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
└── .gitignore

## 📊 Dataset

The dataset should contain book information such as:

Book-Title

Book-Author

Num_ratings

Avg_rating

## 📦 Recommended dataset: Book Recommendation Dataset on Kaggle

Place the dataset file (e.g., Books.csv) inside the data/ folder.

🛠 How to Run
1. Clone the repository
git clone https://github.com/saniya-154/Popularity-based-book-Recommendation-system.git
cd Popularity-based-book-Recommendation-system

2. Install dependencies
pip install -r requirements.txt


(If requirements.txt is missing, install manually:)

pip install pandas numpy matplotlib seaborn

3. Run the Notebook
jupyter notebook


Open Popularity_based_book_recommendation.ipynb and run all cells.

## 📈 Example Output
Rank	Book Title	Author	Avg Rating	Rating Count
1	The Hobbit	J.R.R. Tolkien	4.8	12,000
2	Harry Potter and the Sorcerer’s Stone	J.K. Rowling	4.7	10,500
3	The Da Vinci Code	Dan Brown	4.6	9,800

The notebook outputs the Top N most popular books based on computed scores.

## 💡 Future Scope

Integrate collaborative filtering for personalized recommendations

Add a Streamlit or Flask interface for web-based interaction

Implement genre-based filtering

Visualize user-book interactions

## 👩‍💻 Author

Made by Saniya Sayyed
