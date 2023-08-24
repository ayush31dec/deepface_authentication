from face_authentication.config.database import MongodbClient
import pandas as pd, numpy as np
from face_authentication.entity.user import User
from face_authentication.data_access.user_data import UserData
from face_authentication.data_access.user_embedding_data import UserEmbeddingData
from face_authentication.entity.user_embedding import Embedding

def main():
    Name = "Ayush"
    username = "hsiuahduio"
    password = "hjshdaghjkdha"
    password2 = "hjshdaghjkdha"
    email_id = 'aysuiaghs'
    ph_no = "275w382563"
    user_data1 = User(
Name,
username,
email_id,
ph_no,
password,
password2
)
    
    ud = UserData()
    ud.save_user(user_data1)

    embed_list = list(np.zeros([128, ]))
    uuid = "jhksagdjaisghdiuahsdio"
    embed = Embedding(uuid, embed_list)
    UserEmbeddingData().save_user_embedding(embed)


if __name__ == '__main__':
    main()