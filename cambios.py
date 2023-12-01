from supabase_py import create_client, Client

url: str = "https://pmsrnmhwxxwxedqiavzr.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBtc3JubWh3eHh3eGVkcWlhdnpyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDE0NDI3ODMsImV4cCI6MjAxNzAxODc4M30.11nKPwxSUCAvB-nEjfIgjBPS0tP2NepQ2eJ1oF81Xwg"

supabase: Client = create_client(url, key)

# Realizar una consulta
rows = supabase.table("nombre_de_tu_tabla").select("*").execute()

# Imprimir los resultados
for row in rows['data']:
    print(row)