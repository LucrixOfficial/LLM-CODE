from fastapi import FastAPI
from pydantic import BaseModel
from nlp import parse_ticket_description
from code_generation import generate_code
from unit_test_generation import generate_unit_tests

app = FastAPI()

class JiraTicket(BaseModel):
    description: str

@app.post("/generate-code/")
async def generate_code_endpoint(ticket: JiraTicket):
    parsed_info = parse_ticket_description(ticket.description)
    feature_description = parsed_info  # Extracted feature description
    code_changes = generate_code(feature_description)
    unit_tests = generate_unit_tests(feature_description)
    
    return {
        "code_diff": code_changes,
        "unit_tests": unit_tests
    }