# 🚗 Car-Analyst

**Car-Analyst** is a Python-based project that demonstrates an end-to-end data analysis pipeline to uncover trends in pricing, popular car models, and geographic sales distribution. It loads and cleans raw car sales data, computes model and regional statistics, creates visualizations, and exports results into a formatted Excel report.

### Key Features
- 🧹 **Data Preprocessing**  
  - Handles missing values and inconsistent entries  
  - Normalizes price and mileage data  
  - Converts registration year/month into proper datetime objects  

- 📈 **Statistical Analysis**  
  - Computes average car prices and model popularity  
  - Aggregates sales counts by region  

- 📊 **Data Visualization**  
  - Generates interactive histograms and bar charts using Matplotlib and Seaborn  

- 📗 **Automated Excel Report**  
  - Produces an Excel file (`Car_Analysis_Report.xlsx`)  
  - Includes summary tables, dynamic charts, and clean data sheets
 
## 📘 Technical Details

- **Language:** Python 3.9+
- **Libraries Used:**  
  - Pandas, NumPy, Seaborn, scikit-learn, XlsxWriter

## 🏗️ Project Structure
```
caranalyst/
│
├── preprocess.py         # Load, clean, and normalize raw data
├── analysis.py           # Compute summary statistics
├── visualize.py          # Generate data visualizations
├── report.py             # Write Excel report with charts
│
├── data/
│   └── autos.csv         # Raw eBay car sales dataset
│
└── main.py               # Main pipeline script        
```
## ⚙️ Installation

1. Download or clone this repository
2. Open the project folder
3. Create and activate a virtual environment
4. Install required dependencies
5. Place your dataset (autos.csv) inside the data/ folder (dataset availible on https://www.kaggle.com/datasets/sijovm/used-cars-data-from-ebay-kleinanzeigen/data)
6. Run the main analysis script
   
## 📜 License
This project is released under the MIT License.  
> Ironically, this project has a license… and I still don’t. 🚗💀😅
