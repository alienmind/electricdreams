from typing import Optional

import requests
from schema import ChatGetQueryQuery, HTTPValidationError

BASE_URL = "http://localhost:8000"


def chat_get_query(
    *,
    params: ChatGetQueryQuery,
    headers: Optional[dict] = None,
    proxies: Optional[dict] = None,
    **kwargs,
) -> Optional[HTTPValidationError]:
    headers_ = headers if headers is not None else {}
    proxies_ = proxies if proxies is not None else {}

    response_obj = requests.get(
        url=f"{BASE_URL}/query/",
        params=params.dict(exclude_unset=True),
        headers=headers_,
        proxies=proxies_,
        **kwargs,
    )

    if not response_obj.ok:
        return HTTPValidationError(**response_obj.json())
    return None
