import uuid
import random
from faker import Faker
from datetime import datetime, timedelta
import string  
import pytz

from location_data import USZipcodeLocationData

fake = Faker()

FULFILLMENT_CENTERS = [
    "FC_Atlanta",
    "FC_Dallas",
    "FC_LosAngeles",
    "FC_Chicago",
    "FC_Seattle",
    "FC_NewYork",
    "FC_Denver",
    "FC_Miami",
    "FC_Phoenix",
    "FC_Boston",
    "FC_Detroit",
    "FC_Houston"
]

COUPON_DETAILS = {
    "SAVE10": {
        "discount": 0.10,
        "usage_limit": 1000,
        "stackable": True
    },
    "WELCOME": {
        "discount": 0.05,
        "usage_limit": 500,
        "stackable": True
    },
    "PETSAREGREAT": {
        "discount": 0.15,
        "usage_limit": 50,
        "stackable": False
    },
    "FREESHIP": {
        "discount": 0.0,
        "usage_limit": 300,
        "stackable": True
    }
}

COUPON_USAGE = {
    "SAVE10": 0,
    "WELCOME": 0,
    "PETSAREGREAT": 0,
    "FREESHIP": 0
}

B2G1_PROMOS = {
    "DOG_TREAT_BISCUIT": (2, 1),
    "CAT_TREAT_CRUNCHY": (2, 1)
}

CURRENCY_OPTIONS = ["USD", "EUR", "CAD"]
EXCHANGE_RATES = {
    "USD": 1.0,
    "EUR": 1.07,
    "CAD": 0.75
}

