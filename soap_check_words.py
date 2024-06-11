from zeep import Client, Settings
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)
wsdl = data['wsdl']
settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)


def check_text(text):
    response = client.service.checkText(text)
    print(response[0]['s'])
    return response[0]['s']
