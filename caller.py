from pytrends.request import TrendReq
from pandas import DataFrame


def scrape_trends(
        keywords: str,
        timeframe: str,
        geolocation: str,
        category_id: int,
        interest_low_volume: bool,
        interest_include_geo: bool,
        interest_grouping: str,
        get_related_queries: bool,
        get_related_topics: bool,
        get_interest_by_region: bool
):

    pytrends = TrendReq(hl='en-US', tz=360,)

    # Up to 5 keywords in a list
    pytrends.build_payload(
        kw_list=keywords,
        cat=category_id,
        timeframe=timeframe,
        geo=geolocation,
        gprop=''
    )

    time_data = pytrends.interest_over_time()

    region_data = pytrends.interest_by_region(
        resolution=interest_grouping,
        inc_low_vol=interest_low_volume,
        inc_geo_code=interest_include_geo
    ) if get_interest_by_region else DataFrame()

    related_queries = pytrends.related_queries() if get_related_queries else DataFrame()
    related_topics = pytrends.related_topics() if get_related_topics else DataFrame()

    mapped_related_queries = DataFrame.from_dict(
        related_queries,
        orient='index'
    )
    mapped_related_topics = DataFrame.from_dict(
        related_topics,
        orient='index'
    )

    return time_data, region_data, mapped_related_queries, mapped_related_topics