PRODUCT_CATALOG = {
    "DOG_DRY_PURINA_PRO_PLAN_7.7LB": {
        "name": "Purina Pro Plan Adult Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 22.99
    },
    "DOG_DRY_PURINA_PRO_PLAN_15.5LB": {
        "name": "Purina Pro Plan Adult Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 36.99
    },
    "DOG_DRY_PURINA_PRO_PLAN_25.5LB": {
        "name": "Purina Pro Plan Adult Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 49.99
    },

    "DOG_DRY_PEDIGREE_7.7LB": {
        "name": "Pedigree Complete Nutrition - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 18.99
    },
    "DOG_DRY_PEDIGREE_15.5LB": {
        "name": "Pedigree Complete Nutrition - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 26.99
    },
    "DOG_DRY_PEDIGREE_25.5LB": {
        "name": "Pedigree Complete Nutrition - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 34.99
    },

    "DOG_DRY_IAMS_7.7LB": {
        "name": "Iams Minichunks Adult Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 19.99
    },
    "DOG_DRY_IAMS_15.5LB": {
        "name": "Iams Minichunks Adult Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 29.99
    },
    "DOG_DRY_IAMS_25.5LB": {
        "name": "Iams Minichunks Adult Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 39.99
    },

    "DOG_DRY_EUKANUBA_7.7LB": {
        "name": "Eukanuba Adult Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 21.99
    },
    "DOG_DRY_EUKANUBA_15.5LB": {
        "name": "Eukanuba Adult Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 35.99
    },
    "DOG_DRY_EUKANUBA_25.5LB": {
        "name": "Eukanuba Adult Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 46.99
    },

    "DOG_DRY_BLUE_BUFFALO_WILDERNESS_7.7LB": {
        "name": "Blue Buffalo Wilderness Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 25.99
    },
    "DOG_DRY_BLUE_BUFFALO_WILDERNESS_15.5LB": {
        "name": "Blue Buffalo Wilderness Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 42.99
    },
    "DOG_DRY_BLUE_BUFFALO_WILDERNESS_25.5LB": {
        "name": "Blue Buffalo Wilderness Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 54.99
    },

    "DOG_DRY_MERRICK_7.7LB": {
        "name": "Merrick Healthy Grains Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 24.99
    },
    "DOG_DRY_MERRICK_15.5LB": {
        "name": "Merrick Healthy Grains Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 40.99
    },
    "DOG_DRY_MERRICK_25.5LB": {
        "name": "Merrick Healthy Grains Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 52.99
    },

    "DOG_DRY_WELLNESS_7.7LB": {
        "name": "Wellness Complete Health Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 23.99
    },
    "DOG_DRY_WELLNESS_15.5LB": {
        "name": "Wellness Complete Health Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 39.99
    },
    "DOG_DRY_WELLNESS_25.5LB": {
        "name": "Wellness Complete Health Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 52.99
    },

    "DOG_DRY_HILLS_SCIENCE_DIET_7.7LB": {
        "name": "Hill’s Science Diet Adult Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 26.99
    },
    "DOG_DRY_HILLS_SCIENCE_DIET_15.5LB": {
        "name": "Hill’s Science Diet Adult Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 44.99
    },
    "DOG_DRY_HILLS_SCIENCE_DIET_25.5LB": {
        "name": "Hill’s Science Diet Adult Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 57.99
    },

    "DOG_DRY_ROYAL_CANIN_7.7LB": {
        "name": "Royal Canin Canine Health Nutrition - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 27.99
    },
    "DOG_DRY_ROYAL_CANIN_15.5LB": {
        "name": "Royal Canin Canine Health Nutrition - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 49.99
    },
    "DOG_DRY_ROYAL_CANIN_25.5LB": {
        "name": "Royal Canin Canine Health Nutrition - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 64.99
    },

    "DOG_DRY_NUTRO_7.7LB": {
        "name": "Nutro Wholesome Essentials Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 22.99
    },
    "DOG_DRY_NUTRO_15.5LB": {
        "name": "Nutro Wholesome Essentials Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 37.99
    },
    "DOG_DRY_NUTRO_25.5LB": {
        "name": "Nutro Wholesome Essentials Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 48.99
    },

    "DOG_DRY_TASTE_OF_THE_WILD_7.7LB": {
        "name": "Taste of the Wild Roasted Bison & Venison - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 23.99
    },
    "DOG_DRY_TASTE_OF_THE_WILD_15.5LB": {
        "name": "Taste of the Wild Roasted Bison & Venison - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 38.99
    },
    "DOG_DRY_TASTE_OF_THE_WILD_25.5LB": {
        "name": "Taste of the Wild Roasted Bison & Venison - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 52.99
    },

    "DOG_DRY_RACHAEL_RAY_7.7LB": {
        "name": "Rachael Ray Nutrish Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 19.99
    },
    "DOG_DRY_RACHAEL_RAY_15.5LB": {
        "name": "Rachael Ray Nutrish Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 31.99
    },
    "DOG_DRY_RACHAEL_RAY_25.5LB": {
        "name": "Rachael Ray Nutrish Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 42.99
    },

    "DOG_DRY_INSTINCT_7.7LB": {
        "name": "Instinct Original Grain-Free Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 28.99
    },
    "DOG_DRY_INSTINCT_15.5LB": {
        "name": "Instinct Original Grain-Free Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 49.99
    },
    "DOG_DRY_INSTINCT_25.5LB": {
        "name": "Instinct Original Grain-Free Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 64.99
    },

    "DOG_DRY_ORIJEN_7.7LB": {
        "name": "Orijen Original Grain-Free Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 34.99
    },
    "DOG_DRY_ORIJEN_15.5LB": {
        "name": "Orijen Original Grain-Free Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 59.99
    },
    "DOG_DRY_ORIJEN_25.5LB": {
        "name": "Orijen Original Grain-Free Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 79.99
    },

    "DOG_DRY_ACANA_7.7LB": {
        "name": "Acana Regionals Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 29.99
    },
    "DOG_DRY_ACANA_15.5LB": {
        "name": "Acana Regionals Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 54.99
    },
    "DOG_DRY_ACANA_25.5LB": {
        "name": "Acana Regionals Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 74.99
    },

    "DOG_DRY_VICTOR_7.7LB": {
        "name": "Victor Classic Hi-Pro Plus Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 19.99
    },
    "DOG_DRY_VICTOR_15.5LB": {
        "name": "Victor Classic Hi-Pro Plus Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 34.99
    },
    "DOG_DRY_VICTOR_25.5LB": {
        "name": "Victor Classic Hi-Pro Plus Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 46.99
    },

    "DOG_DRY_HONEST_KITCHEN_7.7LB": {
        "name": "The Honest Kitchen Whole Food Clusters Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 34.99
    },
    "DOG_DRY_HONEST_KITCHEN_15.5LB": {
        "name": "The Honest Kitchen Whole Food Clusters Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 57.99
    },
    "DOG_DRY_HONEST_KITCHEN_25.5LB": {
        "name": "The Honest Kitchen Whole Food Clusters Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 79.99
    },

    "DOG_DRY_EARTHBORN_7.7LB": {
        "name": "Earthborn Holistic Primitive Natural Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 24.99
    },
    "DOG_DRY_EARTHBORN_15.5LB": {
        "name": "Earthborn Holistic Primitive Natural Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 41.99
    },
    "DOG_DRY_EARTHBORN_25.5LB": {
        "name": "Earthborn Holistic Primitive Natural Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 54.99
    },

    "DOG_DRY_NATURES_RECIPE_7.7LB": {
        "name": "Nature’s Recipe Adult Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 17.99
    },
    "DOG_DRY_NATURES_RECIPE_15.5LB": {
        "name": "Nature’s Recipe Adult Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 28.99
    },
    "DOG_DRY_NATURES_RECIPE_25.5LB": {
        "name": "Nature’s Recipe Adult Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 42.99
    },

    "DOG_DRY_SOLID_GOLD_7.7LB": {
        "name": "Solid Gold Hund-N-Flocken Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 22.99
    },
    "DOG_DRY_SOLID_GOLD_15.5LB": {
        "name": "Solid Gold Hund-N-Flocken Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 36.99
    },
    "DOG_DRY_SOLID_GOLD_25.5LB": {
        "name": "Solid Gold Hund-N-Flocken Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 49.99
    },

    "DOG_DRY_CANIDAE_7.7LB": {
        "name": "Canidae All Life Stages Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 24.99
    },
    "DOG_DRY_CANIDAE_15.5LB": {
        "name": "Canidae All Life Stages Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 39.99
    },
    "DOG_DRY_CANIDAE_25.5LB": {
        "name": "Canidae All Life Stages Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 54.99
    },

    "DOG_DRY_NATURAL_BALANCE_7.7LB": {
        "name": "Natural Balance L.I.D. Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 25.99
    },
    "DOG_DRY_NATURAL_BALANCE_15.5LB": {
        "name": "Natural Balance L.I.D. Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 44.99
    },
    "DOG_DRY_NATURAL_BALANCE_25.5LB": {
        "name": "Natural Balance L.I.D. Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 58.99
    },

    "DOG_DRY_WHOLE_EARTH_FARMS_7.7LB": {
        "name": "Whole Earth Farms Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 16.99
    },
    "DOG_DRY_WHOLE_EARTH_FARMS_15.5LB": {
        "name": "Whole Earth Farms Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 29.99
    },
    "DOG_DRY_WHOLE_EARTH_FARMS_25.5LB": {
        "name": "Whole Earth Farms Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 39.99
    },

    "DOG_DRY_AMERICAN_JOURNEY_7.7LB": {
        "name": "American Journey Active Life Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 19.99
    },
    "DOG_DRY_AMERICAN_JOURNEY_15.5LB": {
        "name": "American Journey Active Life Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 32.99
    },
    "DOG_DRY_AMERICAN_JOURNEY_25.5LB": {
        "name": "American Journey Active Life Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 44.99
    },

    "DOG_DRY_CESAR_7.7LB": {
        "name": "Cesar Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 21.99
    },
    "DOG_DRY_CESAR_15.5LB": {
        "name": "Cesar Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 35.99
    },
    "DOG_DRY_CESAR_25.5LB": {
        "name": "Cesar Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 46.99
    },

    "DOG_DRY_FROMM_7.7LB": {
        "name": "Fromm Adult Gold Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 29.99
    },
    "DOG_DRY_FROMM_15.5LB": {
        "name": "Fromm Adult Gold Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 49.99
    },
    "DOG_DRY_FROMM_25.5LB": {
        "name": "Fromm Adult Gold Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 64.99
    },

    "DOG_DRY_TIKI_DOG_7.7LB": {
        "name": "Tiki Dog Aloha Pet Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 28.99
    },
    "DOG_DRY_TIKI_DOG_15.5LB": {
        "name": "Tiki Dog Aloha Pet Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 44.99
    },
    "DOG_DRY_TIKI_DOG_25.5LB": {
        "name": "Tiki Dog Aloha Pet Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 58.99
    },

    "DOG_DRY_FARMINA_7.7LB": {
        "name": "Farmina N&D Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 34.99
    },
    "DOG_DRY_FARMINA_15.5LB": {
        "name": "Farmina N&D Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 59.99
    },
    "DOG_DRY_FARMINA_25.5LB": {
        "name": "Farmina N&D Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 79.99
    },

    "DOG_DRY_BIL_JAC_7.7LB": {
        "name": "Bil-Jac Adult Select Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 18.99
    },
    "DOG_DRY_BIL_JAC_15.5LB": {
        "name": "Bil-Jac Adult Select Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 29.99
    },
    "DOG_DRY_BIL_JAC_25.5LB": {
        "name": "Bil-Jac Adult Select Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 44.99
    },

    "DOG_DRY_ZIGNATURE_7.7LB": {
        "name": "Zignature Grain-Free Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 24.99
    },
    "DOG_DRY_ZIGNATURE_15.5LB": {
        "name": "Zignature Grain-Free Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 39.99
    },
    "DOG_DRY_ZIGNATURE_25.5LB": {
        "name": "Zignature Grain-Free Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 54.99
    },

    "DOG_DRY_DAVES_7.7LB": {
        "name": "Dave’s Pet Food Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 20.99
    },
    "DOG_DRY_DAVES_15.5LB": {
        "name": "Dave’s Pet Food Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 34.99
    },
    "DOG_DRY_DAVES_25.5LB": {
        "name": "Dave’s Pet Food Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 48.99
    },

    "DOG_DRY_EAGLE_PACK_7.7LB": {
        "name": "Eagle Pack Original Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 19.99
    },
    "DOG_DRY_EAGLE_PACK_15.5LB": {
        "name": "Eagle Pack Original Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 31.99
    },
    "DOG_DRY_EAGLE_PACK_25.5LB": {
        "name": "Eagle Pack Original Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 44.99
    },

    "DOG_DRY_DR_GARYS_BEST_BREED_7.7LB": {
        "name": "Dr. Gary’s Best Breed Holistic Dry Dog Food - 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 25.99
    },
    "DOG_DRY_DR_GARYS_BEST_BREED_15.5LB": {
        "name": "Dr. Gary’s Best Breed Holistic Dry Dog Food - 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 39.99
    },
    "DOG_DRY_DR_GARYS_BEST_BREED_25.5LB": {
        "name": "Dr. Gary’s Best Breed Holistic Dry Dog Food - 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 56.99
    },

    "DOG_CANS_PURINA_PRO_PLAN_CASE12": {
        "name": "Purina Pro Plan Wet Dog Food 12.5 oz (Case of 12)",
        "category": "Dog Food (Non-Prescription)",
        "price": 19.99
    },
    "DOG_CANS_PURINA_PRO_PLAN_CASE24": {
        "name": "Purina Pro Plan Wet Dog Food 12.5 oz (Case of 24)",
        "category": "Dog Food (Non-Prescription)",
        "price": 35.99
    },

    "DOG_CANS_PEDIGREE_CASE12": {
        "name": "Pedigree Chopped Wet Dog Food 12.5 oz (Case of 12)",
        "category": "Dog Food (Non-Prescription)",
        "price": 17.99
    },
    "DOG_CANS_PEDIGREE_CASE24": {
        "name": "Pedigree Chopped Wet Dog Food 12.5 oz (Case of 24)",
        "category": "Dog Food (Non-Prescription)",
        "price": 33.99
    },

    "DOG_CANS_IAMS_CASE12": {
        "name": "Iams ProActive Health Wet Dog Food 12.5 oz (Case of 12)",
        "category": "Dog Food (Non-Prescription)",
        "price": 18.99
    },
    "DOG_CANS_IAMS_CASE24": {
        "name": "Iams ProActive Health Wet Dog Food 12.5 oz (Case of 24)",
        "category": "Dog Food (Non-Prescription)",
        "price": 34.99
    },

    "DOG_CANS_BLUE_BUFFALO_CASE12": {
        "name": "Blue Buffalo Homestyle Recipe Wet Dog Food 12.5 oz (Case of 12)",
        "category": "Dog Food (Non-Prescription)",
        "price": 25.99
    },
    "DOG_CANS_BLUE_BUFFALO_CASE24": {
        "name": "Blue Buffalo Homestyle Recipe Wet Dog Food 12.5 oz (Case of 24)",
        "category": "Dog Food (Non-Prescription)",
        "price": 47.99
    },

    "DOG_CANS_CESAR_CASE12": {
        "name": "Cesar Classic Loaf in Sauce Wet Dog Food 12.5 oz (Case of 12)",
        "category": "Dog Food (Non-Prescription)",
        "price": 18.99
    },
    "DOG_CANS_CESAR_CASE24": {
        "name": "Cesar Classic Loaf in Sauce Wet Dog Food 12.5 oz (Case of 24)",
        "category": "Dog Food (Non-Prescription)",
        "price": 35.99
    },

    "CAT_DRY_PURINA_PRO_PLAN_4.4LB": {
        "name": "Purina Pro Plan Complete Dry Cat Food - 4.4 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 14.99
    },
    "CAT_DRY_PURINA_PRO_PLAN_12.2LB": {
        "name": "Purina Pro Plan Complete Dry Cat Food - 12.2 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 24.99
    },
    "CAT_DRY_PURINA_PRO_PLAN_19.8LB": {
        "name": "Purina Pro Plan Complete Dry Cat Food - 19.8 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 36.99
    },

    "CAT_DRY_MEOW_MIX_4.4LB": {
        "name": "Meow Mix Original Dry Cat Food - 4.4 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 9.99
    },
    "CAT_DRY_MEOW_MIX_12.2LB": {
        "name": "Meow Mix Original Dry Cat Food - 12.2 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 15.99
    },
    "CAT_DRY_MEOW_MIX_19.8LB": {
        "name": "Meow Mix Original Dry Cat Food - 19.8 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 23.99
    },

    "CAT_DRY_SHEBA_4.4LB": {
        "name": "Sheba Dry Cat Food - 4.4 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 12.99
    },
    "CAT_DRY_SHEBA_12.2LB": {
        "name": "Sheba Dry Cat Food - 12.2 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 21.99
    },
    "CAT_DRY_SHEBA_19.8LB": {
        "name": "Sheba Dry Cat Food - 19.8 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 29.99
    },

    "CAT_DRY_BLUE_BUFFALO_TASTEFULS_4.4LB": {
        "name": "Blue Buffalo Tastefuls Dry Cat Food - 4.4 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 16.99
    },
    "CAT_DRY_BLUE_BUFFALO_TASTEFULS_12.2LB": {
        "name": "Blue Buffalo Tastefuls Dry Cat Food - 12.2 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 27.99
    },
    "CAT_DRY_BLUE_BUFFALO_TASTEFULS_19.8LB": {
        "name": "Blue Buffalo Tastefuls Dry Cat Food - 19.8 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 42.99
    },

    "CAT_CANS_FANCY_FEAST_CASE24": {
        "name": "Fancy Feast Classic Wet Cat Food 5.5 oz (Case of 24)",
        "category": "Cat Food (Non-Prescription)",
        "price": 18.99
    },
    "CAT_CANS_FANCY_FEAST_CASE12": {
        "name": "Fancy Feast Classic Wet Cat Food 5.5 oz (Case of 12)",
        "category": "Cat Food (Non-Prescription)",
        "price": 9.99
    },

    "CAT_CANS_FRISKIES_CASE24": {
        "name": "Friskies Pate Wet Cat Food 5.5 oz (Case of 24)",
        "category": "Cat Food (Non-Prescription)",
        "price": 16.99
    },
    "CAT_CANS_FRISKIES_CASE12": {
        "name": "Friskies Pate Wet Cat Food 5.5 oz (Case of 12)",
        "category": "Cat Food (Non-Prescription)",
        "price": 8.99
    },

    "CAT_CANS_SHEBA_CASE24": {
        "name": "Sheba Perfect Portions 5.5 oz (Case of 24)",
        "category": "Cat Food (Non-Prescription)",
        "price": 21.99
    },
    "CAT_CANS_SHEBA_CASE12": {
        "name": "Sheba Perfect Portions 5.5 oz (Case of 12)",
        "category": "Cat Food (Non-Prescription)",
        "price": 11.99
    },

    "CAT_CANS_BLUE_BUFFALO_CASE24": {
        "name": "Blue Buffalo Wilderness Wet Cat Food 5.5 oz (Case of 24)",
        "category": "Cat Food (Non-Prescription)",
        "price": 29.99
    },
    "CAT_CANS_BLUE_BUFFALO_CASE12": {
        "name": "Blue Buffalo Wilderness Wet Cat Food 5.5 oz (Case of 12)",
        "category": "Cat Food (Non-Prescription)",
        "price": 15.99
    },

    "DOG_TREAT_MILK_BONE": {
        "name": "Milk-Bone Original Dog Biscuits",
        "category": "Dog Treats",
        "price": 6.99
    },
    "DOG_TREAT_PUP_PERONI": {
        "name": "Pup-Peroni Dog Treats",
        "category": "Dog Treats",
        "price": 4.99
    },
    "DOG_TREAT_BLUE_BUFFALO": {
        "name": "Blue Buffalo Wilderness Dog Treats",
        "category": "Dog Treats",
        "price": 8.99
    },
    "DOG_TREAT_GREENIES": {
        "name": "Greenies Dental Chews for Dogs",
        "category": "Dog Treats",
        "price": 15.99
    },
    "DOG_TREAT_ZUKES": {
        "name": "Zuke’s Mini Naturals Training Treats",
        "category": "Dog Treats",
        "price": 11.49
    },
    "DOG_TREAT_NUDGES": {
        "name": "Nudges Natural Dog Treats",
        "category": "Dog Treats",
        "price": 9.49
    },
    "DOG_TREAT_MERRICK_POWER_BITES": {
        "name": "Merrick Power Bites Dog Treats",
        "category": "Dog Treats",
        "price": 9.99
    },
    "DOG_TREAT_FULL_MOON": {
        "name": "Full Moon All Natural Dog Treats",
        "category": "Dog Treats",
        "price": 12.99
    },
    "DOG_TREAT_NYLABONE_EDIBLE": {
        "name": "Nylabone Healthy Edibles Dog Chew",
        "category": "Dog Treats",
        "price": 7.99
    },
    "DOG_TREAT_OLD_MOTHER_HUBBARD": {
        "name": "Old Mother Hubbard Crunchy Dog Treats",
        "category": "Dog Treats",
        "price": 5.99
    },
    "DOG_TREAT_BOCCES_BAKERY": {
        "name": "Bocce’s Bakery Dog Biscuits",
        "category": "Dog Treats",
        "price": 8.49
    },
    "DOG_TREAT_THREE_DOG_BAKERY": {
        "name": "Three Dog Bakery Dog Cookies",
        "category": "Dog Treats",
        "price": 7.99
    },
    "DOG_TREAT_BIL_JAC": {
        "name": "Bil-Jac Soft Training Treats",
        "category": "Dog Treats",
        "price": 6.99
    },
    "DOG_TREAT_NATURAL_BALANCE": {
        "name": "Natural Balance Limited Ingredient Dog Treats",
        "category": "Dog Treats",
        "price": 8.99
    },
    "DOG_TREAT_WHIMZEES": {
        "name": "Whimzees Dental Chews",
        "category": "Dog Treats",
        "price": 14.99
    },
    "DOG_TREAT_TRUE_CHEWS": {
        "name": "True Chews Premium Jerky",
        "category": "Dog Treats",
        "price": 12.99
    },
    "DOG_TREAT_PLATO": {
        "name": "Plato Pet Treats",
        "category": "Dog Treats",
        "price": 10.99
    },
    "DOG_TREAT_NATURE_GNAWS": {
        "name": "Nature Gnaws Bully Sticks",
        "category": "Dog Treats",
        "price": 16.99
    },
    "DOG_TREAT_ETTA_SAYS": {
        "name": "Etta Says! Crunchy Deer Chews",
        "category": "Dog Treats",
        "price": 11.99
    },
    "DOG_TREAT_CADET": {
        "name": "Cadet Chicken & Duck Treats",
        "category": "Dog Treats",
        "price": 9.99
    },
    "DOG_TREAT_REDBARN": {
        "name": "Redbarn Natural Dog Treats",
        "category": "Dog Treats",
        "price": 8.49
    },
    "DOG_TREAT_BULLYMAKE": {
        "name": "Bullymake Tough Chew Treats",
        "category": "Dog Treats",
        "price": 13.99
    },
    "DOG_TREAT_CANINE_NATURALS": {
        "name": "Canine Naturals Hide Free Chews",
        "category": "Dog Treats",
        "price": 7.99
    },
    "DOG_TREAT_AMERICAN_JOURNEY": {
        "name": "American Journey Soft & Chewy Dog Treats",
        "category": "Dog Treats",
        "price": 8.99
    },
    "DOG_TREAT_STELLA_CHEWYS_FREEZE_DRIED": {
        "name": "Stella & Chewy’s Freeze-Dried Dog Treats",
        "category": "Dog Treats",
        "price": 12.99
    },
    "DOG_TREAT_WELLNESS": {
        "name": "Wellness WellBites Dog Treats",
        "category": "Dog Treats",
        "price": 9.49
    },

    "CAT_TREAT_TEMPTATIONS": {
        "name": "Temptations Classic Crunchy Cat Treats",
        "category": "Cat Treats",
        "price": 5.99
    },
    "CAT_TREAT_FELINE_GREENIES": {
        "name": "Feline Greenies Dental Treats",
        "category": "Cat Treats",
        "price": 6.49
    },
    "CAT_TREAT_BLUE_BUFFALO_BURSTS": {
        "name": "Blue Buffalo Wilderness Cat Treats",
        "category": "Cat Treats",
        "price": 7.99
    },
    "CAT_TREAT_FRISKIES_PARTY_MIX": {
        "name": "Friskies Party Mix Cat Treats",
        "category": "Cat Treats",
        "price": 4.99
    },
    "CAT_TREAT_SHEBA_MEATY_STICKS": {
        "name": "Sheba Meaty Sticks",
        "category": "Cat Treats",
        "price": 5.49
    },
    "CAT_TREAT_MEOW_MIX_BRUSHING_BITES": {
        "name": "Meow Mix Brushing Bites Dental Treats",
        "category": "Cat Treats",
        "price": 3.99
    },
    "CAT_TREAT_WELLNESS_KITTLES": {
        "name": "Wellness Kittles Crunchy Cat Treats",
        "category": "Cat Treats",
        "price": 5.49
    },
    "CAT_TREAT_HARTZ_DELECTABLES": {
        "name": "Hartz Delectables Squeeze Ups",
        "category": "Cat Treats",
        "price": 6.99
    },
    "CAT_TREAT_TIKI_CAT_STIX": {
        "name": "Tiki Cat Stix Wet Treats",
        "category": "Cat Treats",
        "price": 8.49
    },
    "CAT_TREAT_INSTINCT_FREEZE_DRIED": {
        "name": "Instinct Raw Boost Mixers",
        "category": "Cat Treats",
        "price": 9.99
    },
    "CAT_TREAT_STELLA_CHEWYS_FREEZE_DRIED": {
        "name": "Stella & Chewy’s Freeze-Dried Cat Morsels",
        "category": "Cat Treats",
        "price": 11.99
    },
    "CAT_TREAT_NULO": {
        "name": "Nulo Freestyle Grain-Free Cat Treats",
        "category": "Cat Treats",
        "price": 7.99
    },
    "CAT_TREAT_VITAL_ESSENTIALS": {
        "name": "Vital Essentials Freeze-Dried Cat Treats",
        "category": "Cat Treats",
        "price": 12.99
    },
    "CAT_TREAT_PUREBITES": {
        "name": "PureBites Freeze-Dried Cat Treats",
        "category": "Cat Treats",
        "price": 5.99
    },
    "CAT_TREAT_WHOLE_LIFE": {
        "name": "Whole Life Freeze-Dried Cat Treats",
        "category": "Cat Treats",
        "price": 8.99
    },
    "CAT_TREAT_FANCY_FEAST": {
        "name": "Fancy Feast Cat Treats (Purina)",
        "category": "Cat Treats",
        "price": 4.99
    },
    "CAT_TREAT_RACHAEL_RAY_NUTRISH": {
        "name": "Rachael Ray Nutrish LoveBites Cat Treats",
        "category": "Cat Treats",
        "price": 6.49
    },

    "RAW_STELLA_CHEWYS_DOG": {
        "name": "Stella & Chewy’s Raw Frozen Patties (Dog)",
        "category": "Raw/Dehydrated/Toppers",
        "price": 29.99
    },
    "RAW_STELLA_CHEWYS_CAT": {
        "name": "Stella & Chewy’s Raw Freeze-Dried Morsels (Cat)",
        "category": "Raw/Dehydrated/Toppers",
        "price": 23.99
    },

    "RAW_INSTINCT_DOG": {
        "name": "Instinct Raw Frozen Bites (Dog)",
        "category": "Raw/Dehydrated/Toppers",
        "price": 32.99
    },
    "RAW_INSTINCT_CAT": {
        "name": "Instinct Raw Meals (Cat)",
        "category": "Raw/Dehydrated/Toppers",
        "price": 28.99
    },

    "RAW_PRIMAL_DOG": {
        "name": "Primal Raw Frozen Dog Food",
        "category": "Raw/Dehydrated/Toppers",
        "price": 34.99
    },
    "RAW_PRIMAL_CAT": {
        "name": "Primal Raw Frozen Cat Food",
        "category": "Raw/Dehydrated/Toppers",
        "price": 29.99
    },

    "DEHYDRATED_HONEST_KITCHEN_DOG": {
        "name": "The Honest Kitchen Dehydrated Dog Food",
        "category": "Raw/Dehydrated/Toppers",
        "price": 42.99
    },
    "DEHYDRATED_HONEST_KITCHEN_CAT": {
        "name": "The Honest Kitchen Dehydrated Cat Food",
        "category": "Raw/Dehydrated/Toppers",
        "price": 36.99
    },

    "DEHYDRATED_SOJOS_DOG": {
        "name": "Sojos Complete Dehydrated Dog Food",
        "category": "Raw/Dehydrated/Toppers",
        "price": 29.99
    },

    "DEHYDRATED_GRANDMA_LUCYS_DOG": {
        "name": "Grandma Lucy’s Artisan Dehydrated Dog Food",
        "category": "Raw/Dehydrated/Toppers",
        "price": 39.99
    },

    "RAW_VITAL_ESSENTIALS_DOG": {
        "name": "Vital Essentials Raw Freeze-Dried Dog Food",
        "category": "Raw/Dehydrated/Toppers",
        "price": 27.99
    },
    "RAW_VITAL_ESSENTIALS_CAT": {
        "name": "Vital Essentials Raw Freeze-Dried Cat Food",
        "category": "Raw/Dehydrated/Toppers",
        "price": 24.99
    },

    "RAW_BIXBI_RAWBBLE_DOG": {
        "name": "Bixbi Rawbble Freeze-Dried Dog Food",
        "category": "Raw/Dehydrated/Toppers",
        "price": 21.99
    },

    "TOPPER_TIKI_DOG_BROTH": {
        "name": "Tiki Dog Broth Topper",
        "category": "Raw/Dehydrated/Toppers",
        "price": 5.99
    },
    "TOPPER_TIKI_CAT_BROTH": {
        "name": "Tiki Cat Broth Topper",
        "category": "Raw/Dehydrated/Toppers",
        "price": 5.99
    },

    "TOPPER_NULO_DOG_BROTH": {
        "name": "Nulo Freestyle Bone Broth Topper for Dogs",
        "category": "Raw/Dehydrated/Toppers",
        "price": 6.99
    },
    "TOPPER_NULO_CAT_BROTH": {
        "name": "Nulo Freestyle Bone Broth Topper for Cats",
        "category": "Raw/Dehydrated/Toppers",
        "price": 6.99
    },

    "TOPPER_MERRICK_DOG_BROTH": {
        "name": "Merrick Bone Broth Topper for Dogs",
        "category": "Raw/Dehydrated/Toppers",
        "price": 6.99
    },
    "TOPPER_MERRICK_CAT_BROTH": {
        "name": "Merrick Bone Broth Topper for Cats",
        "category": "Raw/Dehydrated/Toppers",
        "price": 6.99
    },

    "TOPPER_WERUVA_DOG_PUMPKIN": {
        "name": "Weruva Pumpkin Patch Up! Topper for Dogs",
        "category": "Raw/Dehydrated/Toppers",
        "price": 7.99
    },
    "TOPPER_WERUVA_CAT_PUMPKIN": {
        "name": "Weruva Pumpkin Patch Up! Topper for Cats",
        "category": "Raw/Dehydrated/Toppers",
        "price": 7.49
    },

    "RAW_ONLY_NATURAL_PET_DOG": {
        "name": "Only Natural Pet RawNibs Freeze-Dried Dog Food",
        "category": "Raw/Dehydrated/Toppers",
        "price": 25.99
    },
    "RAW_ONLY_NATURAL_PET_CAT": {
        "name": "Only Natural Pet RawNibs Freeze-Dried Cat Food",
        "category": "Raw/Dehydrated/Toppers",
        "price": 22.99
    },

    "TOPPER_NATURES_LOGIC_BROTH_DOG": {
        "name": "Nature’s Logic Bone Broth for Dogs",
        "category": "Raw/Dehydrated/Toppers",
        "price": 6.99
    },
    "TOPPER_NATURES_LOGIC_BROTH_CAT": {
        "name": "Nature’s Logic Bone Broth for Cats",
        "category": "Raw/Dehydrated/Toppers",
        "price": 6.99
    },

    "ACCESSORY_FRISCO_CRATE": {
        "name": "Frisco Fold & Carry Dog Crate",
        "category": "Accessories/Crates",
        "price": 44.99
    },
    "ACCESSORY_KONG_LEASH": {
        "name": "KONG Traffic Handle Dog Leash",
        "category": "Accessories/Leashes",
        "price": 17.99
    },
    "ACCESSORY_PETSAFE_HARNESS": {
        "name": "PetSafe Easy Walk Dog Harness",
        "category": "Accessories/Harnesses",
        "price": 24.99
    },
    "ACCESSORY_CHUCKIT_LAUNCHER": {
        "name": "Chuckit! Classic Ball Launcher",
        "category": "Dog Toys",
        "price": 9.99
    },
    "ACCESSORY_RUFFWEAR_OUTDOOR_GEAR": {
        "name": "Ruffwear Front Range Dog Harness",
        "category": "Accessories/Harnesses",
        "price": 39.99
    },
    "ACCESSORY_KURGO_CAR_SEAT_COVER": {
        "name": "Kurgo Car Seat Cover",
        "category": "Accessories/Car Travel",
        "price": 49.99
    },
    "ACCESSORY_BLUEBERRY_PET_COLLAR": {
        "name": "Blueberry Pet Dog Collar",
        "category": "Accessories/Collars",
        "price": 14.99
    },
    "ACCESSORY_MIDWEST_EXERCISE_PEN": {
        "name": "MidWest Exercise Pen",
        "category": "Accessories/Playpens",
        "price": 39.99
    },
    "ACCESSORY_CARLSON_PET_GATE": {
        "name": "Carlson Pet Gate with Door",
        "category": "Gates & Pens",
        "price": 44.99
    },
    "ACCESSORY_OUTWARD_HOUND_LIFE_JACKET": {
        "name": "Outward Hound Granby Dog Life Jacket",
        "category": "Dog Accessories",
        "price": 24.99
    },
    "ACCESSORY_NYLABONE_DURABLE_CHEW": {
        "name": "Nylabone Durable Chew Toy",
        "category": "Dog Toys",
        "price": 9.99
    },
    "ACCESSORY_EARTH_RATED_WASTE_BAGS": {
        "name": "Earth Rated Dog Waste Bags",
        "category": "Cleaning/Potty",
        "price": 5.99
    },
    "ACCESSORY_FURHAVEN_BED": {
        "name": "FurHaven Orthopedic Pet Bed",
        "category": "Beds & Furniture",
        "price": 32.99
    },
    "ACCESSORY_SNOOZER_CAR_SEAT": {
        "name": "Snoozer Lookout Car Seat",
        "category": "Car Travel",
        "price": 59.99
    },
    "ACCESSORY_KH_HEATED_BED": {
        "name": "K&H Pet Products Heated Pet Bed",
        "category": "Beds & Furniture",
        "price": 49.99
    },
    "ACCESSORY_ZIPPYPAWS_PLUSH_TOY": {
        "name": "ZippyPaws Plush Squeaker Toy",
        "category": "Dog Toys",
        "price": 7.99
    },
    "ACCESSORY_DOG_GONE_SMART_DOORMAT": {
        "name": "Dog Gone Smart Dirty Dog Doormat",
        "category": "Home & Living",
        "price": 19.99
    },
    "ACCESSORY_RED_DINGO_ID_TAG": {
        "name": "Red Dingo Engraved Pet ID Tag",
        "category": "Accessories/ID Tags",
        "price": 12.99
    },
    "ACCESSORY_HAMILTON_COLLAR": {
        "name": "Hamilton Adjustable Dog Collar",
        "category": "Accessories/Collars",
        "price": 9.99
    },
    "ACCESSORY_FLEXI_RETRACTABLE_LEASH": {
        "name": "Flexi Retractable Dog Leash",
        "category": "Accessories/Leashes",
        "price": 18.99
    },
    "ACCESSORY_HALTI_HEADCOLLAR": {
        "name": "Halti Headcollar for Dogs",
        "category": "Accessories/Training",
        "price": 14.99
    },
    "ACCESSORY_ANDIS_GROOMING_CLIPPER": {
        "name": "Andis UltraEdge Dog Grooming Clipper",
        "category": "Grooming",
        "price": 79.99
    },
    "ACCESSORY_WAHL_GROOMING_CLIPPER": {
        "name": "Wahl Professional Pet Clipper Kit",
        "category": "Grooming",
        "price": 59.99
    },
    "ACCESSORY_FURMINATOR_DESHED_DOG": {
        "name": "FURminator Deshedding Tool for Dogs",
        "category": "Grooming",
        "price": 24.99
    },

    "MISC_PETALIVE_HERBAL_SUPPLEMENT": {
        "name": "PetAlive Herbal Homeopathic Supplement",
        "category": "Supplements",
        "price": 21.99
    },
    "MISC_BURTS_BEES_DOG_SHAMPOO": {
        "name": "Burt’s Bees Oatmeal Shampoo for Dogs",
        "category": "Grooming",
        "price": 9.99
    },
    "MISC_VETS_BEST_SHAMPOO": {
        "name": "Vet’s Best Hypo-Allergenic Shampoo",
        "category": "Grooming/Health",
        "price": 8.99
    },
    "MISC_SENTRY_CALMING_AID": {
        "name": "Sentry Calming Pheromone Spray",
        "category": "Calming Aids",
        "price": 14.99
    },
    "MISC_THUNDERSHIRT_DOG": {
        "name": "ThunderShirt Classic Dog Anxiety Jacket",
        "category": "Calming Apparel",
        "price": 39.99
    },
    "MISC_SERESTO_FLEA_TICK_DOG": {
        "name": "Seresto Flea & Tick Collar for Dogs",
        "category": "Flea & Tick",
        "price": 57.99
    },
    "MISC_ADAMS_FLEA_TICK_SOLUTION": {
        "name": "Adams Flea & Tick Home Spray",
        "category": "Flea & Tick",
        "price": 12.99
    },
    "MISC_ARM_HAMMER_ODOR_REMOVER": {
        "name": "Arm & Hammer Pet Stain & Odor Remover",
        "category": "Cleaning & Odor Control",
        "price": 7.99
    },
    "MISC_NATURES_MIRACLE_STAIN_ODOR": {
        "name": "Nature’s Miracle Stain & Odor Remover",
        "category": "Cleaning & Odor Control",
        "price": 8.99
    },
    "MISC_PLANET_DOG_TOY": {
        "name": "Planet Dog Orbee-Tuff Ball",
        "category": "Dog Toys",
        "price": 11.99
    },
    "MISC_BENEBONE_CHEW_TOY": {
        "name": "Benebone Wishbone Durable Chew Toy",
        "category": "Dog Toys",
        "price": 12.99
    },
    "MISC_ZESTY_PAWS_SUPPLEMENT": {
        "name": "Zesty Paws Multifunctional Supplement",
        "category": "Supplements",
        "price": 26.99
    },
    "MISC_ARK_NATURALS_DENTAL": {
        "name": "Ark Naturals Brushless Toothpaste Chews",
        "category": "Dental Chews",
        "price": 13.99
    },
    "MISC_FRONTLINE_FLEA_TICK": {
        "name": "Frontline Plus Flea & Tick Treatment",
        "category": "Flea & Tick",
        "price": 39.99
    },
    "MISC_ADVANTAGE_FLEA_TICK": {
        "name": "Advantage II Flea Treatment",
        "category": "Flea & Tick",
        "price": 37.99
    },
    "MISC_K9_ADVANTIX_FLEA_TICK": {
        "name": "K9 Advantix II Flea & Tick Treatment",
        "category": "Flea & Tick",
        "price": 42.99
    },
    "MISC_BIO_GROOM_SHAMPOO": {
        "name": "Bio-Groom Pet Shampoo",
        "category": "Grooming",
        "price": 8.99
    },
    
    "DOG_DRY_FOOD_7.7_LBS": {
        "name": "Dog Dry Food 7.7 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 18.99
    },
    "DOG_DRY_FOOD_15.5_LBS": {
        "name": "Dog Dry Food 15.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 29.99
    },
    "DOG_DRY_FOOD_25.5_LBS": {
        "name": "Dog Dry Food 25.5 lbs",
        "category": "Dog Food (Non-Prescription)",
        "price": 45.99
    },
    "CAT_DRY_FOOD_4.4_LBS": {
        "name": "Cat Dry Food 4.4 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 12.99
    },
    "CAT_DRY_FOOD_12.2_LBS": {
        "name": "Cat Dry Food 12.2 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 22.99
    },
    "CAT_DRY_FOOD_19.8_LBS": {
        "name": "Cat Dry Food 19.8 lbs",
        "category": "Cat Food (Non-Prescription)",
        "price": 34.99
    },
    "DOG_CANS_12.5OZ_CASE12": {
        "name": "Dog Canned Food 12.5 oz (Case of 12)",
        "category": "Dog Food (Non-Prescription)",
        "price": 25.99
    },
    "DOG_CANS_12.5OZ_CASE24": {
        "name": "Dog Canned Food 12.5 oz (Case of 24)",
        "category": "Dog Food (Non-Prescription)",
        "price": 47.99
    },
    "CAT_CANS_5.5OZ_CASE24": {
        "name": "Cat Canned Food 5.5 oz (Case of 24)",
        "category": "Cat Food (Non-Prescription)",
        "price": 29.99
    },
    "CAT_CANS_5.5OZ_CASE12": {
        "name": "Cat Canned Food 5.5 oz (Case of 12)",
        "category": "Cat Food (Non-Prescription)",
        "price": 15.99
    },
    "DOG_TREAT_BISCUIT": {
        "name": "Dog Treat - Biscuit",
        "category": "Dog Treats",
        "price": 8.99
    },
    "DOG_TREAT_JERKY": {
        "name": "Dog Treat - Jerky",
        "category": "Dog Treats",
        "price": 12.50
    },
    "DOG_DENTAL_TREAT": {
        "name": "Dog Dental Treat",
        "category": "Dog Treats",
        "price": 14.99
    },
    "CAT_TREAT_CRUNCHY": {
        "name": "Cat Treat - Crunchy",
        "category": "Cat Treats",
        "price": 6.99
    },
    "CAT_TREAT_SOFT": {
        "name": "Cat Treat - Soft",
        "category": "Cat Treats",
        "price": 7.99
    },
    "DOG_COLLAR_LARGE": {
        "name": "Dog Collar - Large",
        "category": "Accessories",
        "price": 9.99
    },
    "DOG_LEASH_DURABLE": {
        "name": "Dog Leash - Durable",
        "category": "Accessories",
        "price": 14.99
    },
    "CAT_HARNESS": {
        "name": "Cat Harness",
        "category": "Accessories",
        "price": 12.99
    },
    "LARGE_DOG_CRATE": {
        "name": "Large Dog Crate",
        "category": "Crates & Kennels",
        "price": 129.99
    },
    "CAT_TREE_DELUXE": {
        "name": "Cat Tree Deluxe",
        "category": "Cat Trees & Towers",
        "price": 179.99
    },
    "HORSE_FEED_BAG": {
        "name": "Horse Feed 50 lbs",
        "category": "Horse & Farm",
        "price": 59.99
    },
    "FRESHWATER_AQUARIUM_50GAL": {
        "name": "Freshwater Aquarium 50 Gallon",
        "category": "Fish & Aquatic Supplies",
        "price": 249.99
    },

    "DOG_RAW_FREEZE_DRIED": {
        "name": "Dog Raw Freeze-Dried Patties",
        "category": "Dog Food (Non-Prescription)",
        "price": 29.99
    },
    "DOG_DEHYDRATED_FOOD": {
        "name": "Dog Dehydrated Food Mix",
        "category": "Dog Food (Non-Prescription)",
        "price": 36.99
    },
    "DOG_FRESH_FOOD_ROLL": {
        "name": "Dog Fresh Food Roll",
        "category": "Dog Food (Non-Prescription)",
        "price": 19.99
    },
    "DOG_FOOD_TOPPER_BONE_BROTH": {
        "name": "Dog Food Topper - Bone Broth",
        "category": "Food Toppers & Meal Enhancers",
        "price": 6.99
    },

    "DOG_TREAT_SOFT_CHEWY": {
        "name": "Dog Treat - Soft & Chewy",
        "category": "Dog Treats",
        "price": 8.49
    },
    "DOG_TREAT_MEAT_STRIPS": {
        "name": "Dog Treat - Meat Strips",
        "category": "Dog Treats",
        "price": 11.49
    },
    "DOG_TREAT_LONG_LASTING_BULLY": {
        "name": "Dog Long-Lasting Bully Stick",
        "category": "Dog Treats",
        "price": 5.99
    },
    "DOG_TREAT_TRAINING_BITES": {
        "name": "Dog Training Treats (Bite-Sized)",
        "category": "Dog Treats",
        "price": 5.49
    },

    "DOG_TOY_PLUSH": {
        "name": "Dog Toy - Plush Squeaker",
        "category": "Dog Toys",
        "price": 7.99
    },
    "DOG_TOY_PUZZLE": {
        "name": "Dog Interactive Puzzle Toy",
        "category": "Dog Toys",
        "price": 14.99
    },
    "DOG_TOY_RUBBER_CHEW": {
        "name": "Dog Chew Toy (Durable Rubber)",
        "category": "Dog Toys",
        "price": 9.99
    },
    "DOG_TOY_FETCH_BALL": {
        "name": "Dog Fetch Ball",
        "category": "Dog Toys",
        "price": 4.99
    },

    "DOG_HARNESS_NOPULL": {
        "name": "Dog Harness - No Pull",
        "category": "Dog Accessories",
        "price": 24.99
    },
    "DOG_ID_TAG_CUSTOM": {
        "name": "Dog ID Tag (Custom Engraving)",
        "category": "Dog Accessories",
        "price": 9.49
    },
    "DOG_COAT_WATERPROOF": {
        "name": "Dog Waterproof Coat",
        "category": "Dog Accessories",
        "price": 29.99
    },
    "DOG_BED_ORTHOPEDIC": {
        "name": "Dog Orthopedic Bed",
        "category": "Dog Accessories",
        "price": 59.99
    },
    "DOG_CAR_SEAT_COVER": {
        "name": "Dog Car Seat Cover",
        "category": "Dog Accessories",
        "price": 34.99
    },
    "DOG_GROOMING_SHAMPOO": {
        "name": "Dog Shampoo - Oatmeal",
        "category": "Grooming",
        "price": 8.99
    },
    "DOG_ENZYME_CLEANER": {
        "name": "Dog Enzyme Cleaner",
        "category": "Cleaning & Potty",
        "price": 10.99
    },
    "DOG_SLOW_FEED_BOWL": {
        "name": "Dog Slow Feed Bowl",
        "category": "Bowls & Feeders",
        "price": 12.99
    },

    "DOG_VITAMIN_JOINT_SUPPORT": {
        "name": "Dog Joint Support Supplement",
        "category": "Dog Health & Wellness",
        "price": 19.99
    },
    "DOG_FLEA_TICK_COLLAR": {
        "name": "Dog Flea & Tick Collar (OTC)",
        "category": "Dog Health & Wellness",
        "price": 24.99
    },
    "DOG_DEWORMER_BASIC": {
        "name": "Dog Dewormer (Broad Spectrum, OTC)",
        "category": "Dog Health & Wellness",
        "price": 14.99
    },
    "DOG_FIRST_AID_SPRAY": {
        "name": "Dog First Aid Antiseptic Spray",
        "category": "Dog Health & Wellness",
        "price": 7.99
    },
    "DOG_DENTAL_RINSE": {
        "name": "Dog Dental Rinse",
        "category": "Dog Health & Wellness",
        "price": 10.99
    },

    "CAT_FOOD_RAW_FREEZE_DRIED": {
        "name": "Cat Raw Freeze-Dried Morsels",
        "category": "Cat Food (Non-Prescription)",
        "price": 21.99
    },
    "CAT_FOOD_DEHYDRATED": {
        "name": "Cat Dehydrated Food Mix",
        "category": "Cat Food (Non-Prescription)",
        "price": 27.99
    },
    "CAT_FOOD_TOPPER_GRAVY": {
        "name": "Cat Food Topper - Savory Gravy",
        "category": "Food Toppers & Meal Enhancers",
        "price": 5.99
    },

    "CAT_TREAT_FREEZEDRIED_SALMON": {
        "name": "Cat Treat - Freeze-Dried Salmon",
        "category": "Cat Treats",
        "price": 8.99
    },
    "CAT_DENTAL_TREAT_GREENIES": {
        "name": "Cat Dental Treat - Greenies",
        "category": "Cat Treats",
        "price": 6.99
    },
    "CAT_GRASS_KIT": {
        "name": "Cat Grass Kit",
        "category": "Cat Treats/Enrichment",
        "price": 4.99
    },

    "CAT_LITTER_CLUMPING_CLAY": {
        "name": "Cat Litter - Clumping Clay",
        "category": "Cat Litter",
        "price": 12.99
    },
    "CAT_LITTER_CRYSTAL": {
        "name": "Cat Litter - Crystal",
        "category": "Cat Litter",
        "price": 16.99
    },
    "CAT_LITTER_BOX_COVERED": {
        "name": "Covered Cat Litter Box",
        "category": "Cat Litter Boxes",
        "price": 29.99
    },
    "CAT_LITTER_BOX_AUTOMATIC": {
        "name": "Automatic Self-Cleaning Litter Box",
        "category": "Cat Litter Boxes",
        "price": 149.99
    },

    "CAT_TOY_WAND_FEATHER": {
        "name": "Cat Interactive Wand - Feather",
        "category": "Cat Toys",
        "price": 6.99
    },
    "CAT_TOY_LASER_POINTER": {
        "name": "Cat Laser Pointer",
        "category": "Cat Toys",
        "price": 4.99
    },
    "CAT_SCRATCH_POST_SISAL": {
        "name": "Cat Scratching Post (Sisal)",
        "category": "Cat Scratchers",
        "price": 15.99
    },
    "CAT_BED_BOLSTER": {
        "name": "Cat Bolster Bed",
        "category": "Cat Beds & Furniture",
        "price": 24.99
    },
    "CAT_GROOMING_BRUSH": {
        "name": "Cat Grooming Brush",
        "category": "Cat Grooming",
        "price": 7.99
    },
    "CAT_WATER_FOUNTAIN": {
        "name": "Cat Water Fountain",
        "category": "Bowls & Fountains",
        "price": 34.99
    },

    "CAT_FLEA_TICK_TOPICAL": {
        "name": "Cat Flea & Tick Topical (OTC)",
        "category": "Cat Health & Wellness",
        "price": 18.99
    },
    "CAT_VITAMIN_HAIRBALL": {
        "name": "Cat Hairball Control Supplement",
        "category": "Cat Health & Wellness",
        "price": 9.99
    },
    "CAT_DENTAL_WATER_ADDITIVE": {
        "name": "Cat Dental Water Additive",
        "category": "Cat Health & Wellness",
        "price": 8.99
    },
    "CAT_EAR_CLEANER": {
        "name": "Cat Ear Cleaner (Antiseptic)",
        "category": "Cat Health & Wellness",
        "price": 6.99
    },

    "RABBIT_FOOD_PELLETS": {
        "name": "Rabbit Food Pellets",
        "category": "Small Pet Food",
        "price": 8.99
    },
    "GUINEA_PIG_FOOD_VITC": {
        "name": "Guinea Pig Food (with Vitamin C)",
        "category": "Small Pet Food",
        "price": 10.99
    },
    "TIMOTHY_HAY_BAG": {
        "name": "Timothy Hay (Small Pets)",
        "category": "Small Pet Food",
        "price": 14.99
    },
    "HAMSTER_BEDDING_PAPER": {
        "name": "Paper-Based Small Pet Bedding",
        "category": "Small Pet Bedding",
        "price": 9.99
    },
    "RABBIT_CAGE_LARGE": {
        "name": "Large Rabbit Cage",
        "category": "Small Pet Habitats",
        "price": 59.99
    },
    "SMALL_PET_WHEEL_PLASTIC": {
        "name": "Hamster/Small Pet Exercise Wheel",
        "category": "Small Pet Accessories",
        "price": 12.99
    },
    "GUINEA_PIG_HIDEOUT": {
        "name": "Guinea Pig Hideout",
        "category": "Small Pet Accessories",
        "price": 9.49
    },
    "CHINCHILLA_DUST_BATH": {
        "name": "Chinchilla Dust Bath",
        "category": "Small Pet Grooming",
        "price": 7.99
    },

    "REPTILE_PELLET_DIET": {
        "name": "Reptile Pellet Diet",
        "category": "Reptile Food",
        "price": 9.99
    },
    "FROZEN_MICE_PACK": {
        "name": "Frozen Mice (5-pack)",
        "category": "Reptile Food",
        "price": 12.99
    },
    "REPTILE_TERRARIUM_40GAL": {
        "name": "Reptile Terrarium 40 Gallon",
        "category": "Reptile Enclosures",
        "price": 129.99
    },
    "REPTILE_HEAT_LAMP": {
        "name": "Reptile Heat Lamp (UVB)",
        "category": "Reptile Heating & Lighting",
        "price": 24.99
    },
    "REPTILE_BARK_SUBSTRATE": {
        "name": "Reptile Bark Substrate",
        "category": "Reptile Substrate",
        "price": 11.99
    },
    "REPTILE_HUMIDITY_FOGGER": {
        "name": "Reptile Fogger/Humidifier",
        "category": "Reptile Water & Humidity",
        "price": 39.99
    },
    "REPTILE_CALCIUM_SUPPLEMENT": {
        "name": "Reptile Calcium Dust",
        "category": "Reptile Health",
        "price": 5.99
    },

    "AQUARIUM_STARTER_KIT_10GAL": {
        "name": "Aquarium Starter Kit - 10 Gallon",
        "category": "Fish & Aquatic Supplies",
        "price": 59.99
    },
    "AQUARIUM_FILTER_HOB": {
        "name": "Hang-On-Back Aquarium Filter",
        "category": "Fish & Aquatic Supplies",
        "price": 29.99
    },
    "WATER_CONDITIONER_DECHLOR": {
        "name": "Aquarium Water Conditioner (Dechlor)",
        "category": "Fish & Aquatic Supplies",
        "price": 5.99
    },
    "FISH_FOOD_FLAKES": {
        "name": "Fish Food - Flakes",
        "category": "Fish Food",
        "price": 4.99
    },
    "FISH_FOOD_FROZEN_BLOODWORMS": {
        "name": "Frozen Bloodworms (Blister Pack)",
        "category": "Fish Food",
        "price": 8.49
    },
    "AQUARIUM_HEATER_100W": {
        "name": "Aquarium Heater 100W",
        "category": "Fish & Aquatic Equipment",
        "price": 19.99
    },
    "AQUARIUM_GRAVEL_VAC": {
        "name": "Aquarium Gravel Vacuum",
        "category": "Fish & Aquatic Maintenance",
        "price": 12.99
    },

    "BIRD_SEED_PARAKEET": {
        "name": "Bird Seed Blend - Parakeet",
        "category": "Bird Food",
        "price": 8.99
    },
    "BIRD_SEED_PARROT": {
        "name": "Bird Seed Blend - Parrot",
        "category": "Bird Food",
        "price": 14.99
    },
    "BIRD_CAGE_MEDIUM": {
        "name": "Medium Bird Cage",
        "category": "Bird Cages",
        "price": 49.99
    },
    "BIRD_TOY_FORAGING": {
        "name": "Bird Foraging Toy",
        "category": "Bird Toys",
        "price": 8.99
    },
    "CUTTLEBONE_CALCIUM": {
        "name": "Bird Cuttlebone (Calcium)",
        "category": "Bird Health & Grooming",
        "price": 3.99
    },
    "CHICKEN_COOP_SMALL": {
        "name": "Small Chicken Coop",
        "category": "Chicken & Poultry Supplies",
        "price": 199.99
    },
    "LAYER_FEED_25LB": {
        "name": "Layer Feed 25 lbs (Chickens)",
        "category": "Chicken & Poultry Supplies",
        "price": 16.99
    },

    "HORSE_FEED_SENIOR": {
        "name": "Horse Feed (Senior)",
        "category": "Horse & Farm",
        "price": 24.99
    },
    "HORSE_TREAT_APPLE": {
        "name": "Horse Treat - Apple Crunch",
        "category": "Horse & Farm",
        "price": 9.99
    },
    "HORSE_GROOMING_BRUSH_SET": {
        "name": "Horse Grooming Brush Set",
        "category": "Horse Care",
        "price": 29.99
    },
    "HORSE_FLY_SPRAY": {
        "name": "Horse Fly Spray",
        "category": "Horse Care",
        "price": 14.99
    },
    "GOAT_FEED_20LB": {
        "name": "Goat Feed 20 lbs",
        "category": "Farm Animal Feed",
        "price": 12.99
    },
    "PIG_FEED_25LB": {
        "name": "Pig Feed 25 lbs",
        "category": "Farm Animal Feed",
        "price": 17.99
    },

    "PET_GATE_INDOOR": {
        "name": "Indoor Pet Gate",
        "category": "Gates & Playpens",
        "price": 39.99
    },
    "PET_CLEANING_ODOR_REMOVER": {
        "name": "Pet Stain & Odor Remover",
        "category": "Cleaning & Odor Control",
        "price": 8.99
    },
    "PET_CALMING_DIFFUSER": {
        "name": "Pet Calming Pheromone Diffuser",
        "category": "Training & Behavior",
        "price": 22.99
    },
    "PET_CAMERA_WIFI": {
        "name": "WiFi Pet Camera",
        "category": "Pet Tech",
        "price": 129.99
    },
    "TRAINING_CLICKER": {
        "name": "Training Clicker",
        "category": "Training & Behavior",
        "price": 2.99
    },

    "WILD_BIRD_SEED_10LB": {
        "name": "Wild Bird Seed 10 lbs",
        "category": "Wild Bird Supplies",
        "price": 8.99
    },
    "BEEKEEPING_STARTER_KIT": {
        "name": "Beekeeping Starter Kit",
        "category": "Beekeeping Supplies",
        "price": 79.99
    },

    "HILLS_DOG_CD": {
        "name": "Hill’s Prescription Diet c/d Urinary Care (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 49.99
    },
    "HILLS_DOG_DD": {
        "name": "Hill’s Prescription Diet d/d Skin/Food Sensitivities (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 52.99
    },
    "HILLS_DOG_GD": {
        "name": "Hill’s Prescription Diet g/d Aging Care (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 54.99
    },
    "HILLS_DOG_HD": {
        "name": "Hill’s Prescription Diet h/d Heart Care (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 59.99
    },
    "HILLS_DOG_ID": {
        "name": "Hill’s Prescription Diet i/d Digestive Care (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 48.99
    },
    "HILLS_DOG_JD": {
        "name": "Hill’s Prescription Diet j/d Joint Care (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 62.99
    },
    "HILLS_DOG_KD": {
        "name": "Hill’s Prescription Diet k/d Kidney Care (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 55.99
    },
    "HILLS_DOG_LD": {
        "name": "Hill’s Prescription Diet l/d Liver Care (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 57.99
    },
    "HILLS_DOG_METABOLIC": {
        "name": "Hill’s Prescription Diet Metabolic Weight Management (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 63.99
    },
    "HILLS_DOG_RD": {
        "name": "Hill’s Prescription Diet r/d Weight Reduction (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 49.99
    },
    "HILLS_DOG_SD": {
        "name": "Hill’s Prescription Diet s/d Urinary Care (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 51.99
    },
    "HILLS_DOG_TD": {
        "name": "Hill’s Prescription Diet t/d Dental Care (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 58.99
    },
    "HILLS_DOG_UD": {
        "name": "Hill’s Prescription Diet u/d Urinary Care (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 59.99
    },
    "HILLS_DOG_WD": {
        "name": "Hill’s Prescription Diet w/d Digestive/Weight/Glucose (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 58.99
    },
    "HILLS_DOG_ZD": {
        "name": "Hill’s Prescription Diet z/d Food Sensitivities (Dog)",
        "category": "Hill's Prescription Diet (Dog)",
        "price": 64.99
    },

    "HILLS_CAT_CD": {
        "name": "Hill’s Prescription Diet c/d Urinary Care (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 39.99
    },
    "HILLS_CAT_DD": {
        "name": "Hill’s Prescription Diet d/d Skin/Food Sensitivities (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 42.99
    },
    "HILLS_CAT_GD": {
        "name": "Hill’s Prescription Diet g/d Aging Care (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 44.99
    },
    "HILLS_CAT_ID": {
        "name": "Hill’s Prescription Diet i/d Digestive Care (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 38.99
    },
    "HILLS_CAT_JD": {
        "name": "Hill’s Prescription Diet j/d Joint Care (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 46.99
    },
    "HILLS_CAT_KD": {
        "name": "Hill’s Prescription Diet k/d Kidney Care (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 41.99
    },
    "HILLS_CAT_LD": {
        "name": "Hill’s Prescription Diet l/d Liver Care (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 43.99
    },
    "HILLS_CAT_MD": {
        "name": "Hill’s Prescription Diet m/d Glucose/Weight Management (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 45.99
    },
    "HILLS_CAT_RD": {
        "name": "Hill’s Prescription Diet r/d Weight Reduction (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 39.99
    },
    "HILLS_CAT_SD": {
        "name": "Hill’s Prescription Diet s/d Urinary Care (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 41.99
    },
    "HILLS_CAT_TD": {
        "name": "Hill’s Prescription Diet t/d Dental Care (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 46.99
    },
    "HILLS_CAT_WD": {
        "name": "Hill’s Prescription Diet w/d Digestive/Weight/Glucose (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 44.99
    },
    "HILLS_CAT_YD": {
        "name": "Hill’s Prescription Diet y/d Thyroid Care (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 52.99
    },
    "HILLS_CAT_ZD": {
        "name": "Hill’s Prescription Diet z/d Food Sensitivities (Cat)",
        "category": "Hill's Prescription Diet (Cat)",
        "price": 49.99
    },

    "RC_DOG_HYDROLYZED_HP": {
        "name": "Royal Canin Veterinary Diet Hydrolyzed Protein (Dog)",
        "category": "Royal Canin Veterinary Diet (Dog)",
        "price": 59.99
    },
    "RC_DOG_ULTAMINO": {
        "name": "Royal Canin Veterinary Diet Ultamino (Dog)",
        "category": "Royal Canin Veterinary Diet (Dog)",
        "price": 69.99
    },
    "RC_DOG_SELECTED_PROTEIN_PD": {
        "name": "Royal Canin Veterinary Diet Selected Protein PD (Dog)",
        "category": "Royal Canin Veterinary Diet (Dog)",
        "price": 64.99
    },
    "RC_DOG_URINARY_SO": {
        "name": "Royal Canin Veterinary Diet Urinary SO (Dog)",
        "category": "Royal Canin Veterinary Diet (Dog)",
        "price": 58.99
    },
    "RC_DOG_GASTROINTESTINAL": {
        "name": "Royal Canin Veterinary Diet Gastrointestinal (Dog)",
        "category": "Royal Canin Veterinary Diet (Dog)",
        "price": 57.99
    },
    "RC_DOG_SATIETY": {
        "name": "Royal Canin Veterinary Diet Satiety Support (Dog)",
        "category": "Royal Canin Veterinary Diet (Dog)",
        "price": 62.99
    },
    "RC_DOG_RENAL_SUPPORT": {
        "name": "Royal Canin Veterinary Diet Renal Support (Dog)",
        "category": "Royal Canin Veterinary Diet (Dog)",
        "price": 66.99
    },
    "RC_DOG_HEPATIC": {
        "name": "Royal Canin Veterinary Diet Hepatic (Dog)",
        "category": "Royal Canin Veterinary Diet (Dog)",
        "price": 61.99
    },
    "RC_DOG_DIABETIC": {
        "name": "Royal Canin Veterinary Diet Diabetic (Dog)",
        "category": "Royal Canin Veterinary Diet (Dog)",
        "price": 63.99
    },
    "RC_DOG_CALM": {
        "name": "Royal Canin Veterinary Diet Calm (Dog)",
        "category": "Royal Canin Veterinary Diet (Dog)",
        "price": 67.99
    },

    "RC_CAT_HYDROLYZED_HP": {
        "name": "Royal Canin Veterinary Diet Hydrolyzed Protein (Cat)",
        "category": "Royal Canin Veterinary Diet (Cat)",
        "price": 49.99
    },
    "RC_CAT_ULTAMINO": {
        "name": "Royal Canin Veterinary Diet Ultamino (Cat)",
        "category": "Royal Canin Veterinary Diet (Cat)",
        "price": 59.99
    },
    "RC_CAT_SELECTED_PROTEIN_PR": {
        "name": "Royal Canin Veterinary Diet Selected Protein PR (Cat)",
        "category": "Royal Canin Veterinary Diet (Cat)",
        "price": 54.99
    },
    "RC_CAT_URINARY_SO": {
        "name": "Royal Canin Veterinary Diet Urinary SO (Cat)",
        "category": "Royal Canin Veterinary Diet (Cat)",
        "price": 44.99
    },
    "RC_CAT_GASTROINTESTINAL": {
        "name": "Royal Canin Veterinary Diet Gastrointestinal (Cat)",
        "category": "Royal Canin Veterinary Diet (Cat)",
        "price": 43.99
    },
    "RC_CAT_RENAL_SUPPORT": {
        "name": "Royal Canin Veterinary Diet Renal Support (Cat)",
        "category": "Royal Canin Veterinary Diet (Cat)",
        "price": 56.99
    },
    "RC_CAT_HEPATIC": {
        "name": "Royal Canin Veterinary Diet Hepatic (Cat)",
        "category": "Royal Canin Veterinary Diet (Cat)",
        "price": 49.99
    },
    "RC_CAT_DIABETIC": {
        "name": "Royal Canin Veterinary Diet Diabetic (Cat)",
        "category": "Royal Canin Veterinary Diet (Cat)",
        "price": 48.99
    },
    "RC_CAT_SATIETY": {
        "name": "Royal Canin Veterinary Diet Satiety (Cat)",
        "category": "Royal Canin Veterinary Diet (Cat)",
        "price": 54.99
    },
    "RC_CAT_CALM": {
        "name": "Royal Canin Veterinary Diet Calm (Cat)",
        "category": "Royal Canin Veterinary Diet (Cat)",
        "price": 58.99
    },

    "PURINA_DOG_EN": {
        "name": "Purina Pro Plan Vet Diet EN Gastroenteric (Dog)",
        "category": "Purina Veterinary Diet (Dog)",
        "price": 49.99
    },
    "PURINA_DOG_HA": {
        "name": "Purina Pro Plan Vet Diet HA Hydrolyzed (Dog)",
        "category": "Purina Veterinary Diet (Dog)",
        "price": 52.99
    },
    "PURINA_DOG_EL_ELEMENTAL": {
        "name": "Purina Pro Plan Vet Diet EL Elemental (Dog)",
        "category": "Purina Veterinary Diet (Dog)",
        "price": 58.99
    },
    "PURINA_DOG_NC_NEUROCARE": {
        "name": "Purina Pro Plan Vet Diet NC NeuroCare (Dog)",
        "category": "Purina Veterinary Diet (Dog)",
        "price": 64.99
    },
    "PURINA_DOG_JM": {
        "name": "Purina Pro Plan Vet Diet JM Joint Mobility (Dog)",
        "category": "Purina Veterinary Diet (Dog)",
        "price": 56.99
    },
    "PURINA_DOG_OM": {
        "name": "Purina Pro Plan Vet Diet OM Overweight Management (Dog)",
        "category": "Purina Veterinary Diet (Dog)",
        "price": 49.99
    },
    "PURINA_DOG_DH": {
        "name": "Purina Pro Plan Vet Diet DH Dental Health (Dog)",
        "category": "Purina Veterinary Diet (Dog)",
        "price": 48.99
    },
    "PURINA_DOG_UR": {
        "name": "Purina Pro Plan Vet Diet UR Urinary (Dog)",
        "category": "Purina Veterinary Diet (Dog)",
        "price": 54.99
    },
    "PURINA_DOG_DRM": {
        "name": "Purina Pro Plan Vet Diet DRM Dermatologic (Dog)",
        "category": "Purina Veterinary Diet (Dog)",
        "price": 59.99
    },
    "PURINA_DOG_NF": {
        "name": "Purina Pro Plan Vet Diet NF Kidney Function (Dog)",
        "category": "Purina Veterinary Diet (Dog)",
        "price": 62.99
    },

    "PURINA_CAT_EN": {
        "name": "Purina Pro Plan Vet Diet EN Gastroenteric (Cat)",
        "category": "Purina Veterinary Diet (Cat)",
        "price": 39.99
    },
    "PURINA_CAT_HA": {
        "name": "Purina Pro Plan Vet Diet HA Hydrolyzed (Cat)",
        "category": "Purina Veterinary Diet (Cat)",
        "price": 42.99
    },
    "PURINA_CAT_OM": {
        "name": "Purina Pro Plan Vet Diet OM Overweight Management (Cat)",
        "category": "Purina Veterinary Diet (Cat)",
        "price": 38.99
    },
    "PURINA_CAT_DM": {
        "name": "Purina Pro Plan Vet Diet DM Dietetic Management (Cat)",
        "category": "Purina Veterinary Diet (Cat)",
        "price": 44.99
    },
    "PURINA_CAT_UR": {
        "name": "Purina Pro Plan Vet Diet UR Urinary (Cat)",
        "category": "Purina Veterinary Diet (Cat)",
        "price": 42.99
    },
    "PURINA_CAT_NF": {
        "name": "Purina Pro Plan Vet Diet NF Kidney Function (Cat)",
        "category": "Purina Veterinary Diet (Cat)",
        "price": 49.99
    },
    "PURINA_CAT_DH": {
        "name": "Purina Pro Plan Vet Diet DH Dental Health (Cat)",
        "category": "Purina Veterinary Diet (Cat)",
        "price": 38.99
    },
    "PURINA_CAT_CN": {
        "name": "Purina Pro Plan Vet Diet CN Convalescence (Cat)",
        "category": "Purina Veterinary Diet (Cat)",
        "price": 46.99
    },

    "BLUE_DOG_HF": {
        "name": "Blue Buffalo Vet Diet HF Hydrolyzed (Dog)",
        "category": "Blue Buffalo Vet Diet (Dog)",
        "price": 54.99
    },
    "BLUE_DOG_GI": {
        "name": "Blue Buffalo Vet Diet GI Gastrointestinal (Dog)",
        "category": "Blue Buffalo Vet Diet (Dog)",
        "price": 49.99
    },
    "BLUE_DOG_KM": {
        "name": "Blue Buffalo Vet Diet KM Kidney + Mobility (Dog)",
        "category": "Blue Buffalo Vet Diet (Dog)",
        "price": 58.99
    },
    "BLUE_DOG_NP": {
        "name": "Blue Buffalo Vet Diet NP Novel Protein (Dog)",
        "category": "Blue Buffalo Vet Diet (Dog)",
        "price": 62.99
    },
    "BLUE_DOG_WU": {
        "name": "Blue Buffalo Vet Diet WU Weight + Urinary (Dog)",
        "category": "Blue Buffalo Vet Diet (Dog)",
        "price": 57.99
    },

    "BLUE_CAT_HF": {
        "name": "Blue Buffalo Vet Diet HF Hydrolyzed (Cat)",
        "category": "Blue Buffalo Vet Diet (Cat)",
        "price": 44.99
    },
    "BLUE_CAT_GI": {
        "name": "Blue Buffalo Vet Diet GI Gastrointestinal (Cat)",
        "category": "Blue Buffalo Vet Diet (Cat)",
        "price": 39.99
    },
    "BLUE_CAT_KM": {
        "name": "Blue Buffalo Vet Diet KM Kidney + Mobility (Cat)",
        "category": "Blue Buffalo Vet Diet (Cat)",
        "price": 48.99
    },
    "BLUE_CAT_NP": {
        "name": "Blue Buffalo Vet Diet NP Novel Protein (Cat)",
        "category": "Blue Buffalo Vet Diet (Cat)",
        "price": 52.99
    },
    "BLUE_CAT_WU": {
        "name": "Blue Buffalo Vet Diet WU Weight + Urinary (Cat)",
        "category": "Blue Buffalo Vet Diet (Cat)",
        "price": 47.99
    }
}

