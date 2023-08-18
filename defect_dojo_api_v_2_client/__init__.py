""" A client library for accessing Defect Dojo API v2 """
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
