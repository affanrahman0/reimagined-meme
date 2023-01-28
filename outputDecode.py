import heapq

dict1 = {}
charFreq = {}


class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (character)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq


#storing symbol and it's corresponding bit representation
def printNodes(node, val=''):

    
    newVal = val + str(node.huff)

    # if node is not an edge node
    # then traverse inside it
    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)

        # if node is edge node then
        # display its huffman code
    if (not node.left and not node.right):
        #print(f"{node.symbol} -> {newVal}")
        dict1[node.symbol] = newVal


file1 = open('key.txt', 'r')
extension = (file1.readline()).strip()

extension = '.' + extension


while True:
  
    # Get next line from file
    line = file1.readline()

    if not line:
        break


    key = line[0:1]
    if(key=='\n'): 
        line = file1.readline()
        val = int(line[1:len(line)])
    else: val = int(line[2:len(line)])
    charFreq[key] = val
  
file1.close()


# pushing the nodes in a pqueue

nodes = []
for x in charFreq:
    
    heapq.heappush(nodes,node(charFreq[x],x))


#creating huffman tree
while len(nodes) > 1:

    # sort all the nodes in ascending order
    # based on their frequency
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)

    # assign directional value to these nodes
    left.huff = 0
    right.huff = 1

    # combine the 2 smallest nodes to create
    # new node as their parent
    newNode = node(left.freq + right.freq, left.symbol + right.symbol, left,
                   right)

    heapq.heappush(nodes, newNode)

# Huffman Tree is ready!
printNodes(nodes[0])


# Decoding 
# Reading the compressed string

f=open("binfile.bin","rb")
data= f.read()
f.close()

data = data.decode('utf8','strict') 
cf= int(data[:1])
data = data[1:]




def decimalToBinary(n):
    return bin(n).replace("0b","")


# Conversion to binary string
re= ""  

for i in data:
    a1 = ord(i)
    app = decimalToBinary(a1)
    temp = ""
    if(len(app)<8):
        for j in range(0,8-len(app)):
            temp += '0' 

    temp += app        
    re  += temp


x = ""
if(cf>0):
    x= re[len(re)-8:]
    re = re[0:len(re)-8]
    re+= x[8-cf:8]







# Decoding into the original text

ans= ""
def decode(node,ans=""):
    cur = node
    if( not cur) : return
    for i in re:
        # print(i)
        if(not cur.left and not cur.right):
            ans+= cur.symbol
            # print(cur.symbol)
            cur = node


        if(i=='0') :
            cur = cur.left
        elif(i=='1') :
            cur = cur.right  

        else : print("error")  
    # print(cur.symbol)
    ans+= cur.symbol 
    return ans     


ans = decode(nodes[0])

# print(ans)
outputfile = 'output'
outputfile+= extension
with open(outputfile, "w", encoding="utf-8") as f:
    f.write(ans)
f.close  