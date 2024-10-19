from pydantic import BaseModel, EmailStr

class RegistrationConfirmation(BaseModel):
    email: EmailStr  # Используем EmailStr для валидации формата email
