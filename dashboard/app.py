import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Diabetes Glucose Prediction Dashboard",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------
# Helper function
# -----------------------------
@st.cache_data
def load_csv(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    return None


# -----------------------------
# File paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

tuned_results_path = os.path.join(BASE_DIR, "reports", "final_model_metrics.csv")
predictions_path = os.path.join(BASE_DIR, "reports", "final_model_predictions_with_residuals.csv")
feature_path = os.path.join(BASE_DIR, "reports", "final_model_feature_importance.csv")

results_df = load_csv(tuned_results_path)
predictions_df = load_csv(predictions_path)
features_df = load_csv(feature_path)


# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Dashboard Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Project Overview",
        "Final Model Metrics",
        "Actual vs Predicted",
        "Residual Analysis",
        "Feature Importance",
        "Limitations and Conclusions"
    ]
)


# -----------------------------
# Title
# -----------------------------
st.title("Diabetes Glucose Prediction Dashboard")

st.markdown(
    """
    This dashboard presents the final results of the diabetes glucose prediction project.
    The goal of the project is to analyze patient glucose patterns and evaluate machine learning models
    for glucose prediction.
    """
)


# -----------------------------
# Page 1: Project Overview
# -----------------------------
if page == "Project Overview":
    st.header("Project Overview")

    st.markdown(
        """
        This project uses diabetes time-series data to analyze glucose behavior and build a machine learning model
        that predicts glucose levels.

        The full project workflow includes:

        - Data understanding
        - Data cleaning and preprocessing
        - Exploratory data analysis
        - Feature engineering
        - Baseline modeling
        - Hyperparameter tuning
        - Final model evaluation
        - Dashboard creation
        """
    )

    st.subheader("Final Model")

    st.markdown(
        """
        The final selected model is a tuned Random Forest Regressor.

        This model was selected because it can capture nonlinear relationships and performed better than simpler
        baseline models.
        """
    )


# -----------------------------
# Page 2: Final Model Metrics
# -----------------------------
elif page == "Final Model Metrics":
    st.header("Final Model Metrics")

    if results_df is not None:
        st.dataframe(results_df)

        numeric_cols = results_df.select_dtypes(include="number").columns.tolist()

        if len(numeric_cols) > 0:
            st.subheader("Metric Summary")
            st.write(results_df[numeric_cols].describe())
    else:
        st.error("tuned_model_results.csv was not found in the outputs folder.")


# -----------------------------
# Page 3: Actual vs Predicted
# -----------------------------
elif page == "Actual vs Predicted":
    st.header("Actual vs Predicted Glucose Values")

    if predictions_df is not None:
        st.dataframe(predictions_df.head())

        st.markdown("### Available Columns")
        st.write(predictions_df.columns.tolist())

        possible_actual_cols = ["actual_glucose", "y_true", "actual", "glucose"]
        possible_pred_cols = ["predicted_glucose", "y_pred", "predicted", "prediction"]

        actual_col = next((col for col in possible_actual_cols if col in predictions_df.columns), None)
        pred_col = next((col for col in possible_pred_cols if col in predictions_df.columns), None)

        if actual_col and pred_col:
            fig = px.scatter(
                predictions_df,
                x=actual_col,
                y=pred_col,
                title="Actual vs Predicted Glucose",
                labels={
                    actual_col: "Actual Glucose",
                    pred_col: "Predicted Glucose"
                }
            )

            fig.add_shape(
                type="line",
                x0=predictions_df[actual_col].min(),
                y0=predictions_df[actual_col].min(),
                x1=predictions_df[actual_col].max(),
                y1=predictions_df[actual_col].max(),
                line=dict(dash="dash")
            )

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning(
                "Could not automatically find actual and predicted columns. "
                "Please check your tuned_model_predictions.csv column names."
            )
    else:
        st.error("tuned_model_predictions.csv was not found in the outputs folder.")


# -----------------------------
# Page 4: Residual Analysis
# -----------------------------
elif page == "Residual Analysis":
    st.header("Residual Analysis")

    if predictions_df is not None:
        possible_actual_cols = ["actual_glucose", "y_true", "actual", "glucose"]
        possible_pred_cols = ["predicted_glucose", "y_pred", "predicted", "prediction"]

        actual_col = next((col for col in possible_actual_cols if col in predictions_df.columns), None)
        pred_col = next((col for col in possible_pred_cols if col in predictions_df.columns), None)

        if actual_col and pred_col:
            predictions_df["residual"] = predictions_df[actual_col] - predictions_df[pred_col]

            fig = px.histogram(
                predictions_df,
                x="residual",
                nbins=50,
                title="Residual Distribution",
                labels={"residual": "Residual"}
            )

            st.plotly_chart(fig, use_container_width=True)

            fig2 = px.scatter(
                predictions_df,
                x=pred_col,
                y="residual",
                title="Residuals vs Predicted Glucose",
                labels={
                    pred_col: "Predicted Glucose",
                    "residual": "Residual"
                }
            )

            fig2.add_hline(y=0, line_dash="dash")

            st.plotly_chart(fig2, use_container_width=True)

            st.markdown(
                """
                Residuals show the difference between actual and predicted glucose values.
                A good model should have residuals centered around zero with no strong pattern.
                """
            )
        else:
            st.warning("Could not find actual and predicted columns for residual analysis.")
    else:
        st.error("tuned_model_predictions.csv was not found in the outputs folder.")


# -----------------------------
# Page 5: Feature Importance
# -----------------------------
elif page == "Feature Importance":

    st.header("Feature Importance")

    if features_df is not None:

        st.dataframe(features_df.head(15))

        if {"feature", "importance"}.issubset(features_df.columns):

            fig = px.bar(
                features_df.sort_values(
                    "importance",
                    ascending=False
                ).head(15),
                x="importance",
                y="feature",
                orientation="h",
                title="Top 15 Most Important Features"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            st.markdown(
                """
                Feature importance shows which variables contributed most
                to glucose prediction in the final Random Forest model.

                Higher importance values indicate stronger influence on
                model predictions.
                """
            )

        else:
            st.warning(
                "Feature importance columns were not found."
            )

    else:
        st.error(
            "final_model_feature_importance.csv was not found in the outputs folder."
        )

# -----------------------------
# Page 6: Limitations and Conclusions
# -----------------------------
elif page == "Limitations and Conclusions":
    st.header("Model Limitations and Conclusions")

    st.subheader("Limitations")

    st.markdown(
        """
        - The dataset contains a limited number of patients.
        - Glucose behavior can vary significantly between individuals.
        - External factors such as sleep, stress, illness, and meal composition were not fully captured.
        - Random train-test splits may overestimate performance for time-series data.
        - The model is for educational and analytical purposes only.
        - The model should not be used for medical decision-making.
        """
    )

    st.subheader("Conclusions")

    st.markdown(
        """
        The final tuned Random Forest model showed improved performance compared with simpler baseline models.
        Lag glucose features and rolling glucose features were especially useful for prediction.

        This project demonstrates a complete end-to-end data analytics and machine learning workflow, including
        data preparation, modeling, evaluation, interpretation, and dashboard presentation.
        """
    )