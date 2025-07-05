from caranalyst.preprocess import load_data, clean, normalize
from caranalyst.analysis  import compute_price_by_model, compute_sales_by_region
from caranalyst.visualize import plot_price_dist, plot_avg_price_by_model
from caranalyst.report    import write_excel_report

def main():
    # Load & prep
    df = load_data("data/autos.csv")
    df = clean(df)
    df = normalize(df)

    # Compute summaries
    price_by_model  = compute_price_by_model(df)
    sales_by_region = compute_sales_by_region(df)

    # Visualize
    plot_price_dist(df)
    plot_avg_price_by_model(price_by_model)

    # Export Excel report
    write_excel_report(df, price_by_model, sales_by_region)
    print("Report written to Car_Analysis_Report.xlsx")

if __name__ == "__main__":
    main()
