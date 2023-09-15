# 
#### question schema
- id: String
- value: String
- options: Array
  - value: String
  - isAnswer: boolean
- comments: Array
  - id: String
  - value: String
  - upVoteCount: Int
  - downVoteCount: Int
  - createdAt: Datetime
  - lastModifiedAt: Datetime
  - createdBy: String
  - lastModifiedBy: String
  - replies: Array
    - id: String
    - value: String
    - upVoteCount: Int
    - downVoteCount: Int
    - createdAt: Datetime
    - lastModifiedAt: Datetime
    - createdBy: String
    - lastModifiedBy: String
- createdAt: Datetime
- lastModifiedAt: Datetime
- createdBy: String
- lastModifiedBy: String

#### References
- https://stackoverflow.com/questions/29508162/how-can-i-validate-username-password-for-mongodb-authentication-through-pymongo
- 