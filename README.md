Mess App – Monthly Mess Bill Calculator

This is a Streamlit-based web application that allows hostel or PG residents to calculate their monthly mess and room fees based on the days they opt out of mess services (Mess Cuts). It features an interactive UI for selecting "Mess Cut" dates, performs fee calculations, and provides CSV/TXT exports and a visual bar chart to represent usage.

🧰 Features
📅 Interactive Calendar – Pick and view "Mess Cut" dates for any month and year.
💸 Automated Bill Calculation – Computes the total monthly fee based on room and daily mess charges.
💾 Data Export – Download mess cut data (.csv) and fee summary (.txt).
📊 Mess Usage Chart – Visual bar chart comparing mess vs cut days.
🔁 Reset Option – Clear all selected dates and inputs.
🌐 Web UI – Built using Streamlit for a smooth, browser-based experience.

🚀 How to Run
1. Prerequisites

Install required Python packages:
pip install streamlit matplotlib

2. Run the App
streamlit run mess_app_streamlit.py

The app will open in your default web browser.

🖱️ How to Use

Select the Month and Year you want to calculate for (from sidebar).
Enter Fees:
Room fee (monthly)
Mess fee (per day)
Choose Mess Cut Dates from the date selector.
Click "Calculate Mess Bill" to generate results.

Optionally:
Download the fee summary as a .txt file.
Download mess cut log as a .csv file.
View the Mess vs Cut Days bar chart.
Click "Reset" to start fresh.

🧮 Calculation Logic

Mess Cut Days: Number of days you opted out of mess service.
Mess Days = Total days in month − Mess Cut Days
Total Fee = Room Fee + (Mess Days × Mess Fee per Day)

📂 File Outputs

mess_data_<month>_<year>.csv: Logs each selected "Mess Cut" date.
mess_fee_result_<month>_<year>.txt: Fee calculation summary.

📎 Dependencies

streamlit
matplotlib
calendar, datetime, csv (Python built-ins)

📜 License

This project is open-source and available under the MIT License.

👤 Author

Developed by Sagar P
Feel free to fork, improve, and share!
