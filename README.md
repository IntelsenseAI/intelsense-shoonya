### Run `docker-compose-intelsense.yaml` file

```sh
# Change directory
cd Shoonya

# Build images
docker-compose -f docker-compose-intelsense.yaml build

# Run containers
docker-compose -f docker-compose-intelsense.yaml up -d
```


### Backend Setup
Access the backend at http://localhost:8000/

Explore the Swagger API at http://localhost:8000/swagger/

Initial steps:

1. Go to http://localhost:8000/admin/
2. Log in with the following information:
    - Email_address: `admin@gmail.com`
    - Password: `adminpassword`
3. Navigate to `Users` section
   - Click on `admin@gmail.com` to view user details
   - Fill in at least the following fields:
        - username
        - First_name
        - Last_name
        - Select the Role as `Admin` instead of `Annotator`
        - Organization 
            - click the `+` button next to the dropdown
            - Insert `Organization_title` and `Organization_email_domain`
            - Select `admin@gmail.com` as `Created_by` 
            - Click SAVE
4. Now, explore the Frontend.

### Frontend
Access the frontend at http://localhost:3000/

Sign in with the following information:
   - Email Address: `admin@gmail.com`
   - Password: `adminpassword`


