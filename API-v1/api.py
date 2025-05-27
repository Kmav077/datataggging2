# Query API
GET /regulations/{regulation_id}/sections/{section_id}
GET /regulations/search?query="CUI Basic"&classification_level="secret"

# Rule Engine API  
POST /evaluate/classification
POST /evaluate/handling_requirements
POST /evaluate/marking_requirements

# Compliance API
POST /check/document_compliance
GET /requirements/by_classification/{level}