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
import json
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
	insert_book = {
		'title': new_book['title'],
		'author': new_book['author'],
		'genre':new_book['genre'],
		'year':new_book['year'],
		'stats':{
			'quantity': new_book['quantity'],
			'borrowed':[]
		}
	}
	doc = books_collection.find_one({"title": new_book["title"]}) # check if book exist
	if not doc:
		books_collection.insert_one(insert_book)
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
		newM = {
			'email': new_member['email'],
			'name': new_member['name'],
			'phone': new_member['phone'],
			'status':'ACTIVE',
			'book_stats':{
				'books_borrowed':[],
				'penalties':[]
			}
		}
		newMember = members_collection.insert_one(newM)
        #Add Transaction 'account_creation' + 500 FEE
		transaction_account_creation = {
			'member_id':str(newMember.inserted_id),
			'type':'account_creation',
			'status':'RESOLVED',
			'fee':500,
			'timestamp_created':datetime.datetime.now(),
		}
		new_transaction = transactions_collection.insert_one(transaction_account_creation)
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




# Borrowing a book operation
@app.route("/api/v1/book/borrow", methods=["POST"])
def borrow_book():
    borrow_details = request.get_json()
    # check if book is available
    book_id = ObjectId(borrow_details['book_id'])
    select_book = books_collection.find_one({'_id': book_id})
    if(select_book['stats']['quantity'] > 0):
        # book is available, change book quantity, update member, create transaction_borrow
        #TODO:check if penalties or balance < -500
        
        # Add borrow transaction
        transaction_borrow = {
            'member_id':borrow_details['member_id'],
            'book_id':borrow_details['book_id'],
            'type':'borrow',
			'borrow':{
				'duration': borrow_details['duration'],
				'due_date': datetime.datetime.strptime(borrow_details['due_date'],"%a %b %d %Y %H:%M:%S")
			},
			'status':'PENDING',
			'timestamp_created': datetime.datetime.now(),
		}
        new_transaction = transactions_collection.insert_one(transaction_borrow)
        # change book quantity, update transaction id
        new_quantity = select_book['stats']['quantity'] - 1
        new_borrowed = select_book['stats']['borrowed']
        new_borrowed.append({
			'transaction_id': str(new_transaction.inserted_id),
			'member_id': borrow_details['member_id'],
			'status': 'PENDING',
			'return_transaction_id':''
		})
        book_update = {
			'stats.quantity':new_quantity,
			'stats.borrowed': new_borrowed
		}
        books_collection.update_one({'_id': book_id}, {'$set': book_update})
        
        # Update Member
        member_id = ObjectId(borrow_details['member_id'])
        select_member = members_collection.find_one({'_id': member_id})
        new_member_borrowed = select_member['book_stats']['books_borrowed']
        new_member_borrowed.append({
			'transaction_id': str(new_transaction.inserted_id),
			'status':'PENDING'
		})
        member_update = {
			'book_stats.books_borrowed':new_member_borrowed
		}
        members_collection.update_one({'_id': member_id},{'$set':member_update})
        return jsonify({'msg':'Success'}), 200
    #book_id, member_id, duration
    # member = {user_data, book_stats:{
        # books_borrowed:[{transaction_id:1, status:'resolved | pending', return_transaction_id:5}],
        # current_balance:0,
        # penalties:[
		# 	{
		# 		transaction_id: 1,
		# 		type:'late, worn, lost'
		# 	}
		# ]
	# }}
	
	# book = {book_details, stats:{quantity:0, borrowed:[{transaction_id:2, member_id:3, status:'returned, pending, lost', return_transaction_id:67}]}}
 
	# transaction_borrow = {id, borrow_duration ,type:'borrow, account_creation, return, return_late, return_lost, return_worn, account_closure', status:'pending | resolved', fee:500, timestamp_created:tt, timestamp_resolved}
 
 # Returning a book operation
 
