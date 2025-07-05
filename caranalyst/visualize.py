import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_dist(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df["price"], bins=50, kde=True)
    plt.title("Price Distribution")
    plt.xlabel("Price (€)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

def plot_avg_price_by_model(price_by_model, top_n=8):
    top = price_by_model.head(top_n).reset_index()
    plt.figure(figsize=(10,6))
    sns.barplot(data=top, x="model", y="mean")
    plt.title(f"Average Price by Model (Top {top_n} by Count)")
    plt.xlabel("Model")
    plt.ylabel("Avg Price (€)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
