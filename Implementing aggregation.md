A:To create the collection we have to use following command
db.createCollection("books")

db.books.insert([{title:"Mongodb",price:200,type:"ebook"},
... {title:"Artificial Intelligence",price:300,type:"ebook"},
... {title:"Advanced Web Programming",price:400,type:"online"},
... {title:"Android",price:500,type:"online"}])

db.books.aggregate([{$group:{_id:"$Type",category:{$sum:1}}}])
db.books.aggregate([{$group:{_id:"$Type",max_price:{$max:"$price"}}}])
db.books.aggregate([{$group:{_id:"$Type",min_price:{$min:"$price"}}}])
db.books.aggregate([{$group:{_id:"$Type",avg_price:{$avg:"$price"}}}])


B:Write a MongoDB query to use push and add to set expression
db.books.insertOne({title:"HTML",price:985,type:"HardCopy"})
db.books.updateOne({title:"HTML"},{$push:{publication:"techKnowledge"}})
db.books.find()


db.books.insertOne({title:"Python",price:985,type:"Hardcopy"})
db.books.updateOne({title:"Python"},{$addToSet:{unites:10}})
db.books.find()

C:To use the first expression we use following command
#first
db.books.aggregate([{$group:{_id:"$type",first_data:{$first:"$price"}}}])
#last
db.books.aggregate([{$group:{_id:"$type",last_data:{$last:"$Title"}}}])
