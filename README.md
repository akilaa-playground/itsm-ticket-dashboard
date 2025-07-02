# 📊 ITSM Ticket Dashboard (Dummy Data)

## 📌 What This Project Does

Builds a simple dashboard to visualize dummy ITSM ticket data (incidents, problems, changes) using **Streamlit**.

---

## 📂 Project Structure

- `app.py`: Main dashboard code (Streamlit)
- `data/tickets.csv`: Dummy ticket data (Incidents, Changes, Problems)
- `README.md`: Project overview and instructions

---

## ▶️ How to Run

### 🧰 Requirements

```bash
pip install streamlit pandas matplotlib
```

### ▶️ Run the Dashboard

```bash
streamlit run app.py
```

```bash
http://localhost:8501
```

---

## 📊 Sample Dashboard Features

- Bar charts for ticket counts by type
- Line chart showing ticket trends over time
- Pie chart for ticket status distribution
- Filter by ticket type, status, or priority

---

## 📝 Sample Dummy Data Format (`tickets.csv`)

```
TicketID,Type,Status,Priority,CreatedDate
1001,Incident,Open,High,2023-01-01
1002,Change,Closed,Low,2023-01-02
1003,Problem,In Progress,Medium,2023-01-02
...
```

---

## ✅ Skills Demonstrated

- ITSM workflows (Incident, Change, Problem)
- Data visualization and filtering
- Frontend dashboards (Streamlit/Flask)
- Python scripting and pandas


---

## 🚀 Future Enhancements

- Connect to real ITSM APIs (e.g., ServiceNow)
- Export filtered data
- Role-based dashboard views
- Add drill-down by ticket

---

