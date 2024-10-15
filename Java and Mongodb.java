package com_practical.mongodb_conn;
import java.util.Arrays;
public class MyPortlet {
	public static void main(String[] args) {

		String uri = "mongodb://localhost:27017";

		ConnectionString connectionString = new ConnectionString(uri);
		MongoClientSettings settings = MongoClientSettings.builder().applyConnectionString(connectionString).build();

		MongoClient mongoClient = MongoClients.create(settings);

		MongoDatabase database = mongoClient.getDatabase("myDatabase"); // Replace with your database name

		MongoCollection<Document> collection = database.getCollection("Student"); // Replace with your collection name

		Document document = new Document("name", "John Doe").append("age",59).append("skills",
				Arrays.asList("Java", "MongoDB", "Spring"));
		collection.insertOne(document);
		System.out.println("Document inserted successfully!");

		Document foundDocument = collection.find(new Document("name", "John Doe")).first();
		if (foundDocument != null) {
			System.out.println("Found Document: " + foundDocument.toJson());
		}

		collection.deleteOne(new Document("name", "John Doe"));
		System.out.println("Document deleted successfully!");

		mongoClient.close();
	}

}
