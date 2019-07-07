# RestAPI
RestAPI for a Social Media website using Django's Rest Framework and Docker

## The app has the following Endpoints

### 1. Feed
- GET: lists all the posts of all users in chronological order 
```/api/feed/```
- GET: lists all the posts of a specific user in chronological order 
``` /api/feed/<int:user_id>/ ```
- /api/feed/followees/ GET: lists all the posts of followed users in chronological order 
- /api/feed/friends/ GET: lists all the posts of the logged in user’s friends in chronological order 

### 2.Posts
- /api/posts/<int:post_id>/ GET: get a specific post by ID and display all the information about that post 
- /api/posts/<int:post_id>/ PATCH: update a specific post (only allow owner of post or admin) 
- /api/posts/<int:post_id>/ DELETE: delete a post by ID (only allow owner of post or admin) 
- /api/posts/like/<int:post_id>/ POST: like a post 
- /api/posts/like/<int:post_id>/ DELETE: remove like from a post 
- /api/posts/new-post/ POST: user can make a new post by sending post data 
- /api/posts/likes/ GET: the list of the posts the user likes 

### 3. Users
- /api/users/follow/<int:user_id>/ POST: follow a user 
- /api/users/follow/<int:user_id>/ DELETE: unfollow a user 
- /api/users/followers/ GET: List of all the logged in user’s followers 
- /api/users/following/ GET: List of all the people the user is following 
- /api/users/ GET: Get all the users 
- /api/users/<int:user_id>/ GET: Get specific user profile 
- /api/users/friendrequests/<int:user_id>/ POST: Send friend request to another user 
- /api/users/friendrequests/ GET: List all open friend requests from others 
- /api/users/friendrequests/pending/ GET: List all the logged in user’s pending friend requests 
- /api/users/friendrequests/accept/<int:request_id>/ POST: Accept an open friend request 
- /api/users/friendrequests/reject/<int:request_id>/ POST: Reject an open friend request 
- /api/users/friends/ GET: List all accepted friends 
- /api/users/friends/unfriend/<int:user_id>/ DELETE: Unfriend a user 

### 4. Me
- /api/me/ GET: Get logged in user’s profile (as well private information like email, etc.) 
 - /api/me/ POST: Update the logged in user’s profile public info) 

### 5. Registration
 - /api/registration/ POST: Register a new user by asking for an email (send email validation code) 
 - /api/registration/validation/ POST: Validate a new registered user with a validation code sent by email