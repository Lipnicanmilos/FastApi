source fastapi-env/Scripts/activate
uvicorn main:app --reload --host 127.0.0.1 --port 8080

source fastapi-env/Scripts/activate
uvicorn blog.main:app --reload --host 127.0.0.1 --port 8080

python main.py

# -- http://127.0.0.1:8000/
# uvicorn main:milos_app reload

#    http://127.0.0.1:8000/docs/
#    http://127.0.0.1:8000/redoc

# pgadmin

# C:\Users\mlipnican>cd c:\pgsql\bin

# c:\pgsql\bin>pg_ctl -D ^"C^:^\Postgres15^\data^" -l logfile start

# c:\pgsql\bin>pg_ctl -D ^"C^:^\Postgres15^\data^" -l logfile stop

# ----------------------
# pgadmin
# C:\pgsql\pgAdmin 4\bin

# doplneny modul ktory treba nainstalovat do suboru a spusteny prikaz
# pip install -r requirements.txt 

# 3:14 operators -- API ROUTES