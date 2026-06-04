def generate_business_insights(df):

    insights = []

    highest_revenue = (
        df.groupby("department")
        ["total_bill"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"Highest Revenue Department: {highest_revenue}"
    )

    avg_wait = (
        df["waiting_time_minutes"]
        .mean()
    )

    insights.append(
        f"Average Waiting Time: {avg_wait:.2f} mins"
    )

    no_show_rate = (
        (df["appointment_status"] == "No Show")
        .mean()
        * 100
    )

    insights.append(
        f"No Show Rate: {no_show_rate:.2f}%"
    )

    return insights
