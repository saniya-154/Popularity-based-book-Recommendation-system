from flask import Flask,render_template,request, jsonify
import pickle
import numpy as np
import difflib
import pandas as pd

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity_score = pickle.load(open('similarity_score.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author = list(popular_df['Book-Author'].values),
                           image = list(popular_df['Image-URL-M'].values),
                           votes  = list(popular_df['num_ratings'].values),
                           ratings = list(popular_df['avg_ratings'].values),
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

# @app.route('/recommend_books',methods=['post'])
# def recommend():
#     user_input = request.form.get('user_input')
#     if user_input in pt.index:
#         index = np.where(pt.index == user_input)[0][0]
#         similar_items = sorted(list(enumerate(similarity_score[index])),key=lambda x:x[1],reverse=True)[1:5]

#         data = []
#         for i in similar_items:
#             item = []
#             temp_df = books[books['Book-Title'] == pt.index[i[0]]]
#             item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
#             item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
#             item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
#             item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-ISBN'].values))
#             data.append(item)
#         print(data)
#         print(pt.index)
#         print(user_input)
#         return str(user_input) 
#     else:
#         close_matches = difflib.get_close_matches(user_input, pt.index, n=3, cutoff=0.5)
#         return f"Book not found. Did you mean: {', '.join(close_matches)}?"
@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    
    # Clean and normalize user input
    user_input = user_input.strip()
    
    if not user_input:
        return render_template('recommend.html', error="Please enter a book title")
    
    # Check if exact match exists in pivot table
    if user_input in pt.index:
        # Get recommendations using collaborative filtering
        index = np.where(pt.index == user_input)[0][0]
        similar_items = sorted(
            list(enumerate(similarity_score[index])), 
            key=lambda x: x[1], 
            reverse=True
        )[1:6]  # Get top 5 similar books (excluding the input book itself)
        
        data = []
        for i in similar_items:
            try:
                # Get book details from the original books dataframe
                book_title = pt.index[i[0]]
                temp_df = books[books['Book-Title'] == book_title]
                
                if not temp_df.empty:
                    # Get unique book details
                    book_data = temp_df.drop_duplicates('Book-Title').iloc[0]
                    
                    item = {
                        'title': book_data['Book-Title'],
                        'author': book_data['Book-Author'],
                        'image_url': book_data['Image-URL-M'],
                        'isbn': book_data.get('Book-ISBN', 'N/A'),
                        'similarity_score': round(i[1], 3)  # Include similarity score
                    }
                    data.append(item)
            except Exception as e:
                print(f"Error processing book {i[0]}: {e}")
                continue
        
        return render_template('recommend.html', 
                             recommendations=data, 
                             input_book=user_input,
                             found=True)
    
    else:
        # Try to find close matches
        close_matches = difflib.get_close_matches(user_input, pt.index, n=5, cutoff=0.6)
        
        if close_matches:
            return render_template('recommend.html', 
                                 suggestions=close_matches,
                                 input_book=user_input,
                                 found=False)
        else:
            # Fallback: search for partial matches in book titles
            partial_matches = books[books['Book-Title'].str.contains(user_input, case=False, na=False)]
            
            if not partial_matches.empty:
                # Get top 5 partial matches that exist in pivot table
                valid_matches = []
                for _, book in partial_matches.iterrows():
                    if book['Book-Title'] in pt.index:
                        valid_matches.append(book['Book-Title'])
                    if len(valid_matches) >= 5:
                        break
                
                if valid_matches:
                    return render_template('recommend.html', 
                                         suggestions=valid_matches,
                                         input_book=user_input,
                                         found=False,
                                         partial_match=True)
            
            return render_template('recommend.html', 
                                 error=f"Sorry, no books found matching '{user_input}'. Try a different title.",
                                 input_book=user_input,
                                 found=False)


# Additional helper function for better search
def search_books(query, limit=10):
    """
    Enhanced search function that looks for books by title or author
    """
    query = query.lower().strip()
    
    # Search in titles
    title_matches = books[books['Book-Title'].str.lower().str.contains(query, na=False)]
    
    # Search in authors  
    author_matches = books[books['Book-Author'].str.lower().str.contains(query, na=False)]
    
    # Combine and remove duplicates
    all_matches = pd.concat([title_matches, author_matches]).drop_duplicates('Book-Title')
    
    # Filter only books that exist in our pivot table (have enough ratings)
    valid_matches = all_matches[all_matches['Book-Title'].isin(pt.index)]
    
    return valid_matches.head(limit)


# Optional: Add an autocomplete endpoint
@app.route('/autocomplete')
def autocomplete():
    query = request.args.get('q', '')
    if len(query) < 2:
        return jsonify([])
    
    # Get matching book titles from pivot table
    matches = [title for title in pt.index if query.lower() in title.lower()][:10]
    return jsonify(matches)

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Optional: Get popular books endpoint
@app.route('/popular_books')
def popular_books():
    """
    Get most popular books based on number of ratings
    """
    try:
        # Count ratings per book
        book_counts = books.groupby('Book-Title').size().sort_values(ascending=False)
        
        # Get top books that exist in pivot table
        popular_books_list = []
        for book_title in book_counts.index[:20]:
            if book_title in pt.index:
                book_data = books[books['Book-Title'] == book_title].iloc[0]
                popular_books_list.append({
                    'title': book_data['Book-Title'],
                    'author': book_data['Book-Author'],
                    'image_url': book_data['Image-URL-M'],
                    'rating_count': book_counts[book_title]
                })
            if len(popular_books_list) >= 10:
                break
                
        return render_template('popular.html', books=popular_books_list)
    except Exception as e:
        return f"Error: {e}"
if __name__ == '__main__':
    app.run(debug=True)