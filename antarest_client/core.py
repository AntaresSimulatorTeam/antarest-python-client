from http.client import HTTPException
from typing import Optional, Callable, Any

import requests
from requests import Session, Response


class ApiClient:

    def __init__(self, url: str, token: Optional[str]) -> None:
        """

        Args:
            url: url of the antarest (antares web) instance
            token: identification token
        """
        self.url = url
        self.token = token
        self.session: Session = self._create_session()

    def _create_session(self) -> Session:
        session = Session()
        session.verify = False
        session.headers.update({'Authorization': f'Bearer {self.token}'})
        return session

    def call_url(self, call: Callable[[], Response]) -> Any:
        res = call()
        if res.status_code >= 300:
            raise HTTPException(res.status_code, res.json())
        return res.json()
