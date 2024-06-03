# Hibiki
run ./requirement.sh

<!-- Create a seller (POST): -->
curl -X POST -H "Content-Type: application/json" -d '{"seller_name":"John Doe", "profile_pic":"url_to_pic", "phone_number":1234567890, "address":"123 Main St"}' http://127.0.0.1:5000/sellers

Get all sellers (GET)
curl http://127.0.0.1:5000/sellers

Get a seller by ID (GET):
curl http://127.0.0.1:5000/sellers/1


Update a seller (PUT):
curl -X PUT -H "Content-Type: application/json" -d '{"seller_name":"Jane Doe", "profile_pic":"new_url_to_pic", "phone_number":9876543210, "address":"456 Main St"}' http://127.0.0.1:5000/sellers/1

Delete a seller(Delete)
curl -X DELETE http://127.0.0.1:5000/sellers/1
