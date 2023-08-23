from face_authentication.config.database import MongodbClient
import pandas as pd


def main():
    mc = MongodbClient()
    collection = mc.database["User"]
    print(collection)
    df = pd.DataFrame(list(collection.find()))
    print(df.head())
    print(df.columns)


if __name__ == '__main__':
    main()