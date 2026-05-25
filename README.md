
# how to generate type for python supabase
npx supabase gen types --lang=python --db-url "postgresql://postgres.kxmmzqkuugdgyrxsubud:[DB_PASSWORD]@aws-1-ap-southeast-2.pooler.supabase.com:5432/postgres" --schema public > model/supabase_model.py

# Deployment
PART 1: Ok
* chmod stands for change mode — it controls who can read/write/execute a file on Linux/Mac.
    * The 400 means:
        * 4 = owner can read
        * 0 = group cannot do anything
        * 0 = others cannot do anything

* -i stands for identity file — it tells SSH which private key file to use to authenticate

PART 2: Ok

* How to exit nano
    * Ctrl + X to exit
    * Y to confirm save
    * Enter to confirm the filename