DOG_DRY_VARIANTS = [
    ("7.7_LBS", 39.99),
    ("15.5_LBS", 59.99),
    ("25.5_LBS", 79.99)
]
DOG_CAN_VARIANTS = [
    ("12.5OZ_CASE12", 39.99),
    ("12.5OZ_CASE24", 74.99)
]

CAT_DRY_VARIANTS = [
    ("4.4_LBS", 29.99),
    ("12.2_LBS", 49.99),
    ("19.8_LBS", 64.99)
]
CAT_CAN_VARIANTS = [
    ("5.5OZ_CASE12", 21.99),
    ("5.5OZ_CASE24", 39.99)
]

dog_prescription_keys = []
cat_prescription_keys = []
for sku_key, details in PRODUCT_CATALOG.items():
    if "Prescription Diet" in details["category"] or "Veterinary Diet" in details["category"]:
        if "_DOG_" in sku_key:
            dog_prescription_keys.append(sku_key)
        elif "_CAT_" in sku_key:
            cat_prescription_keys.append(sku_key)

for base_key in dog_prescription_keys:
    base_info = PRODUCT_CATALOG[base_key]
    base_name = base_info["name"]
    base_category = base_info["category"]

    for (suffix, price) in DOG_DRY_VARIANTS:
        new_sku = f"{base_key}_{suffix}"
        PRODUCT_CATALOG[new_sku] = {
            "name": f"{base_name} - Dry {suffix.replace('_', ' ')}",
            "category": base_category,
            "price": price
        }

    for (suffix, price) in DOG_CAN_VARIANTS:
        new_sku = f"{base_key}_CANS_{suffix}"
        PRODUCT_CATALOG[new_sku] = {
            "name": f"{base_name} - Canned {suffix.replace('_', ' ')}",
            "category": base_category,
            "price": price
        }

