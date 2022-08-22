provider "aws" { 
   access_key = "YOUR ACCESS KEY" 
   secret_key = "YOUR SECRET KEY"
   region = var.aws_region
   endpoints {
    dynamodb = "http://localhost:4566"
  }
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true
}

