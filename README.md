📚 Popularity-Based Book Recommendation System
🚀 Project Overview

This project is a popularity-based book recommendation system that suggests books based on their overall popularity — determined by metrics like the number of ratings and average rating.
It serves as a simple yet effective baseline recommender model, ideal for learning and understanding the fundamentals of recommendation systems.

🎯 Objective

The goal is to recommend the most popular books to users using available data — without requiring personalized user profiles.

🧠 How It Works

Data Loading: Load and clean the dataset containing book titles, authors, and user ratings.

Aggregation: Compute popularity metrics such as:

Total number of ratings per book

Average rating per book

Filtering: Keep only books that meet a minimum rating threshold for reliability.

Ranking: Sort books based on popularity and display the top results.

📊 Dataset

The dataset used contains information such as:

Book-Title

Book-Author

Num_ratings

Avg_rating

You can use a public dataset from Kaggle such as:

Book Recommendation Dataset

Place your dataset in the project folder (e.g., Books.csv).

🧰 Tech Stack

Language: Python

Libraries: pandas, numpy, matplotlib, seaborn

Environment: Jupyter Notebook

⚙️ Steps to Run
1️⃣ Clone the Repository
git clone https://github.com/saniya-154/Popularity-based-book-Recommendation-system.git
cd Popularity-based-book-Recommendation-system

2️⃣ Install Dependencies
pip install -r requirements.txt


(If requirements.txt is missing, manually install with)

pip install pandas numpy matplotlib seaborn

3️⃣ Run the Notebook

Open Jupyter Notebook and run:

jupyter notebook


Then open and execute the file:

Popularity_based_book_recommendation.ipynb

📈 Example Output

The system outputs the Top N most popular books based on a weighted scoring system, such as:

Rank	Book Title	Author	Avg Rating	Rating Count
1	The Hobbit	J.R.R. Tolkien	4.8	12,000
2	Harry Potter and the Sorcerer’s Stone	J.K. Rowling	4.7	10,500
🔮 Future Improvements

Add collaborative filtering for personalized recommendations.

Integrate Flask / Streamlit for a web-based interface.

Include genre-based filters for more targeted suggestions.

💡 Learning Outcome

This project helps in understanding:

How basic recommender systems work

How to preprocess and analyze datasets

How to build a simple ranking model based on popularity

📜 License

This project is licensed under the MIT License.
Feel free to use, modify, and share it with attribution.

👩‍💻 Author

Saniya Sayyed
📧 GitHub Profile
