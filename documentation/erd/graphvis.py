from graphviz import Digraph

# Create a detailed ERD with attributes and data types
erd_detailed = Digraph('ERD_Detailed', filename='cars_hub_erd', format='png')

# Entities with attributes
entities_detailed = {
    "User": [
        "UserID (PK, INT)", "Username (VARCHAR)", "Email (VARCHAR)",
        "Password (VARCHAR)"
    ],
    "UserProfile": [
        "UserProfileID (PK, INT)", "UserID (FK, INT)",
        "Phone (VARCHAR)", "ProfileImageURL (Filefield)",
        "CreatedDate (DATETIME)"
    ],
    "Car": [
        "CarID (PK, INT)", "UserID (FK, INT)", "Title (VARCHAR)",
        "Model (VARCHAR)", "Brand (VARCHAR)", "Age (INT)",
        "CategoryID (FK, INT)", "Approved (INT)", "Description (TEXT)",
    ],
    "Comment": [
        "CommentID (PK, INT)", "UserID (FK, INT)", "CarID (FK, INT)",
        "Content (TEXT)", "CreatedDate (DATETIME)"
    ],
    "Like": [
        "LikeID (PK, INT)", "UserID (FK, INT)", "CarID (FK, INT)"
    ],
    "Car_Category": [
        "CategoryID (PK, INT)", "CategoryName (VARCHAR)",
        "ImageURL (Filefield)", "CreatedDate (DATETIME)"
    ],
    "Car_Images": [
        "ImageID (PK, INT)", "CarID (FK, INT)", "ImageURL (Filefield)"
    ],
    "Inquiry": [
        "InquiryID (PK, INT)", "Email (VARCHAR)", "Name (VARCHAR)",
        "Message (TEXT)", "Read (INT)", "CreatedDate (DATETIME)"
    ],
    "About": [
        "AboutID (PK, INT)", "Description (TEXT)", "ImageURL (Filefield)",
        "UpdatedDate (DATETIME)"
    ]
}

# Add entities and attributes to the ERD
for entity, attributes in entities_detailed.items():
    label = f"{entity} | " + " \\n ".join(attributes)
    erd_detailed.node(entity, label=label, shape='record')

# Relationships
relations_detailed = [
    ("User", "UserProfile"),
    ("Car_Category", "Car"),
    ("Car", "Car_Images"),
    ("User", "Comment"),
    ("User", "Car"),
    ("User", "Like"),
    ("Car", "Like"),
    ("Car", "Comment"),
]

for src, dst in relations_detailed:
    erd_detailed.edge(src, dst)

# Save ERD as PNG image
erd_detailed.render('cars_hub_erd', format='png', cleanup=False)

