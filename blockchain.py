blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]



def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


add_value(5)
add_value(transaction_amount=2.505, last_transaction=get_last_blockchain_value())
print(blockchain)