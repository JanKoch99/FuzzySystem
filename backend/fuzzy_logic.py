"""
Fuzzy Logic System for Gift Recommendation
===========================================
This module implements a fuzzy logic controller that recommends gifts based on:
- User attributes (age, budget, relationship closeness)
- Recipient attributes (personality, technical, creative, managerial, academic traits)
- Occasion and style preferences
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from typing import Dict, List, Any
import json
import os


class GiftRecommendationFuzzySystem:
    """
    A fuzzy logic system for personalized gift recommendations.
    
    This system uses multiple fuzzy variables and rules to score gifts
    based on compatibility with the gift giver and recipient.
    """
    
    def __init__(self):
        """Initialize the fuzzy system with all variables and rules."""
        self._setup_fuzzy_variables()
        self._setup_membership_functions()
        self._setup_rules()
        self._create_control_system()
        self._load_gifts_data()
    
    def _setup_fuzzy_variables(self):
        """Define all fuzzy input and output variables."""
        
        # Input variables for USER (gift giver)
        self.user_age = ctrl.Antecedent(np.arange(0, 101, 1), 'user_age')
        self.user_budget = ctrl.Antecedent(np.arange(0, 101, 1), 'user_budget')
        self.relationship = ctrl.Antecedent(np.arange(0, 101, 1), 'relationship')
        
        # Input variables for RECIPIENT
        self.personality = ctrl.Antecedent(np.arange(0, 101, 1), 'personality')
        self.technical = ctrl.Antecedent(np.arange(0, 101, 1), 'technical')
        self.creative = ctrl.Antecedent(np.arange(0, 101, 1), 'creative')
        self.managerial = ctrl.Antecedent(np.arange(0, 101, 1), 'managerial')
        self.academic = ctrl.Antecedent(np.arange(0, 101, 1), 'academic')
        
        # Output variable - gift compatibility score
        self.gift_score = ctrl.Consequent(np.arange(0, 101, 1), 'gift_score')
    
    def _setup_membership_functions(self):
        """Define membership functions for all variables."""
        
        # User age membership functions
        self.user_age['young'] = fuzz.trapmf(self.user_age.universe, [0, 0, 25, 40])
        self.user_age['middle'] = fuzz.trimf(self.user_age.universe, [30, 50, 70])
        self.user_age['mature'] = fuzz.trapmf(self.user_age.universe, [60, 75, 100, 100])
        
        # Budget membership functions
        self.user_budget['low'] = fuzz.trapmf(self.user_budget.universe, [0, 0, 30, 45])
        self.user_budget['medium'] = fuzz.trimf(self.user_budget.universe, [35, 50, 65])
        self.user_budget['high'] = fuzz.trapmf(self.user_budget.universe, [55, 70, 100, 100])
        
        # Relationship closeness membership functions
        self.relationship['distant'] = fuzz.trapmf(self.relationship.universe, [0, 0, 20, 40])
        self.relationship['friend'] = fuzz.trimf(self.relationship.universe, [30, 50, 70])
        self.relationship['close'] = fuzz.trapmf(self.relationship.universe, [60, 80, 100, 100])
        
        # Personality (introvert to extrovert) membership functions
        self.personality['introvert'] = fuzz.trapmf(self.personality.universe, [0, 0, 30, 50])
        self.personality['ambivert'] = fuzz.trimf(self.personality.universe, [35, 50, 65])
        self.personality['extrovert'] = fuzz.trapmf(self.personality.universe, [50, 70, 100, 100])
        
        # Technical skill membership functions
        self.technical['low'] = fuzz.trapmf(self.technical.universe, [0, 0, 30, 50])
        self.technical['medium'] = fuzz.trimf(self.technical.universe, [35, 50, 65])
        self.technical['high'] = fuzz.trapmf(self.technical.universe, [50, 70, 100, 100])
        
        # Creative skill membership functions
        self.creative['low'] = fuzz.trapmf(self.creative.universe, [0, 0, 30, 50])
        self.creative['medium'] = fuzz.trimf(self.creative.universe, [35, 50, 65])
        self.creative['high'] = fuzz.trapmf(self.creative.universe, [50, 70, 100, 100])
        
        # Managerial skill membership functions
        self.managerial['low'] = fuzz.trapmf(self.managerial.universe, [0, 0, 30, 50])
        self.managerial['medium'] = fuzz.trimf(self.managerial.universe, [35, 50, 65])
        self.managerial['high'] = fuzz.trapmf(self.managerial.universe, [50, 70, 100, 100])
        
        # Academic interest membership functions
        self.academic['low'] = fuzz.trapmf(self.academic.universe, [0, 0, 30, 50])
        self.academic['medium'] = fuzz.trimf(self.academic.universe, [35, 50, 65])
        self.academic['high'] = fuzz.trapmf(self.academic.universe, [50, 70, 100, 100])
        
        # Gift score output membership functions
        self.gift_score['poor'] = fuzz.trapmf(self.gift_score.universe, [0, 0, 20, 35])
        self.gift_score['fair'] = fuzz.trimf(self.gift_score.universe, [25, 40, 55])
        self.gift_score['good'] = fuzz.trimf(self.gift_score.universe, [45, 60, 75])
        self.gift_score['excellent'] = fuzz.trapmf(self.gift_score.universe, [65, 80, 100, 100])
    
    def _setup_rules(self):
        """Define fuzzy rules for gift recommendation."""
        
        self.rules = []
        
        # Rules for technical gifts (electronics, gadgets)
        self.rules.append(ctrl.Rule(
            self.technical['high'] & self.user_budget['high'],
            self.gift_score['excellent']
        ))
        self.rules.append(ctrl.Rule(
            self.technical['high'] & self.user_budget['medium'],
            self.gift_score['good']
        ))
        self.rules.append(ctrl.Rule(
            self.technical['low'] & self.user_budget['high'],
            self.gift_score['fair']
        ))
        
        # Rules for creative gifts (art supplies, DIY kits)
        self.rules.append(ctrl.Rule(
            self.creative['high'] & self.personality['introvert'],
            self.gift_score['excellent']
        ))
        self.rules.append(ctrl.Rule(
            self.creative['high'] & self.user_budget['medium'],
            self.gift_score['good']
        ))
        
        # Rules for academic gifts (books, courses, stationery)
        self.rules.append(ctrl.Rule(
            self.academic['high'] & self.personality['introvert'],
            self.gift_score['excellent']
        ))
        self.rules.append(ctrl.Rule(
            self.academic['high'] & self.managerial['high'],
            self.gift_score['good']
        ))
        
        # Rules for managerial/professional gifts (planners, desk items)
        self.rules.append(ctrl.Rule(
            self.managerial['high'] & self.user_budget['high'],
            self.gift_score['excellent']
        ))
        self.rules.append(ctrl.Rule(
            self.managerial['high'] & self.academic['high'],
            self.gift_score['good']
        ))
        
        # Rules for social/experience gifts
        self.rules.append(ctrl.Rule(
            self.personality['extrovert'] & self.relationship['close'],
            self.gift_score['excellent']
        ))
        self.rules.append(ctrl.Rule(
            self.personality['extrovert'] & self.user_budget['high'],
            self.gift_score['good']
        ))
        
        # Rules based on relationship closeness
        self.rules.append(ctrl.Rule(
            self.relationship['close'] & self.user_budget['high'],
            self.gift_score['excellent']
        ))
        self.rules.append(ctrl.Rule(
            self.relationship['close'] & self.user_budget['medium'],
            self.gift_score['good']
        ))
        self.rules.append(ctrl.Rule(
            self.relationship['distant'] & self.user_budget['low'],
            self.gift_score['fair']
        ))
        
        # Rules for budget constraints
        self.rules.append(ctrl.Rule(
            self.user_budget['low'] & self.relationship['distant'],
            self.gift_score['fair']
        ))
        
        # Balanced gifts for ambiverts
        self.rules.append(ctrl.Rule(
            self.personality['ambivert'] & self.creative['medium'],
            self.gift_score['good']
        ))
        
        # Rules involving user age (needed to activate the variable)
        self.rules.append(ctrl.Rule(
            self.user_age['young'] & self.technical['high'],
            self.gift_score['excellent']
        ))
        self.rules.append(ctrl.Rule(
            self.user_age['mature'] & self.academic['high'],
            self.gift_score['good']
        ))
        
        # Default rules
        self.rules.append(ctrl.Rule(
            self.user_budget['medium'] & self.relationship['friend'],
            self.gift_score['good']
        ))
    
    def _create_control_system(self):
        """Create the fuzzy control system from rules."""
        self.control_system = ctrl.ControlSystem(self.rules)
        self.simulator = ctrl.ControlSystemSimulation(self.control_system)
    
    def _load_gifts_data(self):
        """Load gifts from JSON file."""
        gifts_path = os.path.join(os.path.dirname(__file__), 'data', 'gifts.json')
        with open(gifts_path, 'r') as f:
            data = json.load(f)
            self.gifts = data['gifts']
    
    def calculate_gift_score(self, gift: Dict, user_data: Dict, recipient_data: Dict) -> float:
        """
        Calculate fuzzy logic score for a specific gift.
        
        Args:
            gift: Gift item dictionary
            user_data: User preferences (age, budget, relationship, occasion)
            recipient_data: Recipient traits (personality, skills, style, gender)
        
        Returns:
            Float score between 0 and 100
        """
        try:
            # Set input values for fuzzy system
            self.simulator.input['user_age'] = float(user_data.get('age', 50))
            self.simulator.input['user_budget'] = float(user_data.get('budget', 50))
            self.simulator.input['relationship'] = float(user_data.get('relationship', 50))
            
            self.simulator.input['personality'] = float(recipient_data.get('personality', 50))
            self.simulator.input['technical'] = float(recipient_data.get('technical', 50))
            self.simulator.input['creative'] = float(recipient_data.get('creative', 50))
            self.simulator.input['managerial'] = float(recipient_data.get('managerial', 50))
            self.simulator.input['academic'] = float(recipient_data.get('academic', 50))
            
            # Compute fuzzy output
            self.simulator.compute()
            base_score = self.simulator.output['gift_score']
            
            # Apply additional matching bonuses
            bonus_score = 0.0
            
            # Budget compatibility bonus
            gift_price = gift['price_range']
            user_budget_value = float(user_data.get('budget', 50))
            budget_match = 100 - abs(gift_price - user_budget_value)
            bonus_score += (budget_match / 100) * 10
            
            # Personality match bonus
            personality_diff = abs(
                gift['attributes']['personality'] - 
                float(recipient_data.get('personality', 50))
            )
            bonus_score += (1 - personality_diff / 100) * 10
            
            # Technical match bonus
            technical_diff = abs(
                gift['attributes']['technical'] - 
                float(recipient_data.get('technical', 50))
            )
            bonus_score += (1 - technical_diff / 100) * 8
            
            # Creative match bonus
            creative_diff = abs(
                gift['attributes']['creative'] - 
                float(recipient_data.get('creative', 50))
            )
            bonus_score += (1 - creative_diff / 100) * 8
            
            # Managerial match bonus
            managerial_diff = abs(
                gift['attributes']['managerial'] - 
                float(recipient_data.get('managerial', 50))
            )
            bonus_score += (1 - managerial_diff / 100) * 7
            
            # Academic match bonus
            academic_diff = abs(
                gift['attributes']['academic'] - 
                float(recipient_data.get('academic', 50))
            )
            bonus_score += (1 - academic_diff / 100) * 7
            
            # Occasion match bonus
            occasion = user_data.get('occasion', '')
            if occasion and occasion in gift['attributes']['occasions']:
                bonus_score += 10
            
            # Style match bonus
            style = recipient_data.get('style', '')
            if style and style == gift['attributes']['style']:
                bonus_score += 8
            
            # Gender match bonus
            gender = recipient_data.get('gender', '').lower()
            gift_gender = gift['attributes']['gender'].lower()
            if gift_gender == 'neutral' or gift_gender == gender:
                bonus_score += 5
            
            # Relationship score bonus
            relationship_match = abs(
                gift['attributes']['relationship_score'] - 
                float(user_data.get('relationship', 50))
            )
            bonus_score += (1 - relationship_match / 100) * 7
            
            # Combine base score with bonus
            final_score = min(100, base_score + bonus_score)
            
            return final_score
            
        except Exception as e:
            print(f"Error calculating score for gift {gift.get('name', 'unknown')}: {e}")
            return 0.0
    
    def recommend_gifts(self, user_data: Dict, recipient_data: Dict, top_n: int = 10) -> List[Dict]:
        """
        Recommend top N gifts based on fuzzy logic scoring.
        
        Args:
            user_data: User preferences
            recipient_data: Recipient traits
            top_n: Number of top gifts to return
        
        Returns:
            List of gift dictionaries with scores
        """
        scored_gifts = []
        
        for gift in self.gifts:
            score = self.calculate_gift_score(gift, user_data, recipient_data)
            gift_with_score = gift.copy()
            gift_with_score['fuzzy_score'] = score
            scored_gifts.append(gift_with_score)
        
        # Sort by score descending
        scored_gifts.sort(key=lambda x: x['fuzzy_score'], reverse=True)
        
        return scored_gifts[:top_n]
    
    def get_diverse_pairs(self, user_data: Dict, recipient_data: Dict, num_pairs: int = 5) -> List[List[Dict]]:
        """
        Generate diverse gift pairs for user comparison.
        
        This method creates pairs of gifts that:
        - Are reasonably matched to the user/recipient
        - Represent different categories/types
        - Provide meaningful choices
        
        Args:
            user_data: User preferences
            recipient_data: Recipient traits
            num_pairs: Number of pairs to generate
        
        Returns:
            List of pairs, where each pair is [gift1, gift2]
        """
        # Get top candidates
        top_gifts = self.recommend_gifts(user_data, recipient_data, top_n=30)
        
        pairs = []
        used_indices = set()
        
        # Try to create diverse pairs
        for i in range(num_pairs):
            if len(top_gifts) < 2:
                break
            
            # Find two gifts from different categories
            gift1_idx = None
            gift2_idx = None
            
            for idx in range(len(top_gifts)):
                if idx not in used_indices:
                    if gift1_idx is None:
                        gift1_idx = idx
                    elif top_gifts[idx]['category'] != top_gifts[gift1_idx]['category']:
                        gift2_idx = idx
                        break
            
            # If we couldn't find different categories, just pick next available
            if gift2_idx is None:
                for idx in range(len(top_gifts)):
                    if idx not in used_indices and idx != gift1_idx:
                        gift2_idx = idx
                        break
            
            if gift1_idx is not None and gift2_idx is not None:
                pairs.append([top_gifts[gift1_idx], top_gifts[gift2_idx]])
                used_indices.add(gift1_idx)
                used_indices.add(gift2_idx)
        
        return pairs
    
    def refine_recommendations(
        self, 
        user_data: Dict, 
        recipient_data: Dict, 
        selected_gifts: List[str],
        top_n: int = 3
    ) -> List[Dict]:
        """
        Refine recommendations based on user's previous selections.
        
        Args:
            user_data: User preferences
            recipient_data: Recipient traits
            selected_gifts: List of gift IDs that user selected in pairs
            top_n: Number of final recommendations
        
        Returns:
            List of top recommended gifts
        """
        # Get all scored gifts
        all_gifts = self.recommend_gifts(user_data, recipient_data, top_n=len(self.gifts))
        
        # Analyze selected gifts to understand preferences
        selected_gift_objects = [g for g in all_gifts if g['id'] in selected_gifts]
        
        if not selected_gift_objects:
            # If no valid selections, return top gifts
            return all_gifts[:top_n]
        
        # Calculate average attributes of selected gifts
        avg_attributes = {
            'personality': np.mean([g['attributes']['personality'] for g in selected_gift_objects]),
            'technical': np.mean([g['attributes']['technical'] for g in selected_gift_objects]),
            'creative': np.mean([g['attributes']['creative'] for g in selected_gift_objects]),
            'managerial': np.mean([g['attributes']['managerial'] for g in selected_gift_objects]),
            'academic': np.mean([g['attributes']['academic'] for g in selected_gift_objects]),
            'price_range': np.mean([g['price_range'] for g in selected_gift_objects])
        }
        
        # Re-score gifts with preference bonus
        for gift in all_gifts:
            preference_bonus = 0
            
            # Bonus for similarity to selected gifts
            for attr in ['personality', 'technical', 'creative', 'managerial', 'academic']:
                diff = abs(gift['attributes'][attr] - avg_attributes[attr])
                preference_bonus += (1 - diff / 100) * 3
            
            # Price range bonus (at top level, not in attributes)
            price_diff = abs(gift['price_range'] - avg_attributes['price_range'])
            preference_bonus += (1 - price_diff / 100) * 3
            
            gift['fuzzy_score'] += preference_bonus
        
        # Re-sort and return top N
        all_gifts.sort(key=lambda x: x['fuzzy_score'], reverse=True)
        
        return all_gifts[:top_n]


# Create singleton instance
fuzzy_system = GiftRecommendationFuzzySystem()
