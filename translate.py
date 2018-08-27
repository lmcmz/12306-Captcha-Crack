import requests,json

base_url = "https://translation.googleapis.com/language/translate/v2/"
api_key= "YOUR—GOOGLE-API-KEY"


def translate(text, source="zh", target="en"):
	params = {'key': api_key}
	data = {
		'q': text,
		'source': source,
		'target': target,
		'format': 'text'
	}
	response = requests.post(base_url, params=params, data=data)
	json_data = json.loads(response.text)
	return json_data['data']['translations'][0]['translatedText']
	

#translate('风铃 | 风铃 | 创可贴 | 创可贴 | 红枣 | 中国结 | 红豆 | 烛台 ')
