from pymongo import MongoClient
from datetime import datetime, timedelta
import logging 

logging.basicConfig(level=logging.DEBUG)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create or access the 'ramble' database
db = client['ramble']

# Create or access the 'user_messages' collection
collection = db['user_messages']

def insert_user_message(user_id, date, messages):
    """
    Inserts a user message into the user_messages collection.
    """
    document = {
        "user_id": user_id,
        "date": date,
        "messages": messages
    }
    try:
        collection.insert_one(document)
        logging.info("Message inserted successfully")
    except Exception as e:
        logging.error("Error inserting message:", e)

def get_messages_by_user(user_id):
    """
    Retrieves all messages for a given user.
    """
    return list(collection.find({"user_id": user_id}))

def get_messages_by_user_and_date(user_id, date):
    """
    Retrieves messages for a given user on a specific date.
    """
    return list(collection.find({"user_id": user_id, "date": date}))

def get_messages_by_date_range(start_date, end_date):
    """
    Retrieves messages within a given date range.
    """
    return list(collection.find({"date": {"$gte": start_date, "$lte": end_date}}))

def get_messages_in_last_7_days():
    """
    Retrieves messages from the last 7 days.
    """
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=7)
    return get_messages_by_date_range(start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))

# Example Usage
if __name__ == "__main__":
    # Insert a sample message
    insert_user_message("user123", "2024-05-23", ["Hello World!", "Another message"])

    # Fetch messages by user
    user_messages = get_messages_by_user("user123")
    print("Messages by user:", user_messages)

    # Fetch messages by user and date
    user_date_messages = get_messages_by_user_and_date("user123", "2024-05-23")
    print("Messages by user and date:", user_date_messages)

    # Fetch messages in the last 7 days
    recent_messages = get_messages_in_last_7_days()
    print("Messages in the last 7 days:", recent_messages)
