import json
import os
from caller import scrape_trends
from apify_client import ApifyClient

apify_token = os.environ['APIFY_TOKEN']
apify_url = os.environ['APIFY_API_BASE_URL']
apify_secret_store = os.environ['APIFY_DEFAULT_KEY_VALUE_STORE_ID']
apify_input_key = os.environ['APIFY_INPUT_KEY']
apify_database_id = os.environ['APIFY_DEFAULT_DATASET_ID']

# Run the main function of the script, if the script is executed directly
if __name__ == '__main__':
    print(f"API url: {apify_url}")
    print(f"Secret store: {apify_secret_store}")

    # Initialize the main ApifyClient instance
    client = ApifyClient(token=apify_token, api_url=apify_url, max_retries=2)

    # Get the resource subclient for working with the default key-value store of the actor
    default_kv_store_client = client.key_value_store(apify_secret_store)

    # Get the value of the actor input and print it
    print('Loading input')
    actor_input = default_kv_store_client.get_record(apify_input_key)['value']
    print(actor_input)

    keywords = actor_input["keywords"]
    timeframe = actor_input["timeframe"]
    geolocation = actor_input["geolocation"]
    category_id = actor_input["category_id"]
    interest_low_volume = actor_input["interest_low_volume"]
    interest_include_geo = actor_input["interest_include_geo"]
    interest_grouping = actor_input["interest_grouping"]
    get_related_queries = actor_input["get_related_queries"]
    get_related_topics = actor_input["get_related_topics"]
    get_interest_by_region = actor_input["get_interest_by_region"]

    result = scrape_trends(
        keywords,
        timeframe,
        geolocation,
        category_id,
        interest_low_volume,
        interest_include_geo,
        interest_grouping,
        get_related_queries,
        get_related_topics,
        get_interest_by_region
    )

    print("Data scraper, transforming")

    time_data = result[0].to_json(orient="records")
    interest_data = result[1].to_json(orient="records")
    related_queries = result[2].to_json(orient="records")
    related_topics = result[3].to_json(orient="records")

    print("Returning data")

    # Get the resource subclient for working with the default dataset of the actor
    default_dataset_client = client.dataset(apify_database_id)

    # Structure of output is defined in .actor/actor.json
    default_dataset_client.push_items([
        {
            "time_data": json.loads(time_data),
            "interest_data": json.loads(interest_data),
            "related_queries": json.loads(related_queries),
            "related_topics": json.loads(related_topics)
        },
    ])
