import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_dataset.csv")

# Clean Price column
df["Price"] = (
    df["Price"]
    .str.replace("Â£", "", regex=False)
    .str.replace("£", "", regex=False)
    .astype(float)
)

# -------------------------------
# 1. Rating Distribution
# -------------------------------
rating_counts = df["Rating"].value_counts()

plt.figure(figsize=(8, 5))
rating_counts.plot(kind="bar")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()


# -------------------------------
# 2. Book Price Distribution
# -------------------------------
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=5)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()


# -------------------------------
# 3. Top 10 Most Expensive Books
# -------------------------------
top_books = df.sort_values("Price", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_books["Title"], top_books["Price"])
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top_10_expensive_books.png")
plt.show()


# -------------------------------
# 4. Price vs Rating
# -------------------------------
rating_order = ["One", "Two", "Three", "Four", "Five"]

plt.figure(figsize=(8, 5))
df.boxplot(column="Price", by="Rating", grid=False)
plt.title("Price Distribution by Rating")
plt.suptitle("")
plt.xlabel("Rating")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.savefig("price_vs_rating.png")
plt.show()


# -------------------------------
# Summary
# -------------------------------
print("===== DATA VISUALIZATION SUMMARY =====")
print("Total books:", len(df))
print("Average price: £", round(df["Price"].mean(), 2))
print("Minimum price: £", round(df["Price"].min(), 2))
print("Maximum price: £", round(df["Price"].max(), 2))
print("Most common rating:", df["Rating"].mode()[0])
print("Most common availability:", df["Availability"].mode()[0])

print("\nCharts created successfully:")
print("1. rating_distribution.png")
print("2. price_distribution.png")
print("3. top_10_expensive_books.png")
print("4. price_vs_rating.png")