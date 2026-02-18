from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

documents=[
    "Alternating subarray prefix",
"Count Subarrays",
"Sums in a Triangle",
"Event Organizer",
"Binary Substituition",
"Magic Rankings",
"SUPW",
"IPL",
"Break Up",
"Fibonacci Series",
"Maximal crosses",
"The White Knight",
"Maximizing LCS",
"CAO Stage-2",
"Dish Distribution",
"Count palindromes",
"Barcelona Gameplay Tactics",
"Bamboo Art",
"Calvins Game",
"Longest Increasing Subsequence",
"Easy Tiling",
"Little Red Riding Hood"
]

# Assuming you already did this:
vectorizer = TfidfVectorizer()
transformed_output = vectorizer.fit_transform(documents)

# Convert sparse matrix to array
tfidf_array = transformed_output.toarray()

# Get feature (word) names
feature_names = vectorizer.get_feature_names_out()

# Create DataFrame
df = pd.DataFrame(tfidf_array, columns=feature_names)

# Save to CSV
df.to_csv("tf-idf.csv", index=False)
