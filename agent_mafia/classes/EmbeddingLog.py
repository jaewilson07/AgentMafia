"""Default description (change me)"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/classes/EmbeddingLog.ipynb.

# %% auto 0
__all__ = ['EmbeddingLog_Error', 'EmbeddingLog']

# %% ../../nbs/classes/EmbeddingLog.ipynb 2
import datetime as dt
from dataclasses import dataclass, field
import json
import os
from typing import List, Dict


import agent_mafia.utils as utils
from agent_mafia.client.MafiaError import MafiaError

# %% ../../nbs/classes/EmbeddingLog.ipynb 4
class EmbeddingLog_Error(MafiaError):
    def __init__(self, message, exception  = None):
        super().__init__(message=message, exception=exception)

# %% ../../nbs/classes/EmbeddingLog.ipynb 5
@dataclass
class EmbeddingLog:
    log_path: str

    data: Dict[str, List[float]] = field(default_factory=dict)

    def __post_init__(self):
        if not os.path.exists(self.log_path):
            utils.upsert_folder(self.log_path)

        self.get()

    def update_file(self):
        data = self.data or {}
        with open(self.log_path, mode="w+", encoding="utf-8") as f:
            json.dump(data, f)

        return True

    @classmethod
    def init(
        cls, log_folder: str = "./QUESTION_EMBEDDINGS", is_reset_log: bool = False
    ) -> str:  # log_path

        log_path = f"{log_folder}/{dt.date.today()}.json"

        log = cls(log_path=log_path)

        if is_reset_log:
            log.update_file()

        return log

    def get(self):
        with open(self.log_path, mode="r+", encoding="utf-8") as f:
            try:
                self.data = json.load(f)

            except json.decoder.JSONDecodeError:
                self.update_file()

        return self.data

    def get_query_embedding(
        self, user_query
    ) -> List[
        float
    ]:  # returns entire log as dict or retrieves the embedding for a query  :

        self.get()

        return self.data.get(user_query, None)

    def update_query_embedding(self, user_query, embedding):

        if not isinstance(embedding, list) or not (
            isinstance(embedding[0], float) or isinstance(embedding[0], int)
        ):
            raise EmbeddingLog_Error(message="invalid embedding - pass a List[float]")

        self.data.update({user_query: embedding})

        self.update_file()
