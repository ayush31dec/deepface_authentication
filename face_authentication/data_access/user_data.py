from face_authentication.config.database import MongodbClient
from face_authentication.constants.database_constants import USER_COLLECTION_NAME
from face_authentication.entity.user import User


class UserData:
    """This class will have all the mongo db operations for user data
    like get_user and save_user
    """

    def __init__(self) -> None:
        self.client = MongodbClient()
        self.collection_name = USER_COLLECTION_NAME
        self.collection = self.client.database[self.collection_name]
        self.keys = ["Name","username","email_id","ph_no","password"]

    def save_user(self, user: User) -> None:
        
        self.user = user
        user_data = self.user.to_dict()

        #Fetch only useful keys
        value_list = [value for key, value in  user_data.items() if key in self.keys] 
        user_dict = dict(zip(self.keys,value_list))
        user_dict["UUID"]=user_data["uuid_"]

        #Save Dictionary to Database
        self.collection.insert_one(user_dict)

    def get_user(self, query: dict):
        user = self.collection.find_one(query)
        return user
