db.createCollection("student")

db.student.insert([{name:"Huzaifa",rollno :10,gender:"M",class:"TYIT"},
... {name:"Maaz",rollno :20,gender:"M",class:"TYIT"},
... {name:"Nafis",rollno :30,gender:"M",class:"TYIT"},
... {name:"Nafisa",rollno :23,gender:"F",class:"TYIT"},
... {name:"neelam",rollno :24,gender:"F",class:"TYIT"}])

db.student.find()
db.student.findOne()
db.student.find({name:"Huzaifa"},{name:true})

db.student.find({rollno:{$gt:24}})
db.student.find({rollno:{$gte:24}})
db.student.find({rollno:{$lte:24}})


db.student.find({$or:[{name:"Maaz"},{gender:{$gte:"M"}}]})

db.student.update({rollno:24},{$set:{name:"Nafis"}})

db.student.find()

db.student.remove({name:"Nafisa"})
db.student.drop()
