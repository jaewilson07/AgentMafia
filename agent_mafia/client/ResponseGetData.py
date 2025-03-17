# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/client/ResponseGetData.ipynb.

# %% auto 0
__all__ = ['ResponseGetData', 'ResponseGetDataSlack']

# %% ../../nbs/client/ResponseGetData.ipynb 1
from typing import Any
from dataclasses import dataclass, field
from abc import abstractmethod

from slack_bolt.async_app import AsyncApp as AsyncSlackApp
from slack_sdk.web.async_client import AsyncSlackResponse

# %% ../../nbs/client/ResponseGetData.ipynb 3
@dataclass
class ResponseGetData:
    is_success: bool
    status : int
    response : Any

    @abstractmethod
    def from_res():
        pass




# %% ../../nbs/client/ResponseGetData.ipynb 4
@dataclass
class ResponseGetDataSlack(ResponseGetData):
    is_success: bool
    status : int
    response : Any

    channel_id : str = None
    message_id : float = None
    app : AsyncSlackApp = field(repr = False , default = None)

    @classmethod
    def from_res(cls, res : AsyncSlackResponse, async_app :AsyncSlackApp, **kwargs):
        return ResponseGetDataSlack(
            is_success=res["ok"],
            response=res.data,
            status = res.status_code,
            app = async_app,
            **kwargs
        )
