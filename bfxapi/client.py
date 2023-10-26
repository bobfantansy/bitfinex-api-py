from typing import \
    TYPE_CHECKING, List, Optional

from bfxapi._utils.logging import ColorLogger

from bfxapi._exceptions import IncompleteCredentialError

from bfxapi.rest import BfxRestInterface
from bfxapi.websocket import BfxWebSocketClient
from bfxapi.urls import REST_HOST, WSS_HOST

if TYPE_CHECKING:
    from bfxapi.websocket._client.bfx_websocket_client import \
        _Credentials

class Client:
    def __init__(
            self,
            api_key: Optional[str] = None,
            api_secret: Optional[str] = None,
            *,
            rest_host: str = REST_HOST,
            wss_host: str = WSS_HOST,
            filters: Optional[List[str]] = None,
            timeout: Optional[int] = 60 * 15,
            log_filename: Optional[str] = None
    ) -> None:
        credentials: Optional["_Credentials"] = None

        if api_key and api_secret:
            credentials = \
                { "api_key": api_key, "api_secret": api_secret, "filters": filters }
        elif api_key:
            raise IncompleteCredentialError( \
                "You must provide both an API-KEY and an API-SECRET (missing API-KEY).")
        elif api_secret:
            raise IncompleteCredentialError( \
                "You must provide both an API-KEY and an API-SECRET (missing API-SECRET).")

        self.rest = BfxRestInterface(rest_host, api_key, api_secret)

        logger = ColorLogger("bfxapi", level="INFO")

        if log_filename:
            logger.register(filename=log_filename)

        self.wss = BfxWebSocketClient(wss_host, \
            credentials=credentials, timeout=timeout, logger=logger)