for base_key in cat_prescription_keys:
    base_info = PRODUCT_CATALOG[base_key]
    base_name = base_info["name"]
    base_category = base_info["category"]

    for (suffix, price) in CAT_DRY_VARIANTS:
        new_sku = f"{base_key}_{suffix}"
        PRODUCT_CATALOG[new_sku] = {
            "name": f"{base_name} - Dry {suffix.replace('_', ' ')}",
            "category": base_category,
            "price": price
        }

    for (suffix, price) in CAT_CAN_VARIANTS:
        new_sku = f"{base_key}_CANS_{suffix}"
        PRODUCT_CATALOG[new_sku] = {
            "name": f"{base_name} - Canned {suffix.replace('_', ' ')}",
            "category": base_category,
            "price": price
        }

class Product:
    def __init__(self, name, category, price, stock):
        self.product_id = str(uuid.uuid4())
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock
        self.out_of_stock = False

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "category": self.category,
            "price": self.price,
            "stock": self.stock,
            "out_of_stock": self.out_of_stock
        }

    @classmethod
    def from_dict(cls, data):
        """Helper to reconstruct a Product from a dict."""
        obj = cls(
            name=data["name"],
            category=data["category"],
            price=data["price"],
            stock=data["stock"]
        )
        obj.product_id = data["product_id"]
        obj.out_of_stock = data.get("out_of_stock", False)
        return obj


