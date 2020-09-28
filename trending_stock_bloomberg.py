class Node:
    def __init__(self, stockName):
        self.stockName = stockName
        self.freq = 1
        self.next = self.prev = None

    def removeBindings(self):
        if self.prev:
            self.prev.next = self.next

        if self.next:
            self.next.prev = self.prev

        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def addToHead(self, node):

        if self.head == None:
            self.head = node
            self.tail = node

        else:

            node.next = self.head
            self.head.prev = node
            self.head = node

        self.length += 1

    def removeNode(self, node):

        if node == self.head == self.tail:
            self.head = None
            self.tail = None

        elif node == self.head:
            self.head = node.next
            node.removeBindings()

        elif node == self.tail:

            newTail = self.tail.prev
            node.removeBindings()
            self.tail = newTail

        # node is somewhere in the middle
        # of the linked list
        else:
            node.removeBindings()

        self.length -= 1


from collections import defaultdict
class TrendingStock:

    def __init__(self):

        self.stocksWithFreq = defaultdict(DoublyLinkedList)

        self.stocks = {}
        self.maxFreq = 0

    def processStock(self, stock):

        if stock in self.stocks:

            node = self.stocks[stock]
            self.updateFreq(node, True)

        else:
            newNode = Node(stock)
            self.stocksWithFreq[1].addToHead(newNode)
            self.stocks[stock] = newNode

    def getTrendingStock(self):

        node = self.stocksWithFreq[self.maxFreq].head
        trendingStock = node.stockName

        self.updateFreq(node, False)

        return trendingStock

    # frequency of an existing node has increased or decreased
    # update self.stocksWithFreq and maxFreq if applicable
    def updateFreq(self, node, isIncreased):

        currFreq = node.freq
        # remove the node from old linked list
        self.stocksWithFreq[currFreq].removeNode(node)

        if isIncreased:

            # increase frequency
            node.freq += 1
            if node.freq > self.maxFreq:
                self.maxFreq = node.freq

            # add node to new linked list
            self.stocksWithFreq[node.freq].addToHead(node)

        else:

            node.freq -= 1

            if node.freq != 0:

                self.stocksWithFreq[node.freq].addToHead(node)

            if node.freq == 0:
                del self.stocks[node.stockName]

            if self.stocksWithFreq[self.maxFreq].length == 0:
                self.maxFreq -= 1
