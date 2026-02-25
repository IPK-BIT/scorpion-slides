matomo = DataSource(
    name="matomo",
    plugin=Matomo(base_url="https://matomo.example.com", auth_token="your_auth_token")
)
web_stats = matomo.extract(
    config={
        'site_id': '1',
        'period': 'month',
        'date': 'lastMonth'
    }
)
results = matomo.transform(data=web_stats)
client = ScorpionClient(base_url="https://scorpion.bi.denbi.de", api_key="your_api_key")
service = client.get_service("my_tool")
yesterday = datetime.date.today() - datetime.timedelta(days=1)
form = client.prepare_indicator_form(service=service, dates=[yesterday.strftime('%Y-%m')])
for measurement in form: 
    measurement.value = results[measurement.kpi]
client.submit_measurements(
    abbreviation="my_tool",
    form=form,
)