@app.route("/api/v1/book/return", methods=["POST"])
@app.route("/api/v1/book/return", methods=["POST"])
def return_book():
    return_details = request.get_json()
    # book_id, member_id, borrow_transaction_id, return_type
    # Return types: late, worn, lost, normal
    # check for book condition
    # if (return_details['return_type'] == 'late' or return_details['return_type'] == 'return_worn' or
    # return_details['return_type'] == 'return_lost' or return_details['return_type'] == 'return_normal'):
    book_id = ObjectId(return_details['book_id'])
    member_id = ObjectId(return_details['member_id'])
    transaction_late = {
        'member_id': return_details['member_id'],
        'book_id': return_details['book_id'],
        'type': return_details['return_type'],
        return_details['return_type']: {'fee': return_details['fee'], 'transaction_id': return_details['borrow_transaction_id']},
        'status': 'PENDING',
        'timestamp_created': datetime.datetime.now(),
    }
    new_transaction = transactions_collection.insert_one(transaction_late)
    select_book = books_collection.find_one({'_id': book_id})
    select_member = members_collection.find_one({'_id': member_id})

    # Update book document - quantity - borrowed with return transaction id if returned: normal or late or worn
    if return_details['return_type'] != 'return_lost':
        new_quantity = select_book['stats']['quantity'] + 1
        old_borrowed = select_book['stats']['borrowed']
        for item in old_borrowed:
            if item['transaction_id'] == return_details['borrow_transaction_id']:
                item['status'] = 'RETURNED'
                item['return_transaction_id'] = str(new_transaction.inserted_id)
                break
        book_update = {
            'stats.quantity': new_quantity,
            'stats.borrowed': old_borrowed
        }
        books_collection.update_one({'_id': book_id}, {'$set': book_update})
        # update member document book_stats.books_borrowed
        if return_details["return_type"] != "return_normal":
            member_borrowed_arr = select_member["book_stats"]["books_borrowed"]
            member_penalties_arr = select_member["book_stats"].get("penalties", [])  # Use get() to handle missing field
            for item in member_borrowed_arr:
                if item["transaction_id"] == return_details["borrow_transaction_id"]:
                    item["return_transaction_id"] = str(new_transaction.inserted_id)
                    break
            member_penalties_arr.append({"transaction_id": str(new_transaction.inserted_id), "type": return_details["return_type"]})
            member_update = {
                "book_stats.books_borrowed": member_borrowed_arr,
                "book_stats.penalties": member_penalties_arr,
            }
            members_collection.update_one({"_id": member_id}, {"$set": member_update})
            return jsonify({"msg": "Penalties Registered"}), 200
        else:
            member_borrowed_arr = select_member["book_stats"]["books_borrowed"]
            for i in member_borrowed_arr:
                if i["transaction_id"] == return_details["borrow_transaction_id"]:
                    i["return_transaction_id"] = str(new_transaction.inserted_id)
                    i["status"] = "RESOLVED"
                    break
            members_collection.update_one({"_id": member_id}, {"$set": {"book_stats.books_borrowed": member_borrowed_arr}})
            return jsonify({"msg": "Success"}), 200

    else:
        borrowed_arr = select_book['stats']['borrowed']
        for i in borrowed_arr:
            if i['transaction_id'] == return_details['borrow_transaction_id']:
                i['status'] = 'LOST'
                i['return_transaction_id'] = str(new_transaction.inserted_id)
                break
        books_collection.update_one({'_id': book_id}, {'$set': {'stats.borrowed': borrowed_arr}})
        # update member document book_stats.books_borrowed
        if return_details["return_type"] != "return_normal":
            member_borrowed_arr = select_member["book_stats"]["books_borrowed"]
            member_penalties_arr = select_member["book_stats"].get("penalties", [])  # Use get() to handle missing field
            for item in member_borrowed_arr:
                if item["transaction_id"] == return_details["borrow_transaction_id"]:
                    item["return_transaction_id"] = str(new_transaction.inserted_id)
                    break
            member_penalties_arr.append({"transaction_id": str(new_transaction.inserted_id), "type": return_details["return_type"]})
            member_update = {
                "book_stats.books_borrowed": member_borrowed_arr,
                "book_stats.penalties": member_penalties_arr,
            }
            members_collection.update_one({"_id": member_id}, {"$set": member_update})
            return jsonify({"msg": "Penalties Registered"}), 200
        else:
            member_borrowed_arr = select_member["book_stats"]["books_borrowed"]
            for i in member_borrowed_arr:
                if i["transaction_id"] == return_details["borrow_transaction_id"]:
                    i["return_transaction_id"] = str(new_transaction.inserted_id)
                    i["status"] = "RESOLVED"
                    break
            members_collection.update_one({"_id": member_id}, {"$set": {"book_stats.books_borrowed": member_borrowed_arr}})
            return jsonify({"msg": "Success"}), 200

    # Add the following return statement at the end of the function
    return jsonify({"msg": "Unknown return type"}), 400


	
        
if __name__ == '__main__':
	app.run(threaded=True, port=5000, debug=False)
	
 