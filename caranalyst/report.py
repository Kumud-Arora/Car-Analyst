import pandas as pd

def write_excel_report(
    df: pd.DataFrame,
    price_by_model: pd.DataFrame,
    sales_by_region: pd.Series,
    out_path: str = "Car_Analysis_Report.xlsx"
):
    with pd.ExcelWriter(out_path, engine="xlsxwriter") as writer:
        workbook  = writer.book
        # Cleaned data
        df.to_excel(writer, sheet_name="Cleaned Data", index=False)

        # Summary tables
        price_by_model.to_excel(writer, sheet_name="Summary", startrow=1)
        sales_by_region.to_frame("sales_count")\
                        .to_excel(writer, sheet_name="Summary", startrow=1, startcol=4)

        summary = writer.sheets["Summary"]

        # Avg Price by Model
        chart1 = workbook.add_chart({"type": "column"})
        chart1.add_series({
            "name":       "Avg Price",
            "categories": ["Summary", 2, 0,  2+len(price_by_model.head(8))-1, 0],
            "values":     ["Summary", 2, 1,  2+len(price_by_model.head(8))-1, 1],
        })
        chart1.set_title({"name": "Average Price by Model"})
        chart1.set_x_axis({"name": "Model"})
        chart1.set_y_axis({"name": "Avg Price (€)"})
        summary.insert_chart("A12", chart1, {"x_scale": 1.5, "y_scale": 1.5})

        # Sales by Region
        chart2 = workbook.add_chart({"type": "pie"})
        chart2.add_series({
            "name":       "Sales by Region",
            "categories": ["Summary", 2, 4,  2+len(sales_by_region)-1, 4],
            "values":     ["Summary", 2, 5,  2+len(sales_by_region)-1, 5],
        })
        chart2.set_title({"name": "Sales Distribution by Region"})
        summary.insert_chart("H12", chart2, {"x_scale": 1.2, "y_scale": 1.2})
