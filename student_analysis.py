# student_analysis.py

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Student Test Score Analysis System",
    layout="centered"
)

st.title("Student Test Score Analysis System")
st.subheader("English Course")
st.write("Enter data for THREE (3) students only.")


# Question 2(a): Streamlit interface for three students
with st.form("student_form"):
    student_entries = []

    for i in range(1, 4):
        st.subheader(f"Student {i}")

        student_name = st.text_input(
            f"Enter Student Name {i}",
            key=f"name_{i}"
        )

        gender = st.radio(
            f"Select Gender {i}",
            options=["Male", "Female"],
            key=f"gender_{i}"
        )

        score = st.number_input(
            f"Enter Score {i}",
            min_value=0,
            max_value=100,
            value=0,
            step=1,
            key=f"score_{i}"
        )

        student_entries.append({
            "Student Name": student_name,
            "Gender": gender,
            "Score": score
        })

    submitted = st.form_submit_button("Submit")


if submitted:
    # Question 2(b): Exception handling and validation
    try:
        validated_students = []

        for i, student in enumerate(student_entries, start=1):
            name = student["Student Name"].strip()
            score = float(student["Score"])

            if not name:
                raise ValueError(
                    f"Student {i}: Student name cannot be empty."
                )

            if not np.isfinite(score) or not 0 <= score <= 100:
                raise ValueError(
                    f"Student {i}: Score must be between 0 and 100."
                )

            validated_students.append({
                "Student Name": name,
                "Gender": student["Gender"],
                "Score": score
            })

    except (ValueError, TypeError) as error:
        st.error(f"Invalid input: {error}")

    else:
        st.success("Data for all three students submitted successfully.")

        # Question 2(c): Store scores in a NumPy array
        scores = np.array(
            [student["Score"] for student in validated_students],
            dtype=float
        )

        mean_score = np.mean(scores)
        maximum_score = np.max(scores)
        sorted_scores = np.sort(scores)

        st.header("NumPy Analysis")
        st.write(f"Mean Score: {mean_score:.2f}")
        st.write(f"Maximum Score: {maximum_score:.2f}")
        st.write("Sorted Scores (Ascending):", sorted_scores)

        # Question 2(d): Create a Pandas DataFrame
        df = pd.DataFrame(validated_students)

        # Question 2(e): Classify results
        df["Result"] = np.where(
            df["Score"] >= 50,
            "Pass",
            "Fail"
        )

        st.header("Student Data")
        st.dataframe(
            df,
            hide_index=True,
            use_container_width=True
        )

        # Sort complete records to preserve name-score relationships
        sorted_df = df.sort_values(
            by="Score",
            ascending=True,
            kind="stable"
        ).reset_index(drop=True)

        st.subheader("Student Data Sorted by Score (Ascending)")
        st.dataframe(
            sorted_df,
            hide_index=True,
            use_container_width=True
        )

        # Visualize student scores
        st.header("Score Chart")

        fig, ax = plt.subplots(figsize=(8, 5))

        # Numeric positions keep separate bars even for duplicate names
        positions = np.arange(len(df))

        ax.bar(
            positions,
            df["Score"],
            color="steelblue"
        )

        ax.set_xticks(positions)
        ax.set_xticklabels(df["Student Name"])
        ax.set_title("Student Scores")
        ax.set_xlabel("Student Name")
        ax.set_ylabel("Score")
        ax.set_ylim(0, 110)

        for position, score in zip(positions, df["Score"]):
            ax.text(
                position,
                score + 1,
                f"{score:g}",
                ha="center",
                va="bottom"
            )

        fig.tight_layout()
        st.pyplot(fig)
        plt.close(fig)