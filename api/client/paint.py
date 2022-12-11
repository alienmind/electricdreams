from typing import Optional

import requests
from schema import HTTPValidationError, PaintGetGetImageQuery

BASE_URL = "http://localhost:8000"


def paint_get_get_image(
    *,
    params: PaintGetGetImageQuery,
    headers: Optional[dict] = None,
    proxies: Optional[dict] = None,
    **kwargs,
) -> Optional[HTTPValidationError]:
    headers_ = headers if headers is not None else {}
    proxies_ = proxies if proxies is not None else {}

    response_obj = requests.get(
        url=f"{BASE_URL}/image/",
        params=params.dict(exclude_unset=True),
        headers=headers_,
        proxies=proxies_,
        **kwargs,
    )

    if response_obj.ok:
        return HTTPValidationError(**response_obj.json())
    return None
