from antarest_client.core import ApiClient
from antarest_client.study import Study


class StudyManager:
    def __init__(self, api_client: ApiClient) -> None:
        self.client = api_client

    def get_studies(self):
        return self.client.call_url(lambda: self.client.session.get(f"{self.client.url}/v1/studies"))

    def get_study(self, study_id: str) -> Study:
        res = self.client.call_url(lambda: self.client.session.get(f"{self.client.url}/v1/studies/{study_id}"))
        return Study(self.client, study_id, res)
