class HashTable:
    def __init__(self, class_size):
        self.class_size = class_size
        self.classes = {"A":[],"B":[],"C":[],"D":[]}

    def hash_code(self, score):
        if score >=90:
            return "A"
        if score >=80:
            return "B"
        if score >=70:
            return "C"
        if score >=60:
            return "D"
        else:
            return None

    def insert(self, name, score):
        classroom = self.hash_code(score)
        if classroom:
            if len(self.classes[classroom]) < self.class_size:
                self.classes[classroom].append({"name":name,"score":score})

    

students = [
    {
        "name": "Jean-Luc Garza",
        "score": 24
    },
    {
        "name": "Teddy Munoz",
        "score": 79
    },
    {
        "name": "Georgia Ali",
        "score": 17
    },
    {
        "name": "Vicky Calhoun",
        "score": 8
    },
    {
        "name": "Awais Weaver",
        "score": 65
    },
    {
        "name": "Athena Kline",
        "score": 52
    },
    {
        "name": "Zacharia Whitaker",
        "score": 38
    },
        {
        "name": "Clarice Davenport",
        "score": 99
    },
    {
        "name": "Viktoria Flynn",
        "score": 84
    },
    {
        "name": "Ianis Crossley",
        "score": 20
    },
    {
        "name": "Johnnie Owens",
        "score": 74
    },
    {
        "name": "Emily-Rose Erickson",
        "score": 33
    },
    {
        "name": "Adeel Nieves",
        "score": 100
    },
    {
        "name": "Dustin Villegas",
        "score": 98 
    },
    {
        "name": "Maxine Hughes",
        "score": 65
    },
    {
        "name": "Bilaal Harding",
        "score": 79
    },
    {
        "name": "Maddie Ventura",
        "score": 71
    },
    {
        "name": "Leroy Rees",
        "score": 44
    },
    {
        "name": "Wanda Frank",
        "score": 73
    },
    {
        "name": "Margaux Herbert",
        "score": 80
    },
    {
        "name": "Ali Rios",
        "score": 70
    },
    {
        "name": "Nigel Santiago",
        "score": 25
    },
    {
        "name": "Markus Greene",
        "score": 78
    },
    {
        "name": "Harlan Parrish",
        "score": 97
    },
    {
        "name": "Baran Davidson",
        "score": 43
    },
    {
        "name": "Seth Rodriguezh",
        "score": 67
    },
    {
        "name": "Diego Mayer",
        "score": 100
    },
]


n=int(input("What is the maximum number of students in class? "))
classes1 = HashTable(n)
for s in students:
    classes1.insert(s["name"],s["score"])
for c,students in classes1.classes.items():
    print(f"ClassRoom {c}")
    for s in students:
        print(f" {s['name']}-> {s['score']} ")
    







"""
a=0
b=0
c=0
d=0

for i in students:
    if i["age"]>60:
        if i["age"]>=90 and a<n:
            classA.insert(i["name"],i["age"])
            a=a+1
        elif i["age"]<90 and i["age"]>=80 and b<n:
            classB.insert(i["name"],i["age"])
            b=b+1
        elif i["age"]<80 and i["age"]>=70 and c<n:
            classC.insert(i["name"],i["age"])
            c=c+1
        else:
            if d<n:
                classD.insert(i["name"],i["age"])
                d=d+1

for i in students:
        if classA.lookup(i["name"])!=None :
            print("%s score: %d in class A" %(i["name"],i["age"]))
        elif classB.lookup(i["name"])!=None:
            print("%s score: %d in class B" %(i["name"],i["age"]))
        elif classC.lookup(i["name"])!=None:
            print("%s score: %d in class C" %(i["name"],i["age"]))
        elif classD.lookup(i["name"])!=None:
            print("%s score: %d in class D" %(i["name"],i["age"]))
        else:
            print("%s score: %d is not in any class"%(i["name"],i["age"]))

"""