class Customer:
    def __init__(self, name, email, phone, address, city, state, zipcode):
        self.customer_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def to_dict(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode
        }

    @classmethod
    def from_dict(cls, data):
        """Helper to reconstruct a Customer from a dict."""
        obj = cls(
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            address=data["address"],
            city=data["city"],
            state=data["state"],
            zipcode=data["zipcode"]
        )
        obj.customer_id = data["customer_id"]
        return obj


class Address:
    """Separate Billing vs. Shipping Address."""
    def __init__(self, street, city, state, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def to_dict(self):
        return {
            "street": self.street,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            street=data["street"],
            city=data["city"],
            state=data["state"],
            zipcode=data["zipcode"]
        )


class OrderItem:
    """
    Represents one line-item in an order (which product and how many).
    """
    def __init__(self, product, quantity, free_qty=0):
        self.product = product
        self.quantity = quantity
        self.free_qty = free_qty

    def to_dict(self):
        return {
            "product": self.product.to_dict(),
            "quantity": self.quantity,
            "free_qty": self.free_qty
        }

    @classmethod
    def from_dict(cls, data):
        product_obj = Product.from_dict(data["product"])
        return cls(
            product=product_obj,
            quantity=data["quantity"],
            free_qty=data.get("free_qty", 0)
        )


class ShipmentRecord:
    """
    Represents a single shipment. Partial shipments or multiple shipments may occur.
    """
    def __init__(self, items, tracking_number=None, shipment_status="Pending"):
        self.shipment_id = str(uuid.uuid4())
        self.items = items
        self.tracking_number = tracking_number
        self.shipment_status = shipment_status
        self.shipment_timestamp = None

    def to_dict(self):
        return {
            "shipment_id": self.shipment_id,
            "items": [i.to_dict() for i in self.items],
            "tracking_number": self.tracking_number,
            "shipment_status": self.shipment_status,
            "shipment_timestamp": self.shipment_timestamp
        }

    @classmethod
    def from_dict(cls, data):
        items = [OrderItem.from_dict(x) for x in data["items"]]
        obj = cls(
            items=items,
            tracking_number=data["tracking_number"],
            shipment_status=data["shipment_status"]
        )
        obj.shipment_id = data["shipment_id"]
        obj.shipment_timestamp = data.get("shipment_timestamp")
        return obj


class OrderStatusHistory:
    """
    Records each status change with a timestamp for deeper analytics.
    """
    def __init__(self, status, timestamp=None):
        self.status_id = str(uuid.uuid4())
        self.status = status
        self.timestamp = timestamp or datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    def to_dict(self):
        return {
            "status_id": self.status_id,
            "status": self.status,
            "timestamp": self.timestamp
        }

    @classmethod
    def from_dict(cls, data):
        obj = cls(
            status=data["status"],
            timestamp=data["timestamp"]
        )
        obj.status_id = data["status_id"]
        return obj


class Order:
    def __init__(
            self,
            customer,
            line_items,
            payment_info,
            pet_name,
            shipping_address=None,
            billing_address=None,
            coupon_codes=None,
            shipping_speed=None,
            shipping_cost=0.0,
            fulfillment_center=None,
            timestamp=None,
            shipping_status=None,
            expected_delivery_date=None,
            delivery_date=None,
            refunded="no",
            delivered="no",
            payment_status="authorized",
            payment_method="credit_card",
            partial_refund_amount=0.0,
            tax_rate=0.0,
            tax_amount=0.0,
            env_fee=0.0,
            currency="USD",
            exchange_rate=1.0,
            loyalty_points_used=0,
            loyalty_tier="None",
            risk_score=0,
            fraud_flag=False,
            subscription_id=None,
            subscription_frequency=None
    ):
        self.order_id = str(uuid.uuid4())
        self.customer = customer
        self.line_items = line_items
        self.payment_info = payment_info
        self.pet_name = pet_name

        self.shipping_address = shipping_address
        self.billing_address = billing_address

        self.timestamp = (
            timestamp
            or datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        )
        self.shipping_status = shipping_status or "Pending"
        self.expected_delivery_date = expected_delivery_date
        self.delivery_date = delivery_date
        self.refunded = refunded
        self.delivered = delivered

        self.payment_status = payment_status
        self.payment_method = payment_method
        self.partial_refund_amount = partial_refund_amount

        if coupon_codes is None:
            coupon_codes = []
        self.coupon_codes = coupon_codes

        self.shipping_speed = shipping_speed
        self.shipping_cost = shipping_cost
        self.fulfillment_center = fulfillment_center

        self.tax_rate = tax_rate
        self.tax_amount = tax_amount
        self.env_fee = env_fee

        self.currency = currency
        self.exchange_rate = exchange_rate

        self.loyalty_points_used = loyalty_points_used
        self.loyalty_tier = loyalty_tier
        self.risk_score = risk_score
        self.fraud_flag = fraud_flag

        self.subscription_id = subscription_id
        self.subscription_frequency = subscription_frequency

        self.shipments = []

        self.status_history = [
            OrderStatusHistory(self.shipping_status).to_dict()
        ]

        self.tracking_number = None
        self.shipping_provider = None

        self.subtotal_before_promos = 0.0
        for item in self.line_items:
            self.subtotal_before_promos += (item.product.price * item.quantity)

        self.apply_b2g1_promos()

        self.subtotal_after_coupon = self.apply_coupons()

        if "FREESHIP" in self.coupon_codes:
            self.shipping_cost = 0.0

        self.order_total = round(
            self.subtotal_after_coupon + self.shipping_cost + self.env_fee + self.tax_amount,
            2
        )

    def apply_b2g1_promos(self):
        """
        Apply "Buy X, get Y free" logic if product is in B2G1_PROMOS.
        Actually sets free_qty on the line item.
        """
        for item in self.line_items:
            sku_match = None
            for promo_sku, (buy_x, get_y) in B2G1_PROMOS.items():
                if promo_sku in item.product.name.replace(" ", "_").upper():
                    sku_match = (buy_x, get_y)
                    break
            if sku_match:
                buy_x, get_y = sku_match
                free_qty = (item.quantity // buy_x) * get_y
                item.free_qty = free_qty

    def apply_coupons(self):
        """
        Subtract discounts from each valid coupon.
        Return the updated subtotal after discount(s).
        """
        current_subtotal = self.subtotal_before_promos

        for ccode in self.coupon_codes:
            cinfo = COUPON_DETAILS.get(ccode)
            if not cinfo:
                continue
            if COUPON_USAGE[ccode] >= cinfo["usage_limit"]:
                continue

            disc_rate = cinfo["discount"]
            discount_amt = disc_rate * current_subtotal
            current_subtotal -= discount_amt
            COUPON_USAGE[ccode] += 1

            if not cinfo["stackable"]:
                break

        return round(current_subtotal, 2)

    def to_dict(self):
        line_items_list = [item.to_dict() for item in self.line_items]
        return {
            "order_id": self.order_id,
            "customer": self.customer.to_dict(),
            "line_items": line_items_list,
            "subtotal_before_promos": round(self.subtotal_before_promos, 2),
            "subtotal_after_coupon": self.subtotal_after_coupon,
            "shipping_cost": self.shipping_cost,
            "env_fee": self.env_fee,
            "tax_rate": self.tax_rate,
            "tax_amount": self.tax_amount,
            "order_total": self.order_total,
            "payment_info": self.payment_info,
            "pet_name": self.pet_name,
            "timestamp": self.timestamp,
            "shipping_status": self.shipping_status,
            "expected_delivery_date": self.expected_delivery_date,
            "delivery_date": self.delivery_date,
            "refunded": self.refunded,
            "delivered": self.delivered,
            "payment_status": self.payment_status,
            "payment_method": self.payment_method,
            "partial_refund_amount": self.partial_refund_amount,
            "coupon_codes": self.coupon_codes,
            "fulfillment_center": self.fulfillment_center,
            "shipping_speed": self.shipping_speed,
            "currency": self.currency,
            "exchange_rate": self.exchange_rate,
            "loyalty_points_used": self.loyalty_points_used,
            "loyalty_tier": self.loyalty_tier,
            "risk_score": self.risk_score,
            "fraud_flag": self.fraud_flag,
            "subscription_id": self.subscription_id,
            "subscription_frequency": self.subscription_frequency,
            "shipments": [s.to_dict() for s in self.shipments],
            "status_history": self.status_history,
            "tracking_number": self.tracking_number,
            "shipping_provider": self.shipping_provider,
            "shipping_address": self.shipping_address.to_dict() if self.shipping_address else None,
            "billing_address": self.billing_address.to_dict() if self.billing_address else None
        }

    @classmethod
    def from_dict(cls, data):
        cust = Customer.from_dict(data["customer"])
        items = [OrderItem.from_dict(i) for i in data["line_items"]]

        shipping_addr = None
        if data.get("shipping_address"):
            shipping_addr = Address.from_dict(data["shipping_address"])

        billing_addr = None
        if data.get("billing_address"):
            billing_addr = Address.from_dict(data["billing_address"])

        shipments_list = []
        if "shipments" in data:
            for sdict in data["shipments"]:
                shipments_list.append(ShipmentRecord.from_dict(sdict))

        obj = cls(
            customer=cust,
            line_items=items,
            payment_info=data["payment_info"],
            pet_name=data["pet_name"],
            shipping_address=shipping_addr,
            billing_address=billing_addr,
            coupon_codes=data.get("coupon_codes", []),
            shipping_speed=data.get("shipping_speed"),
            shipping_cost=data.get("shipping_cost", 0.0),
            fulfillment_center=data.get("fulfillment_center"),
            timestamp=data.get("timestamp"),
            shipping_status=data.get("shipping_status", "Pending"),
            expected_delivery_date=data.get("expected_delivery_date"),
            delivery_date=data.get("delivery_date"),
            refunded=data.get("refunded", "no"),
            delivered=data.get("delivered", "no"),
            payment_status=data.get("payment_status", "authorized"),
            payment_method=data.get("payment_method", "credit_card"),
            partial_refund_amount=data.get("partial_refund_amount", 0.0),
            tax_rate=data.get("tax_rate", 0.0),
            tax_amount=data.get("tax_amount", 0.0),
            env_fee=data.get("env_fee", 0.0),
            currency=data.get("currency", "USD"),
            exchange_rate=data.get("exchange_rate", 1.0),
            loyalty_points_used=data.get("loyalty_points_used", 0),
            loyalty_tier=data.get("loyalty_tier", "None"),
            risk_score=data.get("risk_score", 0),
            fraud_flag=data.get("fraud_flag", False),
            subscription_id=data.get("subscription_id"),
            subscription_frequency=data.get("subscription_frequency")
        )
        obj.order_id = data["order_id"]
        obj.status_history = data.get("status_history", [])
        obj.tracking_number = data.get("tracking_number")
        obj.shipping_provider = data.get("shipping_provider")
        obj.shipments = shipments_list
        return obj


class Review:
    """
    Placeholder for a possible "reviews" table/relationship.
    You'd store references like: review.customer_id, review.product_id, rating, etc.
    """
    def __init__(self, customer_id, product_id, rating, comment=""):
        self.review_id = str(uuid.uuid4())
        self.customer_id = customer_id
        self.product_id = product_id
        self.rating = rating
        self.comment = comment


class FakeEcommerceDataGenerator:
    """
    Generates realistic e-commerce data: Products, Customers, Orders,
    with sequential timestamps on the SAME DAY for all records.
    """

    def __init__(self):
        self.generated_emails = set()
        self.shipping_providers = ["FedEx", "UPS", "USPS", "DHL"]
        self.generated_tracking_numbers = set() 

        self.ny_tz = pytz.timezone("America/New_York")

    def _generate_tracking_number(self, length: int = 12) -> str:
        """
        Returns a unique, carrier‑style tracking number (A‑Z / 0‑9).
        """
        while True:
            code = "".join(random.choices(string.ascii_uppercase + string.digits, k=length))
            if code not in self.generated_tracking_numbers:
                self.generated_tracking_numbers.add(code)
                return code
            
    def _get_next_timestamp_str(self):
        """
        Returns the current timestamp in the desired "YYYY-MM-DD HH:MM:SS.xxx" format,
        then increments it by 1 second.
        """
        now = datetime.now(self.ny_tz)
        return now.strftime("%Y-%m-%dT%H:%M:%S.%f")
            
    def generate_unique_email(self):
        """Generate unique emails by checking in a set."""
        while True:
            candidate = fake.ascii_email()
            if candidate not in self.generated_emails:
                self.generated_emails.add(candidate)
                return candidate

    def generate_customer(self):
        city, state, zipcode, area_code = USZipcodeLocationData.get_random_location()
        name = fake.name()
        address = fake.street_address()
        phone = f"{area_code}-{random.randint(100,999)}-{random.randint(1000,9999)}"
        email = self.generate_unique_email()
        return Customer(name, email, phone, address, city, state, zipcode)

    def generate_address(self):
        """Generate a random address (used for shipping or billing)."""
        city, state, zipcode, _ = USZipcodeLocationData.get_random_location()
        street = fake.street_address()
        return Address(street, city, state, zipcode)

    def generate_payment_info(self):
        """
        Randomly generate either a masked credit card
        or an email (for something like PayPal).
        """
        if random.random() < 0.5:
            return "4443" + "x" * 8 + "0092"
        else:
            random_prefix = fake.user_name()
            random_domain = fake.domain_name()
            return f"{random_prefix}@{random_domain}"

    def generate_coupon_codes(self):
        """
        Potentially return multiple coupon codes, respecting some random logic.
        """
        possible = list(COUPON_DETAILS.keys())
        random.shuffle(possible)
        num = random.randint(0, 2)
        return possible[:num]

    def generate_pet_name(self):
        return fake.first_name()

    def generate_loyalty_tier(self):
        return random.choice(["None", "Silver", "Gold", "Platinum"])

    def generate_risk_score(self, shipping_address, billing_address):
        """
        Slightly increase risk if shipping vs. billing address differ widely.
        """
        risk = random.randint(0, 100)
        if shipping_address and billing_address:
            if shipping_address.city != billing_address.city:
                risk += 10
        return min(risk, 100)

    def generate_partial_shipments(self, order_items):
        """
        Create partial shipments if some items are out of stock or to simulate multi-ship scenarios.
        """
        shipments = []
        random.shuffle(order_items)

        num_shipments = 1 if random.random() < 0.5 else 2

        if num_shipments == 1:
            shipments.append(ShipmentRecord(items=order_items))
        else:
            mid_point = len(order_items) // 2
            first_list = order_items[:mid_point]
            second_list = order_items[mid_point:]
            shipments.append(ShipmentRecord(items=first_list))
            if second_list:
                shipments.append(ShipmentRecord(items=second_list))

        return shipments

    def decrement_stock(self, product, qty):
        product.stock -= qty
        if product.stock < 0:
            product.out_of_stock = True

    def generate_customer_info(self):
        """
        Generates one unique random Customer object.
        This ensures the same customer object can be reused
        for both orders and clickstream events if needed.
        """
        return self.generate_customer()

    def generate_order(self, customer=None):
        """
        Generates a single random Order with a *current* timestamp
        in America/New_York, so all are from "today" in ascending time.
        """
        if customer is None:
            customer = self.generate_customer()

        shipping_addr = self.generate_address()
        if random.random() < 0.8:
            billing_addr = shipping_addr
        else:
            billing_addr = self.generate_address()

        num_items = random.randint(1, 15)
        line_items = []
        catalog_keys = list(PRODUCT_CATALOG.keys())

        for _ in range(num_items):
            sku = random.choice(catalog_keys)
            product_data = PRODUCT_CATALOG[sku]
            stock_amt = random.randint(1, 100)
            prod_obj = Product(
                name=product_data["name"],
                category=product_data["category"],
                price=product_data["price"],
                stock=stock_amt
            )
            quantity = random.randint(1, 4)

            if (stock_amt - quantity) < 0:
                partial_qty = max(0, stock_amt)
                item = OrderItem(prod_obj, partial_qty)
                self.decrement_stock(prod_obj, partial_qty)
            else:
                item = OrderItem(prod_obj, quantity)
                self.decrement_stock(prod_obj, quantity)

            line_items.append(item)

        payment_info = self.generate_payment_info()
        coupon_codes = self.generate_coupon_codes()
        pet_name = self.generate_pet_name()

        possible_methods = ["credit_card", "PayPal", "bank_transfer", "buy_now_pay_later"]
        payment_method = random.choice(possible_methods)

        possible_pay_status = ["authorized", "captured", "failed", "refunded"]
        payment_status = random.choices(possible_pay_status, weights=[0.5, 0.4, 0.05, 0.05], k=1)[0]

        shipping_speed = random.choice(["Standard", "Express", "Overnight"])
        shipping_cost = round(random.uniform(3.0, 25.0), 2)
        fc = random.choice(FULFILLMENT_CENTERS)

        currency_choice = random.choice(CURRENCY_OPTIONS)
        exchange_rate = EXCHANGE_RATES[currency_choice]

        env_fee = 0.0
        if any("Aquatic" in it.product.category or "Terrarium" in it.product.category for it in line_items):
            env_fee = round(random.uniform(1.0, 5.0), 2)

        tax_rate = round(random.uniform(0.05, 0.10), 2)

        loyalty_tier = self.generate_loyalty_tier()
        loyalty_points_used = 0
        if loyalty_tier in ["Gold", "Platinum"]:
            loyalty_points_used = random.randint(0, 1000)

        subscription_id = subscription_frequency = None
        if random.random() < 0.25:
            subscription_id = str(uuid.uuid4())
            subscription_frequency = random.choice(
                ["every 2 weeks", "every 4 weeks", "every month", "every 8 weeks"]
            )

        rscore = self.generate_risk_score(shipping_addr, billing_addr)
        fraud_flag = (rscore > 80)

        order_timestamp_str = self._get_next_timestamp_str()
        order_dt = datetime.strptime(order_timestamp_str, "%Y-%m-%dT%H:%M:%S.%f")

        shipping_status = random.choices(
            ["Pending", "Shipped", "Out for Delivery", "Delivered", "Returned"],
            weights=[0.3, 0.3, 0.1, 0.25, 0.05],
            k=1,
        )[0]

        delivered = "yes" if shipping_status == "Delivered" else "no"
        refunded = "yes" if random.random() < 0.10 else "no"

        expected_delivery_date = None

        delivery_date = None
        if shipping_status in ["Shipped", "Out for Delivery"]:
            expected_delivery_date = (order_dt + timedelta(days=random.randint(1, 7))).strftime(
                "%Y-%m-%d %H:%M:%S.%f"
            )[:-3]
        elif shipping_status == "Delivered":
            delivery_date = (order_dt + timedelta(days=random.randint(0, 2))).strftime(
                "%Y-%m-%d %H:%M:%S.%f"
            )[:-3]

        partial_refund_amount = round(random.uniform(1.0, 150.0), 2) if refunded == "yes" else 0.0

        order = Order(
            customer=customer,
            line_items=line_items,
            payment_info=payment_info,
            pet_name=pet_name,
            shipping_address=shipping_addr,
            billing_address=billing_addr,
            coupon_codes=coupon_codes,
            shipping_speed=shipping_speed,
            shipping_cost=shipping_cost,
            fulfillment_center=fc,
            timestamp=order_timestamp_str,
            shipping_status=shipping_status,
            expected_delivery_date=expected_delivery_date,
            delivery_date=delivery_date,
            refunded=refunded,
            delivered=delivered,
            payment_status=payment_status,
            payment_method=payment_method,
            partial_refund_amount=partial_refund_amount,
            currency=currency_choice,
            exchange_rate=exchange_rate,
            env_fee=env_fee,
            tax_rate=tax_rate,
            loyalty_points_used=loyalty_points_used,
            loyalty_tier=loyalty_tier,
            risk_score=rscore,
            fraud_flag=fraud_flag,
            subscription_id=subscription_id,
            subscription_frequency=subscription_frequency
        )

        if random.random() < 0.70 or shipping_status != "Pending":
            order.tracking_number = self._generate_tracking_number()
            order.shipping_provider = random.choice(self.shipping_providers)

        shipments = self.generate_partial_shipments(order.line_items)
        for s in shipments:
            if shipping_status == "Delivered":
                s.shipment_status = "Delivered"
                s.shipment_timestamp = delivery_date
            elif shipping_status in ["Shipped", "Out for Delivery"]:
                s.shipment_status = "Shipped"
                s.shipment_timestamp = order_timestamp_str
            else:
                s.shipment_status = shipping_status
            s.tracking_number = order.tracking_number or self._generate_tracking_number()
        order.shipments = shipments

        if refunded == "yes":
            order.status_history.append(OrderStatusHistory("Refunded").to_dict())

        return order

    def generate_clickstream_event(self, customer=None):
        """
        Creates a single random clickstream event dictionary,
        using the same day/time approach in ascending sequence.
        """
        event_time_str = self._get_next_timestamp_str()

        city, state, zipcode, area_code = USZipcodeLocationData.get_random_location()

        ip_address = f"198.{area_code % 256}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        geo_location = f"US-{state}"

        choice_roll = random.random()
        if choice_roll < 0.70:
            product_sku = random.choice(list(PRODUCT_CATALOG.keys()))
            product_info = PRODUCT_CATALOG[product_sku]
            page_name = "ProductDetailPage"
            page_url = (
                f"https://www.blewy.com/p/"
                + product_info["name"].lower().replace(" ", "-").replace("'", "")
                + f"/dp/{product_sku}"
            )
            product_id = product_sku
            product_name = product_info["name"]
            brand_name = "Blewy Brand"
            category_name = product_info["category"]
            price = product_info["price"]
        elif choice_roll < 0.80:
            page_name = "HomePage"
            page_url = "https://www.blewy.com"
            product_id = None
            product_name = None
            brand_name = None
            category_name = None
            price = None
        elif choice_roll < 0.85:
            page_name = "ContactUsPage"
            page_url = "https://www.blewy.com/contact"
            product_id = None
            product_name = None
            brand_name = None
            category_name = None
            price = None
        else:
            page_name = "CategoryPage"
            cat_sku = random.choice(list(PRODUCT_CATALOG.keys()))
            cat_info = PRODUCT_CATALOG[cat_sku]
            cat_slug = cat_info["category"].lower().replace(" ", "-").replace("(", "").replace(")", "")
            page_url = f"https://www.blewy.com/c/{cat_slug}"
            product_id = None
            product_name = None
            brand_name = None
            category_name = cat_info["category"]
            price = None

        event_type = random.choice([
            "page_view",
            "add_to_cart",
            "checkout",
            "search",
            "product_impression",
            "remove_from_cart"
        ])

        quantity = 1
        if event_type in ["add_to_cart", "remove_from_cart", "checkout"] and page_name == "ProductDetailPage":
            quantity = random.randint(1, 3)

        if customer is not None:
            user_id = customer.customer_id
        else:
            user_id = f"user-{random.randint(1000, 9999)}"

        session_id = f"sess-{uuid.uuid4()}"

        possible_referrers = [
            "https://www.google.com",
            "https://www.chewy.com",
            "https://www.amazon.com",
            "direct",
            "https://www.bing.com",
        ]
        referrer_url = random.choice(possible_referrers)

        user_login_status = random.choice(["logged_in", "guest"])
        loyalty_status = random.choice(["none", "silver", "gold", "platinum"])
        pet_pref = random.choice(["dog", "cat", "bird", "fish", "small_pet", "horse"])

        possible_campaigns = ["springsale-2025", "wintersale-2024", "emailpromo123", "none"]
        marketing_campaign_id = random.choice(possible_campaigns)
        if marketing_campaign_id == "none":
            marketing_campaign_id = None

        device_type = random.choice(["desktop", "mobile", "tablet"])
        browser_name = random.choice(["Chrome", "Firefox", "Safari", "Edge", "IE"])
        os_version = random.choice(["Windows 11", "MacOS 13", "iOS 16", "Android 12", "Linux"])
        app_version = None
        if device_type in ["mobile", "tablet"] and random.random() < 0.5:
            app_version = f"{random.randint(1, 3)}.{random.randint(0,9)}.{random.randint(0,9)}"

        language_pref = random.choice(["en-US", "en-GB", "es-ES", "fr-FR", "de-DE", "it-IT"])

        search_query = None
        search_results_count = None
        filters_applied = []
        if event_type == "search":
            search_query = random.choice(["plush dog toy", "cat food", "fish tank filter", "dog treats"])
            search_results_count = random.randint(10, 500)
            if random.random() < 0.5:
                filters_applied.append("size:medium")
            if random.random() < 0.3:
                filters_applied.append("material:plush")
            if random.random() < 0.2:
                filters_applied.append("flavor:chicken")

        cart_id = None
        cart_value_before_event = None
        cart_value_after_event = None
        if event_type in ["add_to_cart", "checkout", "remove_from_cart"]:
            cart_id = f"cart-{random.randint(1000, 9999)}"
            base_val = round(random.uniform(5.0, 100.0), 2)
            cart_value_before_event = base_val
            if event_type == "remove_from_cart":
                cart_value_after_event = round(base_val - random.uniform(1, 10), 2)
            else:
                cart_value_after_event = round(base_val + random.uniform(5, 20), 2)

        time_spent_on_page_ms = random.randint(500, 20000)
        promotion_code = None
        if random.random() < 0.2:
            promotion_code = random.choice(list(COUPON_DETAILS.keys()))
        page_load_time_ms = random.randint(100, 5000)
        customer_support_chat_opened = random.random() < 0.05

        evt = {
            "event_id": f"evt-{uuid.uuid4()}",
            "timestamp": event_time_str,
            "user_id": user_id,
            "session_id": session_id,
            "event_type": event_type,
            "page_url": page_url,
            "page_name": page_name,
            "referrer_url": referrer_url,
            "product_id": product_id,
            "product_name": product_name,
            "brand_name": brand_name,
            "category_name": category_name,
            "price": price,
            "quantity": quantity,
            "user_login_status": user_login_status,
            "loyalty_status": loyalty_status,
            "pet_preference": pet_pref,
            "marketing_campaign_id": marketing_campaign_id,
            "device_type": device_type,
            "browser_name": browser_name,
            "app_version": app_version,
            "os_version": os_version,
            "ip_address": ip_address,
            "geo_location": geo_location,
            "language_pref": language_pref,
            "search_query": search_query,
            "search_results_count": search_results_count,
            "filters_applied": filters_applied,
            "cart_id": cart_id,
            "cart_value_before_event": cart_value_before_event,
            "cart_value_after_event": cart_value_after_event,
            "metadata": {
                "is_first_visit": (random.random() < 0.3),
                "time_spent_on_page_ms": time_spent_on_page_ms,
                "promotion_code": promotion_code,
                "page_load_time_ms": page_load_time_ms,
                "customer_support_chat_opened": customer_support_chat_opened
            }
        }
        return evt

    def generate_multiple_clickstream_events(self, count, customer=None):
        """
        Generate multiple clickstream events in a batch.
        If 'customer' is None, we generate one new customer object
        and reuse it for all events.
        """
        if customer is None:
            customer = self.generate_customer_info()
        return [self.generate_clickstream_event(customer=customer) for _ in range(count)]

    def generate_multiple_orders(self, count, customer=None):
        """
        Generate multiple orders in a batch.
        If 'customer' is None, we generate one new customer object
        and reuse it for all orders.
        """
        if customer is None:
            customer = self.generate_customer_info()
        return [self.generate_order(customer=customer) for _ in range(count)]