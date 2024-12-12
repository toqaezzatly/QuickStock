sequenceDiagram

    participant User
    participant Browser
    participant Flask_App
    participant Database

    User ->> Browser: Access /login
    Browser -->> Flask_App: GET /login
    Flask_App -->> Browser: Return login.html
    Browser -->> User: Display login
    User ->> Browser: Submit credentials
    Browser -->> Flask_App: POST /login
    Flask_App ->> Database: Check User Credentials
    Database -->> Flask_App: Return User Data or null
    alt Authentication Successful
        Flask_App -->> Browser: Redirect to /
        Browser -->> Flask_App: GET /
        Flask_App ->> Database: Get Products
        Database -->> Flask_App: Return Products
        Flask_App -->> Browser: Return index.html
        Browser -->> User: Display Inventory
    else Authentication Failed
       Flask_App -->> Browser: Return 401/Invalid Creds
       Browser -->> User: Display Error
    end

   User ->> Browser: Access /add_product
    Browser -->> Flask_App: GET /add_product
    Flask_App -->> Browser: Return add_product.html
    Browser -->> User: Display add_product
   User ->> Browser: Submit new product data
    Browser -->> Flask_App: POST /add_product
    Flask_App ->> Database: Insert new product
     Database -->> Flask_App: Confirmation
    Flask_App -->> Browser: Redirect to /
    Browser -->> Flask_App: GET /
    Flask_App ->> Database: Get Products
     Database -->> Flask_App: Return Products
        Flask_App -->> Browser: Return index.html
        Browser -->> User: Display Inventory

 User ->> Browser: Access /edit_product/1
   Browser -->> Flask_App: GET /edit_product/1
    Flask_App ->> Database: Get product data
    Database -->> Flask_App: Return product details
    Flask_App -->> Browser: Return edit_product.html
   Browser -->> User: Display edit_product
    User ->> Browser: Submit edited product data
   Browser -->> Flask_App: POST /edit_product/1
   Flask_App ->> Database: Update product data
   Database -->> Flask_App: Confirmation
      Flask_App -->> Browser: Redirect to /
      Browser -->> Flask_App: GET /
      Flask_App ->> Database: Get Products
      Database -->> Flask_App: Return Products
      Flask_App -->> Browser: Return index.html
      Browser -->> User: Display Inventory

User ->> Browser: Access /delete_product/1
    Browser -->> Flask_App: GET /delete_product/1
      Flask_App ->> Database: Delete product
      Database -->> Flask_App: Confirmation
    Flask_App -->> Browser: Redirect to /
     Browser -->> Flask_App: GET /
     Flask_App ->> Database: Get Products
      Database -->> Flask_App: Return Products
       Flask_App -->> Browser: Return index.html
       Browser -->> User: Display Inventory

  User ->> Browser: Access /logout
  Browser -->> Flask_App: GET /logout
  Flask_App -->> Flask_App: Clear Session
  Flask_App -->> Browser: Redirect to /login