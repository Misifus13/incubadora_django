from supabase import create_client

SUPABASE_URL = "https://qpuvmkpgdcsahewfuqre.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFwdXZta3BnZGNzYWhld2Z1cXJlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc4MjY0NzYsImV4cCI6MjA5MzQwMjQ3Nn0.U0SQh1xIWh9IV6Bk3jVFr3V-AraEZG8rg40niwi-3cY"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)