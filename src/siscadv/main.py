from __future__ import annotations

from datetime import datetime
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


class Visitor(BaseModel):
    """Represents a visitor registration request/record."""

    name: str = Field(..., min_length=1, description="Full name of the visitor")
    document: str = Field(..., min_length=3, description="Visitor identification document number")
    purpose: str = Field(..., min_length=3, description="Purpose of the visit")
    registered_at: datetime | None = Field(
        default=None, description="Server timestamp when the visitor was registered"
    )


class VisitorRegistry:
    """In-memory registry to store visitor records for the session."""

    def __init__(self) -> None:
        self._records: list[Visitor] = []

    def add_visitor(self, visitor: Visitor) -> Visitor:
        """Store a visitor registration and stamp it with the current time."""

        if not visitor.registered_at:
            visitor.registered_at = datetime.utcnow()
        self._records.append(visitor)
        return visitor

    def list_visitors(self) -> List[Visitor]:
        """Return all registered visitors in insertion order."""

        return list(self._records)


registry = VisitorRegistry()
app = FastAPI(title="Sistema de Cadastramento de Visitantes", version="0.1.0")


@app.get("/health", summary="Health check")
def health() -> dict[str, str]:
    """Lightweight endpoint for availability checks."""

    return {"status": "ok"}


@app.post("/visitors", response_model=Visitor, status_code=201, summary="Register a visitor")
def register_visitor(visitor: Visitor) -> Visitor:
    """Register a visitor and return the stored record."""

    try:
        return registry.add_visitor(visitor)
    except ValueError as exc:  # pragma: no cover - defensive guard
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get("/visitors", response_model=List[Visitor], summary="List visitors")
def list_visitors() -> List[Visitor]:
    """Return all registered visitors for the current server session."""

    return registry.list_visitors()
