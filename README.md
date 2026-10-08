# Flight Analytics Dashboard

A Streamlit application that queries a MySQL flight dataset and presents route
search results alongside interactive airline, airport and daily-frequency charts.

## Features

- Search available flights between a source and destination.
- Compare airline frequency using a Plotly pie chart.
- Review airport activity and daily flight counts.
- Keep database queries in a dedicated helper module.

## Stack

Python, Streamlit, MySQL Connector/Python and Plotly.

## Run locally

```bash
git clone https://github.com/BrahminPulkit/Flight-SQL-App.git
cd Flight-SQL-App
python -m venv .venv
# Activate the virtual environment for your operating system.
python -m pip install -r requirements.txt
```

Create a local MySQL database and import your flight dataset into `flights_data`.
The application expects these columns: `Airline`, `Source`, `Destination`,
`Route`, `Dep_Time`, `Duration`, `Price` and `Date_of_Journey`.
The dataset and a database dump are not included in this repository.

Set the connection values in your terminal. PowerShell example:

```powershell
$env:MYSQL_HOST = "127.0.0.1"
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "<your-local-database-password>"
$env:MYSQL_DATABASE = "flight"
python -m streamlit run app.py
```

Use a local database account with access to the imported data. Credentials are
read from the process environment; keep them out of Git. A `.env` file is not
automatically loaded by this application.

## Files

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit interface and charts |
| `dbhelper.py` | Parameterized route queries and aggregate queries |
| `crud.py` | Separate database-learning script using an `airport` table |

`crud.py` contains write operations for its practice database; it is not needed
to launch the dashboard. Set `MYSQL_DATABASE` explicitly before using it.

## Related analysis

[Flight SQL Case Study](https://github.com/BrahminPulkit/flight-sql-case-study)
contains date-time and route-analysis exercises. Its table is named `flights`;
the dashboard expects `flights_data`, so adapt your import accordingly.

## Connection and query smoke checks

```bash
python -m unittest discover -s tests -v
```

Two database-independent checks validate environment-based connection settings
and parameterized route inputs. They mock the connector and do not verify a live
MySQL instance. The Python dependency set was installed in a clean environment;
a complete dashboard run still requires the external flight dataset/database.
