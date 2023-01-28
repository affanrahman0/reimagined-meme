# A Huffman Tree Node
import heapq
import sys

dict1 = {}
charFreq = {}

inputfile = sys.argv[1]
ext = inputfile.split('.')

outputfile = ext[0] + "-encrypted.huf"


print(outputfile)


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




   





# fetching characters and storing its corresponding frequencies in adictionary
file = open(inputfile, 'r')


ext = inputfile.split('.')
extension = ext[1]


while 1:

    # read by character
    char = file.read(1)
    if not char:
        break
    if char in charFreq:
        charFreq[char] += 1

    else:
        charFreq[char] = 1

file.close()


keyfilename = "downloads/key.txt"
print(keyfilename)

print("Key added")

file1 = open(keyfilename, "a+")  # append mode
file1.write(extension + '\n')
for x in charFreq:
    m = str(x) +" "+ str(charFreq[x])
    m+='\n'
    file1.write(m)
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


print("Huffman Tree is ready")

a = ""
file = open(inputfile, 'r')


#creating binary string corresponding to the characters of the input file
while 1:

    # read by character
    char = file.read(1)
    if not char:
        break

    if char in dict1:
        a+= dict1[char]

    else:
        print("error")

file.close()



# print(a)

special = a




def decimalToBinary(n):
    return bin(n).replace("0b","")

def binaryToDecimal(n):
    return int(n,2)



# converting the binary to char(considering each set of 8 bits and converting them to char)

i=8
scode = ""
while(i < len(a) + 8):
    # print(lis[i], end = " ")
    sstr = binaryToDecimal(a[i-8:i])
    ch1 = chr(sstr) 
    scode+= ch1
    i += 8

print("Storing File")

# output1 = scode
#storing the compressed string into a binary file

c = 0 
c = len(special) % 8

str1 = (str(c) + scode).encode(encoding='utf8')    

f=open(outputfile,"wb")
f.write(str1)
f.close()





# Decoding 
# Reading the compressed string

# f=open("binfile.bin","rb")
# data= f.read()
# f.close()

# data = data.decode('utf8','strict') 
# cf= int(data[:1])
# data = data[1:]




# # Conversion to binary string
# re= ""  

# for i in data:
#     a1 = ord(i)
#     app = decimalToBinary(a1)
#     temp = ""
#     if(len(app)<8):
#         for j in range(0,8-len(app)):
#             temp += '0' 

#     temp += app        
#     re  += temp


# x = ""
# if(cf>0):
#     x= re[len(re)-8:]
#     re = re[0:len(re)-8]
#     re+= x[8-cf:8]







# # Decoding into the original text

# ans= ""
# def decode(node,ans=""):
#     cur = node
#     if( not cur) : return
#     for i in re:
#         # print(i)
#         if(not cur.left and not cur.right):
#             ans+= cur.symbol
#             # print(cur.symbol)
#             cur = node


#         if(i=='0') :
#             cur = cur.left
#         elif(i=='1') :
#             cur = cur.right  

#         else : print("error")  
#     # print(cur.symbol)
#     ans+= cur.symbol 
#     return ans     


# ans = decode(nodes[0])

# # print(ans)

# with open("output.py", "w", encoding="utf-8") as f:
#     f.write(ans)
# f.close  

# # count =0
# # for i in scode:
# #     if(i=='\n') : count+=1

# # print(count)


# # print(scode)
# # print("kkkk")
# # print(data)


# # print(re)
# # print("kkkk")
# # print()







# # for element in range(0, len(re)):
# #     if(re[element]!=special[element]):
# #         print(element," error")


# # for element in range(0, max(len(scode),len(data))):
# #     if(scode[element]!=data[element]):
#         # print(element," fatalerror")
#         # print(scode[element])
#         # print(data[element])


# # print(len(scode))
# # print(len(data))        