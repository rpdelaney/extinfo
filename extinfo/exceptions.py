from requests.exceptions import HTTPError


class ExtinfoError(Exception):
    pass


class ExtensionNotFoundError(ExtinfoError):
    pass


class ClientForbiddenError(ExtinfoError, HTTPError):
    pass
