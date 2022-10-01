import requests
from datetime import datetime, timedelta
import math


class LoaderQuestions:
    URL = 'https://api.stackexchange.com/questions'

    def _get_url_questions(self) -> str:
        from_date = math.ceil(datetime.timestamp(datetime.today() - timedelta(days=2)))
        to_date = math.ceil(datetime.timestamp(datetime.today()))

        params = {
            'tagged': 'python',
            'fromdate': f'{from_date}',
            'todate': f'{to_date}',
            'site': 'stackoverflow',
            'pagesize': 100,
        }

        response = requests.get(self.URL, params=params)

        return response.url

    def get_questions(self) -> list:
        url_link = self._get_url_questions()
        response = requests.get(url_link)
        data_response = response.json()
        questions = [data['title'] for data in data_response['items']]

        return questions


if __name__ == '__main__':
    loader = LoaderQuestions()
    questions = loader.get_questions()

    for question in questions:
        print(question)
