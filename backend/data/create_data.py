from datetime import datetime
import random

from faker import Faker

from data.db_client import create_supabase_client

if __name__ == "__main__":

    raw_data = []
    fake = Faker()

    for _ in range(50):

        # Create start date: Assuming all start from 2010 t0 2023
        start_year = random.randint(2010, 2024)
        start_month = random.randint(1, 12)
        start_day = 28
        tenure_start = datetime(start_year, start_month, start_day).date().isoformat()

        # Create end date: Assuming all end in May 28 to December 28th this year
        end_year = 2026
        end_month = random.randint(5, 12)
        end_day = 28
        tenure_end = datetime(end_year, end_month, end_day).date().isoformat()

        # Randomize Plan tier
        plan_tier = random.randint(1, 4)

        # Create monthly usage based on plan tier in a range that is possible for
        # Upgrade, Stay or Downgrade
        match plan_tier:
            case 1:
                monthly_usage = 500 + random.random() * 500
            case 2:
                monthly_usage = 300 + random.random() * 400
            case 3:
                monthly_usage = 100 + random.random() * 400
            case 4:
                monthly_usage = 50 + random.random() * 250

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
