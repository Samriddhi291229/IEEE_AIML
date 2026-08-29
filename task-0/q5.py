import pandas as pd

# 1. Load the CSV into a DataFrame.
df = pd.read_csv("student_performance.csv")

# 2. Print the first five rows.
print("First 5 Rows:")
print(df.head(5))

# 3. Print the number of rows and columns.
rows, columns = df.shape
print(f"\nNumber of rows: {rows}, Number of columns: {columns}")

# 4. Display the column names.
print("\nColumn Names: ", end="")
print(df.columns.tolist())

# 5. Check whether the dataset contains missing values
print("\nMissing Values Count per Column :")
print(df.isnull().sum())

# 6. Calculate the average Final_Score
avg_final_score = df["Final_Score"].mean()
print(f"\nAverage Final Score: {avg_final_score:.2f}")

# 7. Find the student with the highest Final_Score
top_student_idx = df["Final_Score"].idxmax()
top_student = df.loc[top_student_idx]
print(
    f"\nStudent with Highest Final Score: {top_student['Student']} ({top_student['Final_Score']})")

# 8. Create a new column: Improvement = Final_Score - Previous_Score
df["Improvement"] = df["Final_Score"] - df["Previous_Score"]

# 9. Display only students with attendance greater than or equal to 80
high_attendance_df = df[df["Attendance"] >= 80]
print("\nStudents with Attendance >= 80% :")
print(high_attendance_df)

# 10. Sort the DataFrame by Final_Score in descending order
df_sorted = df.sort_values(by="Final_Score", ascending=False)
print("\nDataFrame Sorted by Final Score (Descending) ")
print(df_sorted.head())

# 11. Save the processed DataFrame as processed_student_performance.csv
df_sorted.to_csv("processed_student_performance.csv", index=False)
print("\nProcessed DataFrame successfully saved to 'processed_student_performance.csv'")
