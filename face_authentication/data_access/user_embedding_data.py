from face_authentication.config.database import MongodbClient
from face_authentication.constants.database_constants import EMBEDDING_COLLECTION_NAME
from face_authentication.entity.user_embedding import Embedding


class UserEmbeddingData:
    def __init__(self) -> None:
        self.client = MongodbClient()
        self.collection_name = EMBEDDING_COLLECTION_NAME
        self.collection = self.client.database[self.collection_name]

    def save_user_embedding(self, embed:Embedding) -> None:
        embed_dict = embed.to_dict()
        self.collection.insert_one(embed_dict)

    def get_user_embedding(self, uuid_: str) -> dict:
        user: dict = self.collection.find_one({"UUID": uuid_})
        if user != None:
            return user
        else:
            return None
