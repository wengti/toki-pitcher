from datetime import datetime
import random

from faker import Faker

from data.db_client import create_supabase_client

if __name__ == "__main__":

    raw_data = []
    fake = Faker()

    for _ in range(50):

        # Create start date: Assuming all start from 2010 t0 2023
        start_year = random.randint(2010, 2023)
        start_month = random.randint(1, 12)
        start_day = 28
        tenure_start = datetime(start_year, start_month, start_day).date().isoformat()

        # Create end date: Assuming all end in May 28 to December 28th this year
        end_year = 2025
        end_month = random.randint(5, 12)
        end_day = 28
        tenure_end = datetime(end_year, end_month, end_day).date().isoformat()

        # Randomize Plan tier
        plan_tier = random.randint(1, 4)

        # Monthly usage baseline is 650, 450, 250, 50 GB from tier 1 to 4
        monthly_usage_baseline = 50 + (abs(4 - plan_tier)) * 200

        # Actual monthly usage will be between (baseline to baseline + 200) GB
        monthly_usage = monthly_usage_baseline + round((random.random() * 200), 2)

        # Push to the list
        raw_data.append(
            {
                "name": fake.name(),
                "plan": f"Tier {plan_tier}",
                "tenure_start": tenure_start,
                "tenure_end": tenure_end,
                "monthly_usage": round(monthly_usage, 2),
            }
        )

    # Insert the raw data to database
    supabase = create_supabase_client()
    try:
        response = supabase.table("customers").insert(raw_data).execute()
        print(f"Operation Success.")
    except Exception as exception:
        print(f"Error: {str(exception)}")
