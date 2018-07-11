import time
import hashlib

class Transaction:
    def __init__(self, fromAdd, toAdd, amount):
        self.fromAdd = fromAdd
        self.toAdd = toAdd
        self.amount = amount


class Block:
    def __init__(self, transaction, date, previousHash=""):
        self.transaction = transaction
        self.date = date
        self.previousHash = previousHash
        self.val = 0
        self.hash = self.calculateHash()
        self.difficulty = 8

    def calculateHash(self):
        string = str(self.transaction[0].fromAdd) + str(self.transaction[0].toAdd) + str(self.transaction[0].amount) + str(self.date) + str(self.val)
        hash_ = hashlib.sha256(string.encode()).hexdigest()
        return hash_
        
        

    def mineBlock(self):
        while True:
            self.val = self.val + 1
            a = str(self.transaction[0].fromAdd) + str(self.transaction[0].toAdd) + str(self.transaction[0].amount) + str(self.date) + str(self.val)
            hash_curr = hashlib.sha256(a.encode()).hexdigest()
            #print(hash_curr[:self.difficulty])
            if( hash_curr[:self.difficulty] == str(0)*self.difficulty ):
                self.hash = hash_curr
                break
            
            
            


class Blockchain:
    def __init__(self):
        self.chain = [Block([Transaction("", "system", 21000000)], time.time())]
        self.pendingTransaction = []
        self.users = []

    def minepending(self):
        minerAdd = input("Enter your name: ")
        print('What is 1+1 ')
        k = int(input())
        if k == 2:
            print(len(self.pendingTransaction))
            block = Block(self.pendingTransaction, time.time(), str(self.chain[len(self.chain) - 1].hash))
            block.mineBlock()
            self.chain.append(block)

            self.pendingTransaction = [Transaction("system", minerAdd, 12.5)]
            print("Wait Until someone mines ur transaction")
            self.users.append(minerAdd)

        else:
            print("Dont enter next time")

    def createTransaction(self, transaction):
        balance = self.getbalance(transaction.fromAdd)

        if (balance >= transaction.amount):
            self.pendingTransaction.append(transaction)
            self.users.append(transaction.fromAdd)
            self.users.append(transaction.toAdd)

        else:
            print("No Balance")

    def check(self):
        for i in range(0, len(self.chain) + 1):

            if(self.chain[i].hash != self.chain[i].calculateHash()):
                print("cal")
                return False
            
            if (self.chain[i-1].hash != self.chain[i].previousHash):
                print("prev")
                return False

            else:
                return True

    def getbalance(self, add):
        balance = 0

        for i in self.chain:
            for j in i.transaction:
                if (add == j.fromAdd):
                    balance = balance - j.amount

                if (add == j.toAdd):
                    balance = balance + j.amount
        
        return balance

    def getUsers(self):
        print(self.users)



coin = Blockchain()

coin.check()
