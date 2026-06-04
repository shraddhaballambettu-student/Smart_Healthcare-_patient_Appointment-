def generate_insights(df):

    insights=[]

    highest_revenue_dept = (
        df.groupby("department")
        ["total_bill"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"Highest revenue department is {highest_revenue_dept}"
    )

    avg_wait = df[
        "waiting_time_minutes"
    ].mean()

    insights.append(
        f"Average waiting time is {avg_wait:.2f} minutes"
    )

    satisfaction = df[
        "patient_satisfaction_score"
    ].mean()

    insights.append(
        f"Patient satisfaction score is {satisfaction:.2f}"
    )

    return insights
