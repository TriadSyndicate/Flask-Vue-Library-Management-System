import hashlib
import datetime
import re
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_cors import CORS
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
#Allow cross origin requests
cors = CORS(app)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'jfwrscasewe233'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=2)

client = MongoClient(os.getenv('DB_URI')) # your connection string
db = client["M-Buku"]

#Collections
# Members = [booksBorrowed, flag(active, closed), dateJoined]
# Transactions = [memberId, Type, Fee, timestamp, status(confirmed,pending), bookId, dueDate]
users_collection = db["users"]
books_collection = db["books"]
members_collection = db["members"]
transactions_collection = db["transactions"]

@app.route("/api/v1/users", methods=["POST"])
def register():
	new_user = request.get_json() # store the json body request
	new_user["password"] = hashlib.sha256(new_user["password"].encode("utf-8")).hexdigest() # encrpt password
	doc = users_collection.find_one({"username": new_user["username"]}) # check if user exist
	if not doc:
		users_collection.insert_one(new_user)
		return jsonify({'msg': 'User created successfully'}), 201
	else:
		return jsonify({'msg': 'Username already exists'}), 409

@app.route("/api/v1/login", methods=["POST"])
def login():
	login_details = request.get_json() # store the json body request
	user_from_db = users_collection.find_one({'username': login_details['username']})  # search for user in database

	if user_from_db:
		encrpted_password = hashlib.sha256(login_details['password'].encode("utf-8")).hexdigest()
		if encrpted_password == user_from_db['password']:
			access_token = create_access_token(identity=user_from_db['username']) # create jwt token
			return jsonify(access_token=access_token), 200

	return jsonify({'msg': 'The username or password is incorrect'}), 401

@app.route("/api/v1/user", methods=["GET"])
@jwt_required
def profile():
	current_user = get_jwt_identity() # Get the identity of the current user
	user_from_db = users_collection.find_one({'username' : current_user})
	if user_from_db:
		del user_from_db['_id'], user_from_db['password'] # delete data we don't want to return
		return jsonify({'profile' : user_from_db }), 200
	else:
		return jsonify({'msg': 'Profile not found'}), 404


# Books Routes & CRUD Operations
#TODO: Add JWT authentication to all routes, add search by title array

@app.route("/api/v1/books", methods=["POST"])
def add_book():
	new_book = request.get_json()
	doc = books_collection.find_one({"title": new_book["title"]}) # check if book exist
	if not doc:
		books_collection.insert_one(new_book)
		return jsonify({'msg': 'Book added successfully'}), 201
	else:
		return jsonify({'msg': 'Book already exists'}), 409

# Get all books
@app.route("/api/v1/books", methods=["GET"])
def get_books():
	books = []
	for book in books_collection.find():
		book['_id'] = str(book['_id'])
		books.append(book)
	return jsonify({'books': books}), 200

# Get a single book by title
@app.route("/api/v1/books/<title>", methods=["GET"])
def get_book(title):
	book = books_collection.find_one({'title': title})
	print(id)
	print(book)
	if book:
		book['_id'] = str(book['_id'])
		return jsonify({'book': book}), 200
	else:
		return jsonify({'msg': 'Book not found'}), 404

# Update a book by id
@app.route("/api/v1/books/<id>", methods=["PUT"])
def update_book(id):
	updated_book = request.get_json()
	book_id = ObjectId(id)
	book = books_collection.find_one({'_id': book_id})
	if book:
		books_collection.update_one({'_id': book_id}, {'$set': updated_book})
		return jsonify({'msg': 'Book updated successfully'}), 200
	else:
		return jsonify({'msg': 'Book not found'}), 404

# Delete a book by id
@app.route("/api/v1/books/<id>", methods=["DELETE"])
def delete_book(id):
    book_id = ObjectId(id)
    result = books_collection.delete_one({'_id': book_id})
    print(result.raw_result)
    if result.deleted_count == 1:
        return jsonify({'msg': 'Book deleted successfully'}), 200
    else:
        return jsonify({'msg': 'Book not found'}), 404
    
