"""
Simple test script to verify the fuzzy logic system works correctly.
Run this before starting the server to ensure everything is set up properly.
"""

import sys
import json

print("🧪 Testing Fuzzy Logic Gift Recommendation System")
print("=" * 60)

# Test 1: Import dependencies
print("\n1️⃣ Testing imports...")
try:
    import numpy as np
    print("   ✅ NumPy imported successfully")
except ImportError as e:
    print(f"   ❌ Failed to import NumPy: {e}")
    sys.exit(1)

try:
    import skfuzzy as fuzz
    from skfuzzy import control as ctrl
    print("   ✅ scikit-fuzzy imported successfully")
except ImportError as e:
    print(f"   ❌ Failed to import scikit-fuzzy: {e}")
    print("   💡 Try: pip install scikit-fuzzy")
    sys.exit(1)

try:
    from fastapi import FastAPI
    print("   ✅ FastAPI imported successfully")
except ImportError as e:
    print(f"   ❌ Failed to import FastAPI: {e}")
    sys.exit(1)

try:
    from pydantic import BaseModel
    print("   ✅ Pydantic imported successfully")
except ImportError as e:
    print(f"   ❌ Failed to import Pydantic: {e}")
    sys.exit(1)

# Test 2: Load gifts data
print("\n2️⃣ Testing gifts database...")
try:
    with open('data/gifts.json', 'r') as f:
        data = json.load(f)
        gifts = data['gifts']
        print(f"   ✅ Loaded {len(gifts)} gifts from database")
        print(f"   📦 Sample gift: {gifts[0]['name']}")
except FileNotFoundError:
    print("   ❌ gifts.json not found in data/ directory")
    sys.exit(1)
except Exception as e:
    print(f"   ❌ Error loading gifts: {e}")
    sys.exit(1)

# Test 3: Initialize fuzzy system
print("\n3️⃣ Testing fuzzy logic system initialization...")
try:
    from fuzzy_logic import fuzzy_system
    print("   ✅ Fuzzy system initialized successfully")
    print(f"   🧠 Loaded {len(fuzzy_system.gifts)} gifts into fuzzy system")
    print(f"   📏 Created {len(fuzzy_system.rules)} fuzzy rules")
except Exception as e:
    print(f"   ❌ Error initializing fuzzy system: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 4: Test recommendation with sample data
print("\n4️⃣ Testing gift recommendation...")
try:
    user_data = {
        'age': 25,
        'budget': 60,
        'relationship': 75,
        'occasion': 'Birthday'
    }
    
    recipient_data = {
        'gender': 'Female',
        'personality': 65,
        'technical': 40,
        'creative': 85,
        'managerial': 50,
        'academic': 60,
        'style': 'Modern'
    }
    
    print("   📝 Sample user: age=25, budget=60, relationship=75")
    print("   🎁 Sample recipient: creative=85, personality=65 (extrovert)")
    
    recommendations = fuzzy_system.recommend_gifts(user_data, recipient_data, top_n=5)
    
    print(f"   ✅ Generated {len(recommendations)} recommendations")
    print("\n   🏆 Top 3 recommendations:")
    for i, gift in enumerate(recommendations[:3], 1):
        print(f"      {i}. {gift['name']} (score: {gift['fuzzy_score']:.2f})")
    
except Exception as e:
    print(f"   ❌ Error generating recommendations: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 5: Test diverse pairs generation
print("\n5️⃣ Testing image pair generation...")
try:
    pairs = fuzzy_system.get_diverse_pairs(user_data, recipient_data, num_pairs=5)
    print(f"   ✅ Generated {len(pairs)} diverse gift pairs")
    print("\n   👥 Sample pair:")
    print(f"      Option A: {pairs[0][0]['name']}")
    print(f"      Option B: {pairs[0][1]['name']}")
except Exception as e:
    print(f"   ❌ Error generating pairs: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 6: Test refinement with selections
print("\n6️⃣ Testing recommendation refinement...")
try:
    # Simulate user selections
    selected_ids = [pairs[i][0]['id'] for i in range(min(5, len(pairs)))]
    
    final_recommendations = fuzzy_system.refine_recommendations(
        user_data,
        recipient_data,
        selected_ids,
        top_n=3
    )
    
    print(f"   ✅ Refined recommendations based on {len(selected_ids)} selections")
    print("\n   🎯 Final recommendations:")
    for i, gift in enumerate(final_recommendations, 1):
        print(f"      {i}. {gift['name']} (score: {gift['fuzzy_score']:.2f})")
    
except Exception as e:
    print(f"   ❌ Error refining recommendations: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# All tests passed
print("\n" + "=" * 60)
print("✅ All tests passed! The fuzzy logic system is ready.")
print("🚀 You can now start the server with: python main.py")
print("=" * 60)
