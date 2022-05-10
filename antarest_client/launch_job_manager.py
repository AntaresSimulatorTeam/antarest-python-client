from antarest_client.core import ApiClient
from antarest_client.study import Study


class LaunchJobManager:
    def __init__(self, api_client: ApiClient) -> None:
        self.client = api_client

    def get_jobs(self):
        return self.client.call_url(lambda: self.client.session.get(f"{self.client.url}/v1/launcher/jobs"))

    def get_job_info(self, job_id: str) -> Study:
        return self.client.call_url(lambda: self.client.session.get(f"{self.client.url}/v1/launcher/jobs/{job_id}"))

    def cancel_job(self, job_id: str) -> bool:
        return self.client.call_url(lambda: self.client.session.post(f"{self.client.url}/v1/launcher/jobs/{job_id}/kill"))