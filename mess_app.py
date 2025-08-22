import streamlit as st
from datetime import datetime, date
import calendar
import csv
import matplotlib.pyplot as plt

# App Title
st.title("🍽️ Mess App – Monthly Mess Fee Calculator")

# Session state for persistent selections
if 'mess_cut_dates' not in st.session_state:
    st.session_state.mess_cut_dates = set()

# --- Sidebar Inputs ---
st.sidebar.header("🧾 Enter Fee Details")
room_fee = st.sidebar.number_input("Room Fee (per month)", min_value=0, step=100)
mess_fee = st.sidebar.number_input("Mess Fee (per day)", min_value=0, step=10)

selected_month = st.sidebar.selectbox("Month", list(calendar.month_name)[1:], index=datetime.now().month - 1)
selected_year = st.sidebar.number_input("Year", value=datetime.now().year, step=1)

# --- Date Selection ---
st.subheader("📅 Select Mess Cut Dates")

_, total_days = calendar.monthrange(selected_year, list(calendar.month_name).index(selected_month))
all_dates = [date(selected_year, list(calendar.month_name).index(selected_month), d) for d in range(1, total_days + 1)]

selected = st.multiselect("Pick the days you will **cut** the mess", all_dates, format_func=lambda x: x.strftime("%b %d, %Y"))

# Save to session state
st.session_state.mess_cut_dates = set(selected)

# --- Calculate Button ---
if st.button("📊 Calculate Mess Bill"):
    mess_cut_days = len(st.session_state.mess_cut_dates)
    mess_days = total_days - mess_cut_days
    mess_total = mess_days * mess_fee
    total = room_fee + mess_total

    # Show result
    st.markdown("### 💰 Fee Summary")
    st.markdown(f"**Month:** {selected_month} {selected_year}")
    st.markdown(f"**Mess Days:** {mess_days} / {total_days}")
    st.markdown(f"**Mess Bill:** {mess_days} × {mess_fee} = ₹{mess_total}")
    st.markdown(f"**Room Fee:** ₹{room_fee}")
    st.markdown(f"**Total Fee:** ₹{total}")

    # Save to .txt file
    result_txt = (
        f"Month: {selected_month} {selected_year}\n"
        f"Mess Days: {mess_days} / {total_days}\n"
        f"Mess Bill: {mess_days} x {mess_fee} = ₹{mess_total}\n"
        f"Room Fee: ₹{room_fee}\n"
        f"Total Fee: ₹{total}"
    )
    filename_txt = f"mess_fee_result_{selected_month}_{selected_year}.txt"
    st.download_button("📥 Download Summary", result_txt, file_name=filename_txt)

    # Save to CSV
    filename_csv = f"mess_data_{selected_month}_{selected_year}.csv"
    with open(filename_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Status"])
        for d in sorted(st.session_state.mess_cut_dates):
            writer.writerow([d.strftime("%Y-%m-%d"), "Mess Cut"])
    with open(filename_csv, 'r') as f:
        st.download_button("📥 Download Mess Cut Data (CSV)", f, file_name=filename_csv)

    # Plot chart
    st.subheader("📊 Mess vs Cut Days")
    fig, ax = plt.subplots()
    ax.bar(["Mess", "Cut"], [mess_days, mess_cut_days], color=["skyblue", "salmon"])
    ax.set_ylabel("Days")
    ax.set_title("Mess vs Cut Days")
    st.pyplot(fig)

# --- Reset Button ---
if st.button("🔄 Reset"):
    st.session_state.mess_cut_dates = set()
    st.experimental_rerun()
