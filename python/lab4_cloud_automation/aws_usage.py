import boto3
ce = boto3.client("ce")
response = ce.get_cost_and_usage(
    TimePeriod={"Start":"2024-07-01","End":"2024-07-20"},
    Granularity="DAILY",
    Metrics=["UnblendedCost"])
print(response)