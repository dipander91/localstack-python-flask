resource "aws_dynamodb_table" "employee-ddb-table" {
  name           = "employee"
  read_capacity  = 1
  write_capacity = 1
  hash_key       = "employeeId"
  range_key      = "city"

  attribute {
    name = "employeeId"
    type = "S"
  }

  attribute {
    name = "city"
    type = "S"
  }

  tags = {
    Name        = "dynamodb-employee-table"
    Environment = "localstack"
  }
}