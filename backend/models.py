"""
Pydantic Models for Gift Recommendation API
============================================
Defines data models for request/response validation.
"""

from pydantic import BaseModel, Field
from typing import List, Optional


class UserData(BaseModel):
    """User (gift giver) information."""
    age: float = Field(..., ge=0, le=100, description="User's age on a scale of 0-100")
    budget: float = Field(..., ge=0, le=100, description="Budget willingness on a scale of 0-100")
    relationship: float = Field(..., ge=0, le=100, description="Relationship closeness on a scale of 0-100")
    occasion: str = Field(..., description="Occasion for the gift (Birthday, Anniversary, etc.)")


class OtherPersonData(BaseModel):
    """Recipient (other person) information."""
    gender: str = Field(..., description="Gender of the recipient (Male/Female)")
    personality: float = Field(..., ge=0, le=100, description="Introvert (0) to Extrovert (100)")
    technical: float = Field(..., ge=0, le=100, description="Technical skill level")
    creative: float = Field(..., ge=0, le=100, description="Creative skill level")
    managerial: float = Field(..., ge=0, le=100, description="Managerial skill level")
    academic: float = Field(..., ge=0, le=100, description="Academic interest level")
    style: str = Field(..., description="Style preference (Classic, Modern, Trendy, Minimalist)")


class GenerateImagePairsRequest(BaseModel):
    """Request model for generating image pairs."""
    user: UserData
    other: OtherPersonData


class ImageInfo(BaseModel):
    """Information about a gift image."""
    path: str = Field(..., description="Image URL/path")
    value: str = Field(..., description="Gift ID")
    name: Optional[str] = Field(None, description="Gift name")
    description: Optional[str] = Field(None, description="Gift description")
    amazon_link: Optional[str] = Field(None, description="Amazon search link for the gift")


class GenerateImagePairsResponse(BaseModel):
    """Response model for image pairs."""
    imagePairs: List[List[ImageInfo]] = Field(..., description="List of image pairs for comparison")


class SelectedImages(BaseModel):
    """Selected images from the pair comparisons."""
    image0: str = Field(..., description="Selected gift ID from round 0")
    image1: str = Field(..., description="Selected gift ID from round 1")
    image2: str = Field(..., description="Selected gift ID from round 2")
    image3: str = Field(..., description="Selected gift ID from round 3")
    image4: str = Field(..., description="Selected gift ID from round 4")


class GenerateFinalImagesRequest(BaseModel):
    """Request model for generating final recommendations."""
    user: UserData
    other: OtherPersonData
    selectedImages: SelectedImages


class FinalImageInfo(BaseModel):
    """Information about a final recommended gift."""
    path: str = Field(..., description="Image URL/path")
    value: str = Field(..., description="Gift ID")
    name: str = Field(..., description="Gift name")
    description: str = Field(..., description="Gift description")
    category: str = Field(..., description="Gift category")
    fuzzy_score: float = Field(..., description="Fuzzy logic compatibility score")
    amazon_link: Optional[str] = Field(None, description="Amazon search link for the gift")


class GenerateFinalImagesResponse(BaseModel):
    """Response model for final gift recommendations."""
    finalImages: List[FinalImageInfo] = Field(..., description="Final recommended gifts")
