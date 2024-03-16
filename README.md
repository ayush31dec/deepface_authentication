# Face Authentication System

DeepFace Authenticator is a project aimed at implementing a facial authentication system utilizing deep learning techniques. Leveraging the power of the 'deepface' model, this system identifies faces based on cosine similarity. If a user is registered in the database, they are prompted to log in and verify their face for authentication. If not, the system guides them through the registration process, allowing them to register their face before attempting to log in again. The deepface model generates facial embeddings and performs identification using cosine similarity, ensuring robust and reliable authentication.

## Features
Facial Authentication: Utilizes deep learning techniques to authenticate users based on facial recognition.<br>
Cosine Similarity: Employs cosine similarity to compare facial embeddings for accurate identification.<br>
User Registration: Guides users through the process of registering their face for authentication.<br>
User-friendly Interface: Offers a simple and intuitive interface for seamless user interaction.<br>

## Project Archietecture
![deepAuth_flowchart](https://github.com/ayush31dec/deepface_authentication/assets/63890982/e157aeef-f345-4d5d-9156-9a78d3ea2be1)


## Getting Started
### To get started with DeepFace Authenticator, follow these steps:
### Step 1: Clone the repository
```
git clone https://github.com/yourusername/deepface-authenticator.git
```
### Step 2: Install Required libraries
```
pip install -r requirements.txt
```
### Step 3: Export MongoDB Keys, Database Name, Collection Name(Embedding and User)
```
export DATABASE_NAME=<DATABASE_NAME>
export USER_COLLECTION_NAME=<USER_COLLECTION_NAME>
export EMBEDDING_COLLECTION_NAME=<EMBEDDING_COLLECTION_NAME>
export MONGODB_URL_KEY=<MONGODB_URL_KEY>
export SECRET_KEY=klgH6AzYDeZeGwD288to79I3vTHT8wp7
export ALGORITHM=HS256
```
### Step 4: Run the application
```
python main.py 
```
