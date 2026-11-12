
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

# ----------------------------------
# PAGE CONFIGURATION
# ----------------------------------

st.set_page_config(
    page_title="Diabetes AI | Data Analysis",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Diabetes Quality of Life AI")
st.subheader("Dataset Inspection and Analysis Engine")

st.write(
    "Upload your research dataset to inspect its structure, "
    "quality and statistical characteristics."
)

st.divider()

# ----------------------------------
# DATASET UPLOAD
# ----------------------------------

uploaded_file = st.file_uploader(
    "Upload your dataset",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:

    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # ----------------------------------
        # BASIC INFORMATION
        # ----------------------------------

        st.success("Dataset loaded successfully!")

        st.header("1. Dataset Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Records", df.shape[0])

        with col2:
            st.metric("Total Variables", df.shape[1])

        with col3:
            st.metric("Missing Values", int(df.isna().sum().sum()))

        with col4:
            st.metric("Duplicate Rows", int(df.duplicated().sum()))

        # ----------------------------------
        # DATA PREVIEW
        # ----------------------------------

        st.header("2. Dataset Preview")

        st.dataframe(df.head(10), use_container_width=True)

        # ----------------------------------
        # DATA TYPES
        # ----------------------------------

        st.header("3. Variable Information")

        information = pd.DataFrame({
            "Variable": df.columns,
            "Data Type": df.dtypes.astype(str).values,
            "Missing Values": df.isna().sum().values,
            "Unique Values": df.nunique().values
        })

        st.dataframe(information, use_container_width=True)

        # ----------------------------------
        # MISSING VALUES
        # ----------------------------------

        st.header("4. Missing Values Analysis")

        missing = df.isnull().sum()
        missing = missing[missing > 0]

        if len(missing) > 0:

            missing_df = missing.reset_index()
            missing_df.columns = ["Variable", "Missing Count"]

            st.dataframe(missing_df, use_container_width=True)

            fig, ax = plt.subplots(figsize=(10, 4))
            sns.barplot(
                data=missing_df,
                x="Variable",
                y="Missing Count",
                ax=ax
            )
            ax.set_title("Missing Values by Variable")
            ax.tick_params(axis="x", rotation=45)
            plt.tight_layout()

            st.pyplot(fig)
            plt.close(fig)

        else:
            st.success("No missing values detected.")

        # ----------------------------------
        # STATISTICAL SUMMARY
        # ----------------------------------

        st.header("5. Statistical Summary")

        st.dataframe(
            df.describe(include="all").transpose(),
            use_container_width=True
        )

        # ----------------------------------
        # CORRELATION ANALYSIS
        # ----------------------------------

        st.header("6. Correlation Analysis")

        numeric_df = df.select_dtypes(include="number")

        if numeric_df.shape[1] >= 2:

            correlation = numeric_df.corr()

            fig, ax = plt.subplots(figsize=(10, 6))

            sns.heatmap(
                correlation,
                annot=True,
                cmap="coolwarm",
                fmt=".2f",
                ax=ax
            )

            ax.set_title("Variable Correlation Matrix")
            plt.tight_layout()

            st.pyplot(fig)
            plt.close(fig)

        else:
            st.info("At least two numeric variables are needed.")

        # ----------------------------------
        # DUPLICATES
        # ----------------------------------

        st.header("7. Duplicate Records")

        duplicate_count = int(df.duplicated().sum())

        if duplicate_count > 0:
            st.warning(
                f"{duplicate_count} duplicate records detected. "
                "No records have been deleted."
            )
        else:
            st.success("No duplicate records detected.")

        # ----------------------------------
        # EXPORT REPORT
        # ----------------------------------

        st.header("8. Export Dataset Report")

        report = BytesIO()

        with pd.ExcelWriter(report, engine="openpyxl") as writer:
            information.to_excel(
                writer, sheet_name="Variables", index=False
            )
            df.describe(include="all").transpose().to_excel(
                writer, sheet_name="Statistics"
            )
            missing.rename("Missing Count").to_excel(
                writer, sheet_name="Missing Values"
            )

        st.download_button(
            label="Download Analysis Report",
            data=report.getvalue(),
            file_name="diabetes_dataset_analysis.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as error:
        st.error(f"Dataset processing error: {error}")

else:

    st.info(
        "Upload a CSV or Excel dataset to begin the analysis."
    )

st.divider()

st.caption(
    "Diabetes Quality of Life AI | Research and Educational Use"
)
