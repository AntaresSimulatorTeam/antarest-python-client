from typing import Any, Dict, Optional

from antarest_client.core import ApiClient


class Study:
    def __init__(self, api_client: ApiClient, study_id: str, study_data: Optional[Dict[str, Any]] = None) -> None:
        self.client = api_client
        self.study_id = study_id
        self.study_data = study_data

    def get_synthesis(self):
        return self.client.call_url(
            lambda: self.client.session.get(f"{self.client.url}/v1/studies/{self.study_id}/synthesis"))

    def run(self):
        return self.client.call_url(
            lambda: self.client.session.post(f"{self.client.url}/v1/launcher/run/{self.study_id}"))


