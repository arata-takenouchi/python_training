import datetime
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'date': datetime.datetime.now(datetime.UTC)
}

stack2 = {
    'name': 'customer2',
    'pip': ['python', 'java'],
    'info': {'os': 'windows'},
    'date': datetime.datetime.now(datetime.UTC)
}

db_stacks = db.stacks
# stack_id = db_stacks.insert_one(stack1).inserted_id
# print(stack_id, type(stack_id))
# print('####')
from bson.objectid import ObjectId
# str_stack_id = '6785035dc47e400254dc3bf0'
# print(db_stacks.find_one({'_id': ObjectId(str_stack_id)}))

# stack_id = db_stacks.insert_one(stack2).inserted_id
# print(stack_id, type(stack_id))
#
# for stack in db_stacks.find():
#     print(stack)

# now = datetime.datetime.now(datetime.UTC)
# for stack in db_stacks.find({'data': {'$lt': now}}):
#     print(stack)

# db_stacks.find_one_and_update(
#     {'name': 'customer1'}, {'$set': {'name': 'YYY'}}
# )
# print(db_stacks.find_one({'name': 'YYY'}))

db_stacks.delete_one({'name': 'YYY'})
print(db_stacks.find_one({'name': 'YYY'}))