# Find Book By Id
@app.route("/api/v1/books/id/<id>", methods=["GET"])
def get_book_byId():
	book_id = ObjectId(id)
	book = books_collection.find_one({'_id': book_id})
	if book:
		book['_id'] = str(book['_id'])
		return jsonify({'book': book}), 200
	else:
		return jsonify({'msg': 'Book not found'}), 404

# Search for books with similar title or author
@app.route("/api/v1/books/search/<search_term>", methods=["GET"])
def search_books(search_term):
	books = []
	query = {
		"$or": [
			{"title": {"$regex": re.compile(search_term, re.IGNORECASE)}},
			{"author": {"$regex": re.compile(search_term, re.IGNORECASE)}}
		]
	}
	for book in books_collection.find(query):
		book['_id'] = str(book['_id'])
		books.append(book)
	return jsonify({'books': books}), 200


#<----------------------Members Routes & CRUD Operations---------------------->

# Add a member
@app.route("/api/v1/members", methods=["POST"])
def add_member():
	new_member = request.get_json()
	query ={"$or": [{"name": new_member["name"], "email": new_member["email"], "phone": new_member["phone"]}]}
	doc = members_collection.find_one(query) # check if member exist   
	print(doc)
	if not doc:
		members_collection.insert_one(new_member)
		return jsonify({'msg': 'Member added successfully'}), 201
	else:
		return jsonify({'msg': 'Member already exists'}), 200    

# Get all members
@app.route("/api/v1/members", methods=["GET"])
def get_members():
	members = []
	for member in members_collection.find():
		member['_id'] = str(member['_id'])
		members.append(member)
	return jsonify({'members': members}), 200

# Search for members with similar name, email or phone
@app.route("/api/v1/members/search/<search_term>", methods=["GET"])
def search_members(search_term):
	members = []
	query = {
		"$or": [
			{"name": {"$regex": re.compile(search_term, re.IGNORECASE)}},
			{"email": {"$regex": re.compile(search_term, re.IGNORECASE)}},
			{"phone": {"$regex": re.compile(search_term, re.IGNORECASE)}}
		]
	}
	for member in members_collection.find(query):
		member['_id'] = str(member['_id'])
		members.append(member)
	return jsonify({'members': members}), 200

#Find Member By Id
@app.route("/api/v1/members/id/<id>", methods=["GET"])
def get_member_byId():
	member_id = ObjectId(id)
	member = members_collection.find_one({'_id': member_id})
	if member:
		member['_id'] = str(member['_id'])
		return jsonify({'member': member}), 200
	else:
		return jsonify({'msg': 'Member not found'}), 404

# Update a member by id
@app.route("/api/v1/members/<id>", methods=["PUT"])
def update_memberById(id):
    updated_member = request.get_json()
    member_id = ObjectId(id)
    member = members_collection.find_one({'_id': member_id})
    if member:
        members_collection.update_one({'_id': member_id}, {'$set': updated_member})
        return jsonify({'msg': 'Member updated successfully'}), 200
    else:
        return jsonify({'msg': 'Member not found'}), 404

# Delete a member by id
@app.route("/api/v1/members/<id>", methods=["DELETE"])
def delete_member(id):
	member_id = ObjectId(id)
	result = members_collection.delete_one({'_id': member_id})
	print(result.raw_result)
	if result.deleted_count == 1:
		return jsonify({'msg': 'Member deleted successfully'}), 200
	else:
		return jsonify({'msg': 'Member not found'}), 404

#<----------------------Transactions Routes {Borrow, Returns, Registration, Late Fees, Closing} & CRUD Operations---------------------->
# Add a transaction
@app.route("/api/v1/transactions", methods=["POST"])
def add_transaction():
	new_transaction = request.get_json()
	transactions_collection.insert_one(new_transaction)
	return jsonify({'msg': 'Transaction added successfully'}), 201

# Get all transactions
@app.route("/api/v1/transactions", methods=["GET"])
def get_transactions():
	transactions = []
	for transaction in transactions_collection.find():
		transaction['_id'] = str(transaction['_id'])
		transactions.append(transaction)
	return jsonify({'transactions': transactions}), 200


if __name__ == '__main__':
	app.run(threaded=True, port=5000, debug=False)
	
 