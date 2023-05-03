from voluptuous import Schema, PREVENT_EXTRA, Length, All


def is_email_true(email):
    if "@" in email and "." in email:
        return True
    raise ValueError("Not email")


user_schema = Schema(
    {
        "id": int,
        "email": All(str, is_email_true),
        "first_name": str,
        "last_name": str,
        "avatar": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

list_user_schema = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": All([user_schema], Length(min=1)),
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)

resource_schema = Schema(
    {
        "id": int,
        "name": str,
        "year": int,
        "color": str,
        "pantone_value": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

created_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

updated_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

register_schema = Schema(
    {
        "id": int,
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)
