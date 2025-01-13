from neo4j import GraphDatabase

driver = GraphDatabase.driver('bolt://127.0.0.1:7687', auth=('neo4j', 'password'))

def clear_db(tx):
    tx.run('MATCH (n) DETACH DELETE n')

def add_friend(tx, name, friend_name=None):
    if not friend_name:
        return tx.run('CREATE (p:Person {name: $name}) RETURN p', name=name)
    return tx.run('MATCH (p:Person {name: $name}) '
                  'CREATE (p)-[:FRIEND]->(:Person {name: $friend_name})',
                  name=name, friend_name=friend_name)

def print_friend(tx, name):
    for record in tx.run('MATCH (p {name: $name})-[:FRIEND]->(yourFriends) '
                         'RETURN p,yourFriends', name=name):
        print(record)

with driver.session() as session:
    session.execute_write(clear_db)
    session.execute_write(add_friend, 'Arata')
    for f in ['Mike', 'Nancy']:
        session.execute_write(add_friend, 'Arata', f)
    session.execute_read(print_friend, 'Arata')