"""
Gift Recommendation API using Fuzzy Logic
==========================================
FastAPI backend for personalized gift recommendations.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import (
    GenerateImagePairsRequest,
    GenerateImagePairsResponse,
    GenerateFinalImagesRequest,
    GenerateFinalImagesResponse,
    ImageInfo,
    FinalImageInfo
)
from fuzzy_logic import fuzzy_system
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Gift Recommendation API",
    description="Fuzzy logic-based gift recommendation system",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint."""
    return {
        "message": "Gift Recommendation API is running",
        "status": "healthy",
        "version": "1.0.0"
    }


@app.post("/api/generate-image-pairs", response_model=GenerateImagePairsResponse)
async def generate_image_pairs(request: GenerateImagePairsRequest):
    """
    Generate diverse gift pairs for user comparison.
    
    This endpoint uses fuzzy logic to:
    1. Score all gifts based on user and recipient attributes
    2. Select diverse, high-scoring gifts
    3. Create meaningful pairs for comparison
    
    Args:
        request: Contains user data and recipient data
    
    Returns:
        5 pairs of gift images with metadata
    """
    try:
        logger.info("Generating image pairs...")
        logger.info(f"User data: age={request.user.age}, budget={request.user.budget}, "
                   f"relationship={request.user.relationship}, occasion={request.user.occasion}")
        logger.info(f"Recipient data: gender={request.other.gender}, "
                   f"personality={request.other.personality}, technical={request.other.technical}")
        
        # Convert Pydantic models to dicts
        user_data = request.user.model_dump()
        recipient_data = request.other.model_dump()
        
        # Get diverse pairs from fuzzy system
        pairs = fuzzy_system.get_diverse_pairs(user_data, recipient_data, num_pairs=5)
        
        if not pairs or len(pairs) == 0:
            raise HTTPException(status_code=500, detail="Failed to generate gift pairs")
        
        # Convert to response format
        image_pairs = []
        for pair in pairs:
            pair_images = []
            for idx, gift in enumerate(pair):
                # Use the image_url from the gift data
                image_info = ImageInfo(
                    path=gift.get('image_url', 'placeholder.jpg'),
                    value=gift['id'],
                    name=gift['name'],
                    description=gift['description']
                )
                pair_images.append(image_info)
            image_pairs.append(pair_images)
        
        logger.info(f"Successfully generated {len(image_pairs)} image pairs")
        
        return GenerateImagePairsResponse(imagePairs=image_pairs)
        
    except Exception as e:
        logger.error(f"Error generating image pairs: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating image pairs: {str(e)}")


@app.post("/api/generate-final-images", response_model=GenerateFinalImagesResponse)
async def generate_final_images(request: GenerateFinalImagesRequest):
    """
    Generate final gift recommendations based on user selections.
    
    This endpoint:
    1. Analyzes which gifts the user preferred in pair comparisons
    2. Uses fuzzy logic to refine recommendations
    3. Returns top 3 personalized gift suggestions
    
    Args:
        request: Contains user data, recipient data, and selected gift IDs
    
    Returns:
        3 final gift recommendations with detailed information
    """
    try:
        logger.info("Generating final recommendations...")
        
        # Convert Pydantic models to dicts
        user_data = request.user.model_dump()
        recipient_data = request.other.model_dump()
        
        # Extract selected gift IDs
        selected_ids = [
            request.selectedImages.image0,
            request.selectedImages.image1,
            request.selectedImages.image2,
            request.selectedImages.image3,
            request.selectedImages.image4
        ]
        
        logger.info(f"Selected gift IDs: {selected_ids}")
        
        # Get refined recommendations from fuzzy system
        final_gifts = fuzzy_system.refine_recommendations(
            user_data,
            recipient_data,
            selected_ids,
            top_n=3
        )
        
        if not final_gifts or len(final_gifts) == 0:
            raise HTTPException(status_code=500, detail="Failed to generate final recommendations")
        
        # Convert to response format
        final_images = []
        for idx, gift in enumerate(final_gifts):
            # Use the image_url from the gift data
            final_image = FinalImageInfo(
                path=gift.get('image_url', 'placeholder.jpg'),
                value=gift['id'],
                name=gift['name'],
                description=gift['description'],
                category=gift['category'],
                fuzzy_score=round(gift['fuzzy_score'], 2)
            )
            final_images.append(final_image)
        
        logger.info(f"Successfully generated {len(final_images)} final recommendations")
        logger.info(f"Top recommendation: {final_images[0].name} (score: {final_images[0].fuzzy_score})")
        
        return GenerateFinalImagesResponse(finalImages=final_images)
        
    except Exception as e:
        logger.error(f"Error generating final recommendations: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error generating final recommendations: {str(e)}")


@app.get("/api/gifts")
async def get_all_gifts():
    """
    Get all available gifts in the database.
    
    This is a utility endpoint for debugging/exploration.
    """
    try:
        return {"gifts": fuzzy_system.gifts, "count": len(fuzzy_system.gifts)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching gifts: {str(e)}")


@app.get("/api/gifts/{gift_id}")
async def get_gift_by_id(gift_id: str):
    """
    Get a specific gift by ID.
    
    Args:
        gift_id: The ID of the gift to retrieve
    
    Returns:
        Gift details
    """
    try:
        gift = next((g for g in fuzzy_system.gifts if g['id'] == gift_id), None)
        if not gift:
            raise HTTPException(status_code=404, detail="Gift not found")
        return gift
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching gift: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4000)
