import pandas as pd
import matplotlib.pyplot as plt

# Load processed dataset from Q5
df = pd.read_csv("processed_student_performance.csv")

plt.style.use(
    "seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")


# 1. Bar Chart: Student Names vs Final Scores
plt.figure(figsize=(12, 6))
# display top 20 for readability
plot_df = df

plt.bar(plot_df["Student"], plot_df["Final_Score"],
        color="#1f77b4", edgecolor="black")
plt.title("1. Student Names vs Final Scores", fontsize=14, fontweight="bold")
plt.xlabel("Student Name", fontsize=12)
plt.ylabel("Final Score", fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig("plots/final_scores.png", dpi=300)
plt.close()

# 2. Scatter Plot: Hours Studied vs Final Score

plt.figure(figsize=(8, 5))
plt.scatter(df["Hours_Studied"], df["Final_Score"],
            color="#2ca02c", alpha=0.7, edgecolors="none")
plt.title("2. Hours Studied vs Final Score", fontsize=14, fontweight="bold")
plt.xlabel("Hours Studied", fontsize=12)
plt.ylabel("Final Score", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("plots/study_vs_score.png", dpi=300)
plt.close()

# 3. Histogram: Distribution of Final Scores

plt.figure(figsize=(8, 5))
plt.hist(df["Final_Score"], bins=10, color="#d62728", edgecolor="white")
plt.title("3. Distribution of Final Scores", fontsize=14, fontweight="bold")
plt.xlabel("Final Score Range", fontsize=12)
plt.ylabel("Number of Students", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("plots/score_distribution.png", dpi=300)
plt.close()

# 4. Custom Plot: Attendance Category vs Final Scores (Box Plot)
plt.figure(figsize=(8, 5))
low_att = df[df["Attendance"] < 80]["Final_Score"]
high_att = df[df["Attendance"] >= 80]["Final_Score"]

plt.boxplot([low_att, high_att], tick_labels=["Attendance < 80%",
            "Attendance >= 80%"], patch_artist=True)
plt.title("4. Attendance Category vs Final Scores",
          fontsize=14, fontweight="bold")
plt.xlabel("Attendance Category", fontsize=12)
plt.ylabel("Final Score", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("plots/custom_plot.png", dpi=300)
plt.close()

print("All 4 plots successfully saved as PNG files!")
