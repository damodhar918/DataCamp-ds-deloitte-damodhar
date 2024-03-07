
# FastAPI Commands

This document contains commands for running and interacting with a FastAPI application.

## Running the Application

To run the FastAPI application, use the following command:

```bash
uvicorn main1:app --reload
```

This command starts the FastAPI application defined in the `main1.py` file. The `--reload` flag enables hot reloading, which means the server will automatically update whenever you make changes to your code.

## Interacting with the API

### Updating an Item

To update an item with ID 1, use the following `curl` command:

```bash
curl -X PUT "http://127.0.0.1:8000/items/1" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\":5,\"name\":\"Updated Item\",\"description\":\"This is an updated item\",\"price\":29.99,\"is_offer\":false}"
```

This command sends a PUT request to the `/items/1` endpoint to update the item with ID 1. The request body contains the updated item data in JSON format.

### Adding a New Item

To add a new item, use the following `curl` command:

```bash
curl -X POST "http://127.0.0.1:8000/items/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"id\":5,\"name\":\"Updated Item\",\"description\":\"This is an updated item\",\"price\":29.99,\"is_offer\":false}"
```

This command sends a POST request to the `/items/` endpoint to add a new item. The request body contains the new item data in JSON format.

### Deleting an Item

To delete an item with ID 5, use the following `curl` command:

```bash
curl -X DELETE "http://127.0.0.1:8000/items/5"
```

This command sends a DELETE request to the `/items/5` endpoint to delete the item with ID 5.

### Retrieving an Item

To retrieve an item with ID 1, use the following `curl` command:

```bash
curl -X GET "http://127.0.0.1:8000/items/1" -H "accept: application/json"
```

This command sends a GET request to the `/items/1` endpoint to retrieve the item with ID 1.

### Retrieving All Items

To retrieve all items, use the following `curl` command:

```bash
curl -X GET "http://127.0.0.1:8000/items" -H "accept: application/json"
```

This command sends a GET request to the `/items` endpoint to retrieve all items